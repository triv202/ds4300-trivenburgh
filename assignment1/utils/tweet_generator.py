# File to generate one million tweets and save to text file
import random
import datetime
import string


def generate():
    results = open('../tweets.txt', 'w')
    count = 0
    while count <= 1000000:
        results.write(get_next_tweet() + '\n')
        count+= 1
    else:
        results.close()


def get_next_tweet():
    user_id = random.randint(1, 10000)  # Ten Thousand Users
    tweet_ts = get_random_date().strftime("%m/%d/%Y, %H:%M:%S")
    tweet_text = ''.join(random.choices(string.ascii_uppercase, k=140))
    return f'{user_id}, {tweet_ts}, {tweet_text}'


def get_random_date():
    today = datetime.datetime.now()
    start_date = datetime.datetime(2006, 7, 15)  # Twitter's Public Release Date
    delta = today - start_date
    return start_date + datetime.timedelta(days=random.randint(1, delta.days),
                                           hours=random.randint(0, 24),
                                           minutes=random.randint(0, 60),
                                           seconds=random.randint(0, 60))


if __name__ == '__main__':
    generate()