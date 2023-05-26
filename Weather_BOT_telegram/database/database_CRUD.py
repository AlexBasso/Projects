from typing import List, Dict, TypeVar
from peewee import ModelSelect

from database.models import ModelBase, db


T = TypeVar('T')


def _store_date(db: db, model: T, *data: List[Dict]) -> None:
    """
    Private function that stores data in to DB. Uses peewee's atomic() for working with transactions.

    :param db: DB in which to store data
    :param model: Model in which to store data
    :param data: list of dictionaries based of the model.
    :return: None
    """
    with db.atomic():
        model.insert_many(*data).execute()


def _retrieve_all_data(db: db, model: T, *columns: ModelBase) -> ModelSelect:
    """
    Private function that retrieves data in to DB. Uses peewee's atomic() for working with transactions. Table is
    sorted by primary key(id) in descending order and has a limit of 10.

    :param db: DB in which to store data
    :param model: Model in which to store data
    :param columns: Columns to be retried form DB.
    :return: peewee.ModelSelect type object
    """
    with db.atomic():
        response = model.select(*columns).order_by(model.id.desc()).limit(value=10)

    return response


class CRUDInterface:
    """
    Base class interface for accessing private functions for storing and retrieving data
    """

    @classmethod
    def create(cls):
        """
        @Classmethod of CRUDInterface for storing new data in the DB.
        :return: private function for storing data
        """
        return _store_date

    @classmethod
    def retrieve(cls):
        """
        @Classmethod of CRUDInterface for retrieving data from the DB.
        :return: private function for retrieving data
        """
        return _retrieve_all_data


if __name__ == '__main__':
    CRUDInterface()
