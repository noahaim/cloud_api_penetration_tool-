import json


class API:
    def __init__(self, name,endpoint_url, port, github_link,tests):
        self.name = name
        self.endpoint_url = endpoint_url
        self.port = port
        self.github_link = github_link
        # self.queries = queries
        self.tests = tests
        self.runs = []

    def add_run(self,run):
        self.runs.append(run.writeToJson())

    def writeToJson(self):
        return {'name':self.name,'endpoint URL':self.endpoint_url,'endpoint port':self.github_link,'github link':self.github_link,'tests':self.tests,'runs':self.runs}