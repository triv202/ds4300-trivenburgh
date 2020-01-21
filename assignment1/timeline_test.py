# File to load tweets into db from file
import os
import sys
import time
import random

sys.path.append(os.path.realpath(''))
from db_utils import DbUtils


def retrieve_timelines():
    t_end = time.time() + 60 * 3  # run for 3 minutes
    timeline_count = 0
    db = DbUtils()
    while time.time() < t_end:
        user_id = random.randint(1, 10000)  # Ten Thousand Users
        db.get_timeline(user_id)
        timeline_count += 1
    print(f'Total timelines retrieved in three minutes: {timeline_count}')


if __name__ == '__main__':
    retrieve_timelines()
