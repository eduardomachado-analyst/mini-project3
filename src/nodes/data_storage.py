import pandas as pd
import logging

logger = logging.getLogger('nodes.data_storage')


def update(client, params):
    """
    Upload dataframe to database in PostgreSQL.
    """

    # Soap operas
    table_name = params.novelas.split('.')[0]

    df = params.novelas_df
    df.to_sql(table_name, con=client.conn, if_exists='replace', index=False)

    # Casting
    table_name = params.casting.split('.')[0]

    df = params.cast_df
    df.to_sql(table_name, con=client.conn, if_exists='replace', index=False)

    # Images
    table_name = params.features.split('.')[0]

    df = params.novelas_df
    df.to_sql(table_name, con=client.conn, if_exists='replace', index=False)

    # Feature by soap opera
    table_name = params.color_novela.split('.')[0]

    df = params.color_novela_df
    df.to_sql(table_name, con=client.conn, if_exists='replace', index=False)

    table_name = params.race_novela.split('.')[0]

    df = params.race_novela_df
    df.to_sql(table_name, con=client.conn, if_exists='replace', index=False)

    # IBGE
    table_name = params.ibge.split('.')[0]

    df = params.ibge_df
    df.to_sql(table_name, con=client.conn, if_exists='replace', index=False)


def done(client, params):
    """
    Check whether the table exists in the database AND it is populated.
    """
    table_name = params.ibge.split('.')[0]

    if client.engine.has_table(table_name):
        result = pd.read_sql(f'SELECT * FROM {table_name} LIMIT 5', con=client.conn)

        if result.shape[0] > 0:
            logger.info(f'Table {table_name} found in the database and it is populated. Skipping upload...')
            return True

    return False
