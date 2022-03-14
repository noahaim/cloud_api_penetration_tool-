class TestRes():
    def __init__(self, test_name, result, msg):
        self.test_name = test_name
        self.result = result
        self.msg = msg

    def writeToJson(self):
        return {"Test_name": self.test_name, "Result": self.result, "msg": self.msg}
