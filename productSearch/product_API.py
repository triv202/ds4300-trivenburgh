from pymongo import MongoClient


class watchAPI:
    def __init__(self):
        self.client = MongoClient()


    def setup_data(self):
        db = self.client["watchDB"]
        watch_col = db["watches"]
