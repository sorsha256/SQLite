import time
import json
import sqlite3
from SQLite import SQLite


class SQLite_Example:
    def __init__(self):
        self.sql = SQLite()
        self.sql.connect = sqlite3.connect(f'./base/Base.db')

    def insert(self):

        data = {'email': 'email@email.com', 'password': '12345qwerty!'}
        data = json.dumps(data)
        query = {'table': 'accounts', 'account_info': data, 'idx': 897899}
        # And as many arguments as you want to fill in the columns
        self.sql.insert(**query)  # if no problems return True


    def select(self):
        query = {'table': 'accounts', 'idx': 3}
        data = self.sql.select(**query)
        print(data)

        #  If there are more than 1 columns, then you need to put it in the list ['idx', 'shadow']
        query = {'table': 'accounts', 'column': ['idx', 'shadow'], 'shadow': 1}
        data = self.sql.select(**query)
        print(data)  # return data from table 'accounts' according to specified parameters

        query = {'table': 'accounts', 'country': 'US', 'fetchall': False}  # default fetchall=True
        data = self.sql.select(**query)
        print(data)  # return data from table 'accounts' according to specified parameters

        #  If column is 1, then the data type is string
        query = {'table': 'accounts', 'country': 'US', 'shadow': 1, 'column': 'idx'}
        data = self.sql.select(**query)
        print(data)  # return data from table 'accounts' according to specified parameters

    def update(self):

        # selector value type str!
        query = {'table': 'accounts', 'selector': {'idx': str(1), 'device_id': '12345'}, 'shadow': 0}
        self.sql.update(**query)  # return None

        query = {'table': 'accounts', 'selector': {'idx': str(1)}, 'shadow': 0, 'country': 'KZ', 'last_publish': time.time()}
        self.sql.update(**query)

        data = ['1', '2', 3]
        data = json.dumps(data)  # need json.dumps() if that dict, or list
        query = {'table': 'accounts',  'selector': {'idx': str(1)}, 'account_info': data}
        self.sql.update(**query)

        data = {'key0': 'value0', 'key1': 'value1'}
        data = json.dumps(data)  # need json.dumps() if that dict, or list
        query = {'table': 'accounts', 'selector': {'idx': str(1)}, 'account_info': data}
        self.sql.update(**query)

    def delete(self):
        self.sql.delete(table='accounts', columns='idx', value=0)
        # sorry, im very small used delete


if __name__ == "__main__":
    SQLite_Example().insert()
