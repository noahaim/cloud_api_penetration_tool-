class Run:
  def __init__(self, date):
    self.day=date.day
    self.month=date.month
    self.year=date.year
    self.hour=date.hour
    self.minute=date.minute
    # self.results = results

  def get_date(self):
    return str(self.day)+"/"+str(self.month)+"/"+str(self.year)

  def get_time(self):
    return str(self.hour)+":"+str(self.minute)

  def writeToJson(self):
    return {'date': self.get_date(),'time':self.get_time()}
