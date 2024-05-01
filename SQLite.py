import sqlite3
import time


class SQLite:
    connect = None
    
    def insert(self, table, **kwargs):
        connect = self.connect
        obj = connect.cursor()
        if len(kwargs) > 1:
            placeholder = ', '.join(['?' for _ in range(len(kwargs))])
            columns = ', '.join(kwargs.keys())
        else:
            placeholder = "?"
            columns = ''.join(kwargs.keys())

        query, value = f"INSERT INTO {table} ({columns}) VALUES({placeholder})", tuple(kwargs.values())
        try:
            obj.execute(query, value)
            connect.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def select(self, table, column=None, fetchall=True,  **kwargs):
        connect = self.connect
        obj = connect.cursor()

        if len(tuple(kwargs)) == 0:
            placeholder = ''
        elif len(tuple(kwargs)) == 1:
            placeholder = "WHERE {value}=?".format(value=''.join(kwargs.keys()))
        else:
            placeholder = "WHERE {value}".format(value=' AND '.join([f"{_}=?" for _ in kwargs.keys()]))
        if column:
            if isinstance(column, list):
                if len(column) > 1:
                    column = ', '.join(column)
            else:
                column = column
        else:
            column = "*"
        query, value = f"SELECT {column} FROM {table} {placeholder}", tuple(kwargs.values())
        if fetchall:
            return obj.execute(query, value).fetchall()
        else:
            return obj.execute(query, value).fetchone()

    def delete(self, table, columns, value):
        try:
            connect = self.connect
            obj = connect.cursor()
            obj.execute(f"DELETE FROM {table} WHERE {columns}=?", (value,))
            connect.commit()
        except Exception as ex:
            print(ex)
            self.delete(table, columns, value)

    def update(self, table, selector: dict = None, **kwargs):
        try:
            connect = self.connect
            obj = connect.cursor()
            if len(tuple(kwargs)) > 0:
                placeholder = ', '.join([f"{_}=?" for _ in kwargs.keys()])
            else:
                placeholder = f"{''.join(kwargs.keys())}=?"
            key = selector.keys()
            value = selector.values()
            if len(selector) >= 2:
                key = ' AND '.join([f"{_}=?" for _ in key])
                value = tuple(','.join([f"{_}" for _ in value]).split(','))
            else:
                key = ''.join(selector.keys()) + "=?"
                value = (''.join(selector.values()), )
            query, value = f"UPDATE {table} SET {placeholder} WHERE {key}", tuple(kwargs.values()) + value
            obj.execute(query, value)
            connect.commit()

        except Exception as ex:
            print(ex)
            time.sleep(2)
            self.update(table, selector, **kwargs)
