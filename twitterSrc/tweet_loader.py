# File to load tweets into db from file
import os
import sys
import time

sys.path.append(os.path.realpath(''))
from redis_db_utils import RedisDbUtils


def load_tweets():
    if len(sys.argv) < 3:
        return print("Error: Please specify file path and insertion strategy")
    file_path = sys.argv[1]
    insert_option = sys.argv[2]

    db = RedisDbUtils()
    tweet_count = 1
    start_time = time.time()
    f = open(file_path, "r")
    for x in f:
        tweet_args = x.split(",")
        user_id = tweet_args[0].strip()
        tweet_text = tweet_args[2].strip()
        if insert_option == "one":
            db.insert_tweet(user_id, tweet_text, broadcast=False)
        elif insert_option == "two":
            db.insert_tweet(user_id, tweet_text, broadcast=True)
        else:
            return print("Error: Specify a valid insertion strategy")
        tweet_count += 1
    f.close()
    print("--- %s seconds total ---" % (time.time() - start_time))


if __name__ == '__main__':
    load_tweets()
