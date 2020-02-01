import redis
import json


def sort_timeline(timeline):
    sorted_timeline = sorted(timeline, key=lambda k: k['tweet_ts'], reverse=True)
    return sorted_timeline[0:10]


class RedisDbUtils:
    def __init__(self):
        self.r = redis.Redis(host='localhost', port=6379, charset="utf-8", decode_responses=True)

    def add_follower(self, follower_id, follows_id):
        self.r.sadd(f'{follows_id}:followers', follower_id)

    def get_followers(self, user_id):
        return self.r.smembers(f'{user_id}:followers')

    def get_user_tweets(self, user_id):
        return self.r.lrange(f'{user_id}:tweets', 0, -1)

    def insert_tweet_one(self, user_id, tweet_ts, tweet_txt):
        tweet_dict = {"tweet_ts": tweet_ts, "tweet_txt": tweet_txt}
        tweet_json = json.dumps(tweet_dict)
        return self.r.rpush(f'{user_id}:tweets', tweet_json)

    def get_timeline_one(self, user_id):
        user_timeline = []
        followers = self.get_followers(user_id)
        for f in followers:
            tweets = self.get_user_tweets(f)
            for t in tweets:
                user_timeline.append(json.loads(t))
        return sort_timeline(user_timeline)


