import configparser

import json
import requests
import xmltodict
from requests.auth import HTTPBasicAuth
from requests.structures import CaseInsensitiveDict


class PentahoApiManager:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('../config.ini')
        self.url = config['PENTAHO']['url']
        self.user = config['PENTAHO']['username']
        self.password = config['PENTAHO']['password']

    def xmlTojson(self, xml):
        return json.dumps(xmltodict.parse(xml))

    def listPentahoUsers(self):
        response = requests.get(self.url + '/api/users' ,auth=HTTPBasicAuth(self.user, self.password))
        return str(self.xmlTojson(response.text))

    def listPentahoRoles(self):
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        response = requests.get(self.url + '/api/userrolelist/allRoles', headers=headers , auth=HTTPBasicAuth(self.user, self.password))
        return str(response.text)

    def listPentahoProyect(self):
        return  True

    # def createPentahoUser(self, user, password):
    #     data = {'user': user,'password':password}
    #     response = requests.put(self.url + '/api/userroledao/createUser', data= {'user': user,'password':password},
    #                             auth=HTTPBasicAuth(self.user, self.password))
    #     print(response)


def main():
    sammy = PentahoApiManager()
    sammy.listPentahoRoles


if __name__ == "__main__":
    main()