# ds4300-trivenburgh

### Assignment 3 - Answers for part 1 are in the products.sql file

## Abstract
The goal of this experiment was to model Twitter's data needs and experiment with strategies to optimize data performance. Tweet data was falsified, written to a file, and loaded into a variety of data stores. Additionally, follower data was similarly mocked. The two main stores were a traditional MySQL database and a local redis store. With the Redis store, two slightly different strategies were implemented. For all three (MySQL and the two redis) tweets were inserted to the store to simulate posting and tweets/second were tracked. Likewise, for each retreiving a user's "timeline" was implemented, as the ten most recent tweets by people they follow. The results were fairly consistent with expectations with a redis strategy optimizing reading of timelines being the most efficient at doing so, and the redis strategy optimizing for easy "tweeting" or inserting being the best at doing so, as well. MySQL did perform better than the second redis strategy for inserts, but did not compete with either redis strategy for timeline reads.


## Methods
  The redis API was implemented using the following structure:
   * Tweets -- simple key, value store as tweet_id (referred to as tid in code): tweet_text
   * tweet_id was incremented by a nextTweetId redis counter 
   * user_id:tweets: list of tweet_id (a list of tweets for user as a tid reference to the master key,value store)
   * user_id:timeline: list of tweet_id (a list of tweets posted by other users as a tid reference to the master tweet key,value store)
   * user_id:followers: list of user_ids
   * user_id:following: list of user_ids
#### There were two strategies for posting tweets and generating timelines, as outlined by the assignment.
   ###### The first:
   * Handled posting by a simple generation of the next tweet_id, posting this tweet_id to the key value store with the tweet_text, and then posting the tweet_id to the user_id:tweets tweet_id list.
   * The concept of a "timeline" was generated from iterating through who a specific user was following and getting their tweet references hence on the fly buidling a timeline.
  ###### The second:
   * Posted tweets in the same way to the users own feed as strategy one
   * Also iterated through the users followers and posted the tweet_id to each followers timeline list
#### Both strategies are implemented in the current code.
  * To run a timeline retrieval test simply run the timeline_test.py file with either "one" or "two" as an option
  * i.e. `python timeline_test.py one`
  * Similarly, an insertion timing test can be done by running the tweet_loader.py script with a file of formatted tweets (tweets.txt works) and "one" or "two" as an option. `python tweet_loader.py tweets.txt two`
   
## Results

| Strategy  | Tweets inserted/second  |  Timelines retreived/second |   
|:-:|---|---|
|  MySQL |  123.00 | 0.41  |   
|  Redis Strategy One |  1251.60 | 25.68  |   
|   Redis Strategy Two | 89.71  |  799.64 |   

## Discussion

According to our results, our most performant insert strategy was the first redis strategy. This is no surprise as a simple insert into a redis key value store would most definitely be more optimal than writing to MySQL and strategy two is essentially strategy one with extra steps. Our optimal reading strategy by far was the second redis strategy. This was also to be expected. 
 
The magnitude of efficiency on these reads also is limited by the data we are using. By restricting each user to only 100 followers, the first redis strategy's reads may seem okay. As the number of followers grows, though, as it would with a real implementation of Twitter, the reads for this first strategy would continue to get worse. For the second redis strategy, the writes (tweet insertion) would get worse, but the timeline retrieval would continue to be performant. 
 
If this were to be a real implementation of Twitter, this write could be augmented by sending the timeline writes to a queue of somesort, improving the speed of writing by trading off data consistency for a user's followers. In the event, that a follower were to refresh their timeline at the exact time that a user was posting, the follower may just have to wait a few seconds or minutes to see this new tweet with this queuing strategy. Because the second strategy ensures a faster data read, and it's flaws can be mitigated through various strategies it is undoubtably the best for Twitter's data needs.

