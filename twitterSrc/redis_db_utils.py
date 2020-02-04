import redis


class RedisDbUtils:
    def __init__(self):
        self.r = redis.Redis(host='localhost', port=6379, charset="utf-8", decode_responses=True)

    def add_follower(self, follower_id, user_id):
        self.r.sadd(f'{user_id}:followers', follower_id)
        self.r.sadd(f'{follower_id}:following', user_id)

    def get_followers(self, user_id):
        return self.r.smembers(f'{user_id}:followers')

    def get_following(self, user_id):
        return self.r.smembers(f'{user_id}:following')

    def get_next_tid(self):
        return self.r.incr("nextTweetID")

    def get_user_tweets(self, user_id):
        return self.r.lrange(f'{user_id}:tweets', 0, -1)


    def insert_tweet(self, user_id, tweet_txt, broadcast):
        tid = self.get_next_tid()
        self.r.set(tid, tweet_txt)
        if broadcast:
            followers = self.get_followers(user_id)
            for f in followers:
                self.r.lpush(f'{f}:timeline', tid)
        return self.r.lpush(f'{user_id}:tweets', tid)


    def get_timeline(self, user_id, broadcasted):
        if broadcasted:
            tweets = []
            for tid in self.r.lrange(f'{user_id}:timeline', 0, 9):
                tweets.append(self.r.get(tid))
            return tweets
        else:
            user_timeline_tids = []
            following = self.get_following(user_id)
            for f in following:
                user_timeline_tids += self.get_user_tweets(f)
            return self.generate_timeline(user_timeline_tids)

    def generate_timeline(self, tids):
        tweets = []
        sorted_tids = sorted(tids, key=lambda k: k, reverse=True)
        for tid in sorted_tids[0:10]:
            tweets.append(self.r.get(tid))
        return tweets