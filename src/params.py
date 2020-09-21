import os
import pandas as pd
from dotenv import load_dotenv


class Params:
    """
    Parameters class.

    This file centralizes anything that can be 
    parametrized in the code.

    If you want to use a parameter later in the code, you
    should instantiate params as:
    `params = Params()`, 
    send the object `params` within functions and, inside the 
    function, call the parameter as an attribute of the `params` object.

    For instance, if you have a parameter called `url` created here, you'd 
    call it in a function called `func` as:

    def func(params):
        ...
        url = params.url
        ...
    """
    # Data paths
    raw_data = os.path.abspath('../data/raw/')
    external_data = os.path.abspath('../data/external/')
    processed_data = os.path.abspath('../data/processed/')
    intermediate_data = os.path.abspath('../data/intermediate/')

    chromedriver = '../chromedriver'

    # Log file
    log_name = os.path.abspath('../log/log.log')

    # If this is set to True, then all the nodes will be automatically
    # considered not up-to-date and will be rerun.
    force_execution = False

    # Load environment variables from any .env files
    load_dotenv(os.path.abspath('../.env'))

    # Database connection params
    db_server = 'postgresql'
    user = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    host = 'localhost'
    database = "mini-project3"

    # URLs
    haystackapi = 'https://api.haystack.ai/api/image/analyze?output=json&apikey=' + os.getenv('KEYAPI')
    novelas_url = 'https://en.wikipedia.org/wiki/List_of_Rede_Globo_telenovelas#2000s'
    casting_url = ''

    # Filenames
    novelas = 'novelas.csv'
    casting = 'casting.csv'
    features = 'cast_features.csv'
    color_novela = 'color_novela.csv'
    race_novela = 'race_novela.csv'
    ibge = 'ibge_2018.csv'


    # DataFrames
    novelas_df = pd.DataFrame()
    cast_df = pd.DataFrame()
    features_df = pd.DataFrame()
    color_novela_df = pd.DataFrame()
    race_novela_df = pd.DataFrame()
    ibge_df = pd.DataFrame()


