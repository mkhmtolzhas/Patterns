from Connection import Connection
from Database import Database


class PosgresSQLFactory(Database):
    def factory_method(self) -> Connection:
        return PostgresConnection()


class PostgresConnection(Connection):
    def connect(self) -> str:
        return "Connected to PostreSQL"