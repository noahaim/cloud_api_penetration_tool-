import datetime

from run_class import Run

if __name__ == '__main__':
    time = datetime.datetime.now()
    r=Run(time)
    print(r.get_time())