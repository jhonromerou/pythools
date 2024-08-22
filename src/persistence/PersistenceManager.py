import mysql.connector
import json

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
