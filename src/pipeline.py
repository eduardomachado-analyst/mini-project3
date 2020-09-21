import logging

from client import Client
from nodes import data_gathering
from nodes import data_storage
from nodes import data_transform
from params import Params


def process(client, params):
    """
    The ETL pipeline.

    It contains the main nodes of the extract-transform-load
    pipeline from the process.

    Parameters
    ----------

    client: Client
    parmas: Params

    Notes
    -----
    The main idea is to consider each task as a conceptual **node**.
    This function, `process` is the **pipeline** that integrates all
    tasks together. Each node is a .py file imported from the `nodes`
    directory.

    The main idea is that each node can be in one of the following state:
        - up-to-date: the task to be done given the input parameters is
        already completed. Hence, no rework is needed.

        - out-of-date: the task to be done is not completed and should be
        run.

    """

    if not data_gathering.done(client, params) or params.force_execution:
        data_gathering.update(client, params)

    if not data_transform.done(client, params) or params.force_execution:
        data_transform.update(client, params)

    if not data_storage.done(client, params) or params.force_execution:
        data_storage.update(client, params)


if __name__ == '__main__':
    params = Params()

    logging.basicConfig(filename=params.log_name,
                        level=logging.INFO,
                        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    client = Client(params)
    process(client, params)