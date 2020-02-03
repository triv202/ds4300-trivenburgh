# ds4300-trivenburgh

## Abstract



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
   
## Results

| Strategy  | Tweets inserted/second  |  Timelines retreived/second |   
|:-:|---|---|
|  MySQL |  123.00 | 0.41  |   
|  Redis Strategy One |  1251.60 | 25.68  |   
|   Redis Strategy Two |   |   |   

