from Database import Database
from Connections.PostgreSQL import PosgresSQLFactory
from Connections.MongoDB import MongoDBFactory


def client_code(db: Database):
   print(db.connect())


if __name__ == "__main__":
   print("Connecting to PostgreSQL...")
   client_code(PosgresSQLFactory())

   print("Connecting to MongoDB...")
   client_code(MongoDBFactory())
