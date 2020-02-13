# File to load tweets into db from file
import os
import sys
import json

sys.path.append(os.path.realpath(''))
from product_API import productAPI


def run():
    type = sys.argv[1]
    api = productAPI()
    if type == "setup":
        return api.setup_data()
    elif type == "query":
        if len(sys.argv) < 4:
            return print("Error: Please specify category then filters")
        category = sys.argv[2]
        filters = json.loads(sys.argv[3])
        return api.find_data(category, filters)
    else: return "Please specify valid action: setup or query"




if __name__ == '__main__':
    run()