import postgresql
from pretty_view import PrettyView


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
        self.pretty_view = PrettyView()

    def create_query(self, name, text):
        self.q[name] = text

    def use_query(self, name, *args):
        result_of_querry = self.db.query(self.q[name].format(*args))

        result = []
        if result_of_querry[0] not in ('INSERT', 'DELETE', 'UPDATE'):
            for stroke in result_of_querry:
                result.append(tuple(map(self.pretty_view, stroke)))
        else:
            result = result_of_querry

        return result
