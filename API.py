import json


class API:
    def __init__(self, endpoint_url, port, github_link,tests):
        self.endpoint_url = endpoint_url
        self.port = port
        self.github_link = github_link
        # self.queries = queries
        self.tests = tests
        self.runs = []

    def add_run(self,run):
        self.runs.append(run.writeToJson())

    def writeToJson(self):
        return {'endpoint URL':self.endpoint_url,'endpoin port':self.github_link,'github link':self.github_link,'tests':self.tests,'runs':self.runs}