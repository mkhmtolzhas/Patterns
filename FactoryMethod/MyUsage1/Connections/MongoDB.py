from Connection import Connection
from Database import Database


class MongoDBFactory(Database):
    def factory_method(self) -> Connection:
        return MongoDBConnection()


class MongoDBConnection(Connection):
    def connect(self) -> str:
        return "Connected to MongoDB"