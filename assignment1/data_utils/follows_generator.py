# File to generate followers for tweets
# Each of 10,000 users will have a random number of followers up to 100 each
import os
import sys
import random

sys.path.append(os.path.realpath('.'))
from db_utils import DbUtils


def generate():
    db = DbUtils()
    user_id_count = 0
    while user_id_count <= 10000:
        follower_count = random.randint(1, 100)  # Get number of followers for user
        follower_id_set = set()
        while follower_count > 0:
            follower_id = random.randint(1, 10000)  # Get follower user_id
            follower_id_set.add(follower_id)  # add to follower_id_set (ensure uniqueness)
            follower_count -= 1
        for follower_id in follower_id_set:
            if follower_id != user_id_count:  # can't follow yourself
                db.insert_follower(user_id=follower_id, follows_id=user_id_count)
        user_id_count += 1


if __name__ == '__main__':
    generate()
