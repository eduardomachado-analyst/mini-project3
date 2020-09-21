import logging
import os
import re
import urllib.request
import pandas as pd
import requests
import unidecode
import wikipedia
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger('nodes.data_gathering')


def update(client, params):
    """
    Collect data and write the result in a file.
    """

    ## Wikipedia soap operas
    logger.info(f'Gathering data from {params.novelas_url}')

    response = requests.get(params.novelas_url)
    html = response.content
    soup = BeautifulSoup(html)

    # Search for tables on the page
    tables = soup.find_all('table', {'class': 'wikitable'})[35:-1]

    # Get the table with the name of soap operas and the aired year
    novelas_name = [tr.find('i').text for table in tables for tr in table.find_all('tr') if tr.find('i')]
    aired = [re.findall('\d* \w+ \d\d*', str(tr.find_all('td')))[0] for table in tables for tr in table.find_all('tr')
             if tr.find_all('td')]

    novelas_df = pd.DataFrame({'novela_name': novelas_name, 'aired': aired})

    # Write to log file and save the file to disk
    file_path = os.path.join(params.intermediate_data, params.novelas)
    logger.info(f'Storing results at {file_path}')
    novelas_df.to_csv(file_path, index=False)

    # Set the table in params for storage later
    params.novelas_df = novelas_df

    ## Get the list of casting
    wikipedia.set_lang("pt")

    cast_df = pd.DataFrame()

    # Search for the soap opera name and get the casting list
    for i, row in novelas_df.iterrows():
        soup = None
        try:
            query = row['novela_name'] + ' novela ' + row['aired'][-4:]
            soup = BeautifulSoup(wikipedia.page(query).html(), 'lxml')
        except:
            try:
                query = row['novela_name'] + ' (telenovela) ' + row['aired'][-4:]
                soup = BeautifulSoup(wikipedia.page(query).html(), 'lxml')
            except:
                print(row['novela_name'])
        if soup:
            foundid = soup.find('span', {'id': 'Elenco'})
            table = foundid.findNext('table')
            cast = [tr.find('td').text.strip().replace('\n', '') for tr in table.find_all('tr') if tr.find('td')]
            cast_df = cast_df.join(pd.DataFrame({row['novela_name']: cast}), how='outer')

    # Remove the accentuation in names
    for i in cast_df:
        cast_df[i] = [unidecode.unidecode(str(x).split(' (')[0].split('[')[0].strip()) for x in cast_df[i]]

    # Replace nan string to type NaN
    cast_df = cast_df[cast_df != 'nan']

    mask = cast_df.count().sort_values() < 30
    drop_cols = mask[mask].index
    cast_df = cast_df.drop(drop_cols, axis=1)

    # Write to log file and save the file to disk
    file_path = os.path.join(params.intermediate_data, params.casting)
    logger.info(f'Storing results at {file_path}')
    cast_df.to_csv(file_path, index=False)

    # Set the table in params for storage later
    params.cast_df = cast_df

    ## Get the pictures of casting from Google
    chrome_path = params.chromedriver

    # Open the chrome browser
    driver = webdriver.Chrome(executable_path=chrome_path)

    file_path = os.path.join(params.external_data, '/images/')

    # Get the casting names and search on Google images to get the first one
    cast_lst = list(set([x for i in cast_df for x in cast_df[i]]))

    for i in cast_lst:
        if len(i.split(' ')) > 1:
            url = f'https://www.google.com/search?as_st=y&tbm=isch&hl=pt-PT&as_q="{i}"+ator+atriz+"globo"+"novela"&as_epq=&as_oq=&as_eq=&cr=countryBR&as_sitesearch=&safe=images&tbs=ctr:countryBR,itp:face,ic:color '

            # Navigate to webpage
            driver.get(url)

            img = WebDriverWait(driver, 3600).until(EC.presence_of_element_located((By.TAG_NAME, 'img')))
            src = img.get_attribute('src')

            # Download the image
            fullfilename = os.path.join(file_path, f'{i}.jpg')
            urllib.request.urlretrieve(src, fullfilename)

    driver.close()

    # List the filenames of the images
    files = os.listdir(file_path)

    # Apply the haystack API to analyze the race and gender
    df_data_cast = pd.DataFrame()
    not_found = 0
    for i in files:
        try:
            r = requests.post(params.haystackapi, data=open(f"{file_path}{i}", 'rb'))
            gender = r.json()['people'][0]['gender']['gender']
            race = r.json()['people'][0]['ethnicity']['ethnicity']
            df_race = pd.DataFrame({'name': [unidecode.unidecode(i[:-4])], 'race': [race], 'gender': [gender]})
            df_data_cast = pd.concat([df_data_cast, df_race])
        except:
            not_found += 1

    # Separate by Black, Latin and White
    df_data_cast['color'] = df_data_cast['race'].apply(
        lambda x: 'Black' if 'Black' in x else ('Latin' if 'Latin' in x else 'White'))

    # Write to log file and save the file to disk
    file_path = os.path.join(params.intermediate_data, params.features)
    logger.info(f'Storing results at {file_path}')
    df_data_cast.to_csv(file_path, index=False)

    # Set the table in params for storage later
    params.features_df = df_data_cast


def done(client, params):
    """
    Return whether the file to be downloaded already exists or not.
    """
    # Extract date
    for filename in (params.features, params.casting, params.novelas):
        file_path = os.path.join(params.intermediate_data, filename)

        if os.path.exists(file_path):
            logger.info(f'{file_path} found.')
        else:
            return os.path.exists(file_path)
    return os.path.exists(file_path)
