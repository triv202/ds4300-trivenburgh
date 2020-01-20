# File to load tweets into db from file
import os
import sys
import time

sys.path.append(os.path.realpath('.'))
from db_utils import DbUtils


def load_tweets():
    start_time = time.time()
    if len(sys.argv) != 2:
        return print("Error: Please specify file path")
    file_path = sys.argv[1]
    f = open(file_path, "r")
    db = DbUtils()
    tweet_count = 1
    for x in f:
        tweet_args = x.split(",")
        user_id = tweet_args[0].strip()
        tweet_date_time = tweet_args[1].strip()
        tweet_text = tweet_args[2].strip()
        db.insert_tweet(user_id, tweet_date_time, tweet_text, tweet_count)
        tweet_count += 1
    f.close()
    print("--- %s seconds total ---" % (time.time() - start_time))


if __name__ == '__main__':
    load_tweets()
