import postgresql
import sqlite3
from pretty_view import PrettyView


class DB:
    queries = dict()
    pretty_view = PrettyView()
    query_exec = None

    def create_query(self, name, text):
        self.queries[name] = text

    def use_query(self, name, *args):
        result_of_query = [_ for _ in
                           self.query_exec(self.queries[name].format(*args))]
        if len(result_of_query) == 0:
            result_of_query.append(self.queries[name].split()[0])

        result = []
        if result_of_query[0] not in ('INSERT', 'DELETE', 'UPDATE'):
            for stroke in result_of_query:
                result.append(tuple(map(self.pretty_view, stroke)))
        else:
            result = result_of_query

        return result


class Postgres(DB):
    def __init__(self, url, port, login, password, name):
        self.url = url
        self.port = port
        self.login = login
        self.password = password
        self.name = name

        self.db = postgresql.open(
                "pq://{0}:{1}@{2}:{3}/{4}".format(login, password, url,
                                                  port, name))
        self.query_exec = self.db.query


class Sqlite3(DB):
    def __init__(self, filepath, name):
        self.filepath = filepath
        self.name = name

        self.db = sqlite3.connect(self.filepath)
        self.query_exec = self.db.execute
