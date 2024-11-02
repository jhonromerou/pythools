import json

import mysql.connector

envs = json.load(open("enviroments.json", 'r'))


class PersistenceManager:
    def get_connection(self, schemaName):
        dbEnvs = envs.get(schemaName)
        commConn = mysql.connector.connect(
            host=dbEnvs.get("host"),
            port=dbEnvs.get("port"),
            user=dbEnvs.get("user"),
            password=dbEnvs.get("pass"),
            database=dbEnvs.get("schema"))

        return commConn


persistence_manager2 = PersistenceManager()


class Connection:
    def __init__(self, connection_key: str):
        self.connection = persistence_manager2.get_connection(connection_key)

    def __cursor(self):
        return self.connection.cursor(dictionary=True)

    def fetch(self, table: str, fields: str, criteria: str, offset=0, limit=None | int, order_by=None,
              view_query=False) -> list[dict]:
        cursor = self.connection.cursor(dictionary=True)
        paginate = 'LIMIT {},{}'.format(offset, limit) if limit is not None else ''
        order_by_value = 'ORDER BY {}'.format(order_by) if order_by is not None else ''
        query = 'SELECT\n{}\nFROM {}\nWHERE {}\n{}\n{}'.format(fields, table, criteria, order_by_value, paginate)
        if view_query:
            print(query)
        cursor.execute(query)
        return cursor.fetchall()

    def update_one(self, table: str, fields: str, criteria: dict, view_query=False):
        cursor = self.__cursor()
        query = "UPDATE {} SET {} WHERE {} LIMIT 1".format(table, fields, Connection.__where__(criteria))
        if view_query:
            print(query)
        cursor.execute(query)
        self.connection.commit()

    def insert(self, table: str, data: dict, commited=True):
        cursor = self.__cursor()
        fields = ''
        values = ''
        for key in data:
            fields = fields + key + ', '
            values = "{}'{}', ".format(values, data[key])

        fields = fields[0:len(fields) - 2]
        values = values[0:len(values) - 2]
        query = "INSERT INTO {} ({}) VALUES ({})".format(table, fields, values)
        cursor.execute(query)
        if commited:
            self.connection.commit()

    def executemany(self, prepare_query: str, data: list, commited=True):
        cursor = self.__cursor()
        cursor.executemany(prepare_query, data)
        if commited:
            self.connection.commit()

    def cursor(self):
        return self.__cursor()

    def commit(self):
        self.connection.commit()

    @staticmethod
    def __where__(data: dict):
        criteria = ''
        for key in data:
            criteria = "{}{} = '{}' AND ".format(criteria, key, data[key])

        return criteria[0:len(criteria) - 5]
