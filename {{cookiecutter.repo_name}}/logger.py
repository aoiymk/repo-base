import logging as log
import os

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=Singleton):
    log.basicConfig(
        format='[%(asctime)s] %(message)s',
        level=log.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def get_dataframe_info(dataframe):
    return '[columns={0}, size={1}]'.format(dataframe.columns.values, len(dataframe.index))

def notify(message,title=os.getcwd().split('/')[-1]):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(message, title))
