import os
from itertools import chain

from sqlalchemy import create_engine, MetaData, insert, select

from database import models


class DataBase:
    def __init__(self, name):
        self.name = name
        self.metadata = MetaData()
        self.engine = create_engine(f"sqlite:///{name}.sqlite3")

    def create_all_tables(self):
        if not os.path.exists(self.name):
            models.Base.metadata.create_all(self.engine)

    def engine_connect(self, query, isReturn=False):
        with self.engine.connect() as connection:
            if isReturn:
                return connection.execute(query)
            connection.execute(query)

    def select_query(self, query, return_type: int):
        with self.engine.connect() as connection:
            if return_type == 1:
                return list(chain.from_iterable(connection.execute(query).fetchall()))
            elif return_type == 2:
                return connection.execute(query).fetchone()[0]
            elif return_type == 3:
                return connection.execute(query).fetchall()

    def get_last_index(self, table):
        try:
            index = str(sorted(self.select_query(select(table), 1))[-1] + 1)
        except IndexError:
            index = str(0)
        return index

    def insert_query(self, table, *args):
        self.engine_connect(insert(table).values(args))
