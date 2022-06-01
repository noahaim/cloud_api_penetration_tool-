import json


class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.api_list = []

    def __init__(self, name, email,apiList):
        self.name = name
        self.email = email
        self.api_list = apiList

    def add_api(self,api):
        self.api_list.append(api.writeToJson())

    def writeToJson(self):
        return {'name':self.name,'email':self.email,'apiList':self.api_list}

