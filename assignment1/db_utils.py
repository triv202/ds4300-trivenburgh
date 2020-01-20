import sqlalchemy as sql


class DbUtils:
    def __init__(self):
        self.engine = sql.create_engine("mysql+pymysql://root:homesweethome@localhost/twitterdb")

    def create_connection(self):
        connection = self.engine.connect()
        return connection


    def insert_follower(self, user_id, follows_id):
        metadata = sql.MetaData(bind=self.engine)
        conn = self.create_connection()
        followers_table = sql.Table('followers', metadata, autoload=True)
        i = sql.insert(followers_table)
        i = i.values({"user_id": user_id, "follows_id": follows_id})
        conn.execute(i)
        print(f'{follows_id} follows {user_id}')
        conn.close()

    def insert_tweet(self, user_id, tweet_ts, tweet_text, tweet_number):
        metadata = sql.MetaData(bind=self.engine)
        conn = self.create_connection()
        tweet_table = sql.Table('tweets', metadata, autoload=True)
        i = sql.insert(tweet_table)
        i = i.values({"user_id": user_id, "tweet_ts": tweet_ts, "tweet_text": tweet_text})
        print(f'Tweet #:{tweet_number} made by user: {user_id}')
        conn.execute(i)
        conn.close()
