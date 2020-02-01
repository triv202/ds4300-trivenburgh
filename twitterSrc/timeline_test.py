# File to load tweets into db from file
import os
import sys
import time
import random

sys.path.append(os.path.realpath(''))
from redis_db_utils import RedisDbUtils


def retrieve_timelines():
    timeline_strategy = sys.argv[1]
    t_end = time.time() + 60 * 3  # run for 3 minutes
    timeline_count = 0
    db = RedisDbUtils()
    while time.time() < t_end:
        user_id = random.randint(1, 10000)  # Ten Thousand Users
        if timeline_strategy == "one":
            db.get_timeline_one(user_id)
        elif timeline_strategy == "two":
            db.get_timeline_two(user_id)
        else:
            return print("Error: Specify a valid timeline strategy")
        timeline_count += 1
    print(f'Total timelines retrieved in three minutes: {timeline_count}')


if __name__ == '__main__':
    retrieve_timelines()
