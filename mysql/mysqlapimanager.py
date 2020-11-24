import configparser
import pymysql
import json,jsonify

class MysqlApiManager:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('../config.ini')
        self.host = config['MYSQL']['host']
        self.user = config['MYSQL']['username']
        self.password = config['MYSQL']['password']
        self.port = config['MYSQL']['port']



    def showListDatabase(self):
        connection = pymysql.connect(host="localhost", user="root", passwd="pinone32", database="sample")
        cursor = connection.cursor()
        # Query for creating table
        ArtistTableSql = "SHOW DATABASES"

        cursor.execute(ArtistTableSql)
        #rows = cursor.fetchall()
        row_headers = [x[0] for x in cursor.description]  # this will extract row headers
        rv = cursor.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        print(json.dumps(json_data))
        print(json.dumps(rv, indent=4))

        # commiting the connection then closing it.
        connection.commit()
        connection.close()

        return True


    def createUser(self, user):
        return True


if __name__ == "__main__":
    mysql = MysqlApiManager()
    mysql.showListDatabase()