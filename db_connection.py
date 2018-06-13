import postgresql
import pandas as pd


class DB:
    def __init__(self, url, port, login, password, name):
        self.url = url
        self.port = port
        self.login = login
        self.password = password
        self.name = name

        self.db = postgresql.open(
            "pq://{0}:{1}@{2}:{3}/{4}".format(login, password, url,
                                              port, name))
        self.q = dict()

    def create_query(self, name, text):
        self.q[name] = text

    def use_query(self, name, *args):
        temp = pd.DataFrame(self.db.query(self.q[name].format(*args)))
        return temp
