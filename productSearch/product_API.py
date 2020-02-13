from pymongo import MongoClient


class productAPI:
    def __init__(self):
        self.client = MongoClient()


    def setup_data(self):
        db = self.client["productDB"]
        product_collection = db["products"]
        test_data = [
            {"category": "watch", "diameter": "44mm", "brand": "Tommy Hilfiger", "dial_color": "Beige"},
            {"category": "watch", "diameter": "42mm", "brand": "Ralph Lauren", "dial_color": "Blue"},
            {"category": "watch", "diameter": "44mm", "brand": "Seiko", "dial_color": "Blue"},
            {"category": "watch", "diameter": "42mm", "brand": "Timex", "dial_color": "White"},
            {"category": "watch", "diameter": "44mm", "brand": "Tommy Hilfiger", "dial_color": "Black"},
            {"category": "wine", "winery": "Yellow Tail", "type": "Pinot Noir", "year_bottled": "2012"},
            {"category": "wine", "winery": "Barefoot", "type": "Cabernet Sauvignon", "year_bottled": "2005"},
            {"category": "wine", "winery": "Dark Horse", "type": "Zinfandel", "year_bottled": "1999"},
            {"category": "wine", "winery": "Yellow Tail", "type": "Chardonnay", "year_bottled": "2018"},
            {"category": "wine", "winery": "Kim Crawford", "type": "Sauvignon Blanc", "year_bottled": "2019"}
        ]

        result = product_collection.insert_many(test_data)
        return print(result.inserted_ids)

    def find_data(self, category, filters):
        db = self.client["productDB"]
        product_collection = db["products"]
        category_dict = {"category": category}
        query = {**category_dict, **filters}
        results = product_collection.find(query)

        if results.count() != 0:
            for x in results:
                print(x)
        else:
            print("No results found. Try again with different parameters.")


