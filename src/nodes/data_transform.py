import pandas as pd
import os
import logging
from datetime import datetime

logger = logging.getLogger('nodes.data_transform')


def feat_novelas(client, params, feature):
    """"
    This function get the table from data base and transform to clean csv file
    """
    table_casting = params.casting.split('.')[0]
    table_features = params.features.split('.')[0]
    table_novelas = params.novelas.split('.')[0]

    # Read table from SQL
    cast_df = pd.read_sql_query(f'SELECT * FROM {table_casting};', con=client.conn)
    feat_df = pd.read_sql_query(f'SELECT * FROM {table_features};', con=client.conn)
    novelas_df = pd.read_sql_query(f'SELECT * FROM {table_novelas};', con=client.conn)

    # Replace the name of casting to their features
    f = feat_df[feature].unique()
    feature_novela = pd.DataFrame(index=cast_df.columns, columns=f).sort_index()
    for i, item in feat_df.iterrows():
        cast_df.replace(item['name'], item[feature], inplace=True)

    # The total of ehtnicity by soap operas
    for i in f:
        feature_novela[i] = cast_df[cast_df == i].count().sort_index()

    feature_novela.reset_index(inplace=True)
    feature_novela.rename(columns={'index': 'novela_name'}, inplace=True)

    # Insert the aired year to new table
    feature_novela = feature_novela.merge(novelas_df, left_on='novela_name', right_on='novela_name')
    feature_novela['aired_year'] = feature_novela['aired'].apply(
        lambda x: datetime.strptime(x, '%d %B %Y').strftime('%Y'))

    # Write the file to disk
    filename = feature + '_novela.csv'
    file_path = os.path.join(params.processed_data, filename)
    logger.info(f'Storing results at {file_path}')
    feature_novela.to_csv(file_path, index=False)

    return feature_novela


def clean_ibge_data(client, params):
    """
    This function get the IBGE dataframe from database and clean it
    """
    file_path = os.path.join(params.external_data, params.ibge)
    ibge_data = pd.read_csv(file_path, sep=';')

    # Use the 2018 column
    ibge_data.drop(columns=['2015', '2016', '2017'], axis=1, inplace=True)

    # Split by indicators
    if not os.path.exists(os.path.join(params.intermediate_data, 'Geral.csv')):
        for i in range(1, 6):
            category_df = ibge_data.loc[ibge_data['Nível'].str.startswith(str(i))].reset_index(drop=True)
            filename = category_df.loc[0, 'Indicador'] + '.csv'

            file_path = os.path.join(params.intermediate_data, filename)
            logger.info(f'Storing results at {file_path}')
            category_df.to_csv(file_path, index=False)

    # Population dataframe
    file_path = os.path.join(params.intermediate_data, 'Geral.csv')
    df = pd.read_csv(file_path)
    df = df.iloc[[3, 4], 1:]
    file_path = os.path.join(params.processed_data, 'population.csv')
    logger.info(f'Storing results at {file_path}')
    df.to_csv(file_path, index=False)

    # Education dataframe
    file_path = os.path.join(params.intermediate_data, 'Educação.csv')
    education_df = pd.read_csv(file_path)
    df = education_df.iloc[[4, 5], 1:]
    file_path = os.path.join(params.processed_data, 'illiteracy.csv')
    logger.info(f'Storing results at {file_path}')
    df.to_csv(file_path, index=False)

    df = education_df.iloc[[34, 35], 1:]
    file_path = os.path.join(params.processed_data, 'higher_education.csv')
    logger.info(f'Storing results at {file_path}')
    df.to_csv(file_path, index=False)

    # Employment dataframe
    file_path = os.path.join(params.intermediate_data, 'Trabalho.csv')
    employment_df = pd.read_csv(file_path)
    df = employment_df.iloc[[11, 12], 1:]
    file_path = os.path.join(params.processed_data, 'unemployment.csv')
    logger.info(f'Storing results at {file_path}')
    df.to_csv(file_path, index=False)

    df = employment_df.iloc[[38, 39], 1:]
    file_path = os.path.join(params.processed_data, 'income.csv')
    logger.info(f'Storing results at {file_path}')
    df.to_csv(file_path, index=False)

    # Join IBGE data base


def join_ibge_data(params):
    """
    Join the files that it will use for reporting
    """
    filenames = ['higher_education', 'illiteracy', 'income', 'population', 'unemployment']

    df = pd.DataFrame({'Indicador': ['Brancos', 'Pretos ou pardos']})
    for f in filenames:
        new_df = pd.read_csv(os.path.join(params.processed_data, f'{f}.csv'), usecols=['Indicador', '2018'])
        new_df.rename(columns={'2018': f}, inplace=True)

        df = new_df.merge(df)

    # Replace percentage to numbers
    df['unemployment'] = df['unemployment'] * df['population']
    df['illiteracy'] = df['illiteracy'] * df['population']
    df['higher_education'] = df['higher_education'] * df['population']

    # Set the table in params for storage later
    params.ibge_df = df

    # Write to log file and save the file to disk
    file_path = os.path.join(params.processed_data, params.ibge)
    logger.info(f'Storing results at {file_path}')
    df.to_csv(file_path, index=False)


def update(client, params):

    params.race_novela_df = feat_novelas(client, params, 'race')
    params.color_novela_df = feat_novelas(client, params, 'color')

    clean_ibge_data(client, params)

    join_ibge_data(params)


def done(client, params):
    """
    Return whether the file to be downloaded already exists or not.
    """
    # Soap Operas data
    file_path = os.path.join(params.processed_data, params.ibge)

    if os.path.exists(file_path):
        logger.info(f'{file_path} found.')

    return os.path.exists(file_path)
