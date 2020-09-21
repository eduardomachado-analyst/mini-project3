from sqlalchemy import create_engine
import logging
import pandas as pd

logger = logging.getLogger('client.py')


class Client:
    """
    Connection to the database.

    The current implementation only refers to the PostgreSQL
    database, however, this could be easily enhanced to any
    database at all, including cloud.
    """

    def __init__(self, params):
        """
        Connect to the database.

        Use the information contained in the params.py file
        to connect to the postgreSQL database.
        """

        try:

            self.engine = create_engine(
                f'{params.db_server}://{params.user}:{params.password}@{params.host}/{params.database}')
            self.conn = self.engine.connect()
            logger.info(f'Connected to PostgreSQL@{params.database}')

        except Exception as e:
            logger.warning('Could not connect to the database on client.py file.')
            logger.warning('Verify your credentials for {params.user}.')
            logger.warning(e)

    def create_table_db(self, df, name_tbl):
        """
        This functions creates a table into the data base
        """
        df.to_sql(name=name_tbl, con=self.conn, if_exists='replace', index=False)

    def read_table_db(self, name_tbl):
        return pd.read_sql_query(f'SELECT * FROM {name_tbl};', con=self.conn)
