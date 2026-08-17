from pymongo import MongoClient
from pymongo.database import Database

from core.data.Data import HOST, MONGO_PORT


class Mongo_impl:
    client: MongoClient
    db: Database

    def __init__(self, db_name):
        self.client = MongoClient(host=HOST, port=MONGO_PORT)
        self.db = self.client[db_name]
        self.collection = self.db['projectcollection']

    def insert(self) -> None:
        self.collection.insert_one()

    def update(self) -> None:
        self.collection.update_one()

    def delete(self) -> None:
        self.collection.delete_one()

    def find(self):
        document = self.collection.find_one()
        if document:
            return document
        return None
