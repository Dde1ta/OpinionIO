# This is so that I do not lose my mind :D


## External -> Kafka Produces
1. NEW_TASK

## Internal

    METADATA COLLECTOR
        Consumes :->
            1. NEW_TASK
        
        Produces :->
            1. META_DATA
    
    METADATA PROCESSER
        Consumes :->
            1. META_DATA
        
        Produces :->
            1. TASK_DATA

    METADATA DISPATCHER
        Consumes :->
             1. TASK_DATA
        
        Produces :->
            1. INFLUENTIAL_TASK
            2. BULK_TASK
    
    TINY BERT
        Consumes :->
            1. INFLUENTIAL_TASK
        
        Produces :->
            1. COMPLETED_INFLUENTIAL_TASK

    XGBOOST (2 Containers)
        Consumes :->
            1. BULK_TASK

        Produces :->
            1. COMPLETED_BULK_TASK
    
    INFLUENTIAL RESULT
        Consumes :->
            1. COMPLETED_INFLUENTIAL_TASK
        
        Sets it on the Database Table Influential :)

    XGBOOST RESULT
        Consumes :->
            1. COMPLETED_BULK_TASK
        
        Sets it on the Database Table Bulk :)
        

## Contracts

### NEW_TASK
    
    TaskContract :
        id: int
        topic: int
        region: int

### META_DATA
#### sample tweet fetch

```json
{ 
  "id": "2023282727802560990",
  "author_id": "823844920074981376",
  "text": "India is hosting the India-AI Impact Summit 2026 in New Delhi from 16-20 February 2026.\n#AISummitIndia http s ://t.co/0HS96ZDAHW",
  "lang": "en",
  "created_at": "2026-02-16T06:26:07.000Z",
  "public_metrics":
    { 
      "retweet_count": 0,
      "reply_count": 0, 
      "like_count": 0, 
      "quote_count": 0
    }
}
```
    UnprocessedTweets:
        tweet_id: int
        text: string
        lang: string
        metrics: {User, Tweet}
    
    MetaDataContract:
        id: int
        tweets: [UnprocessedTweets]
    
    User:
        user_id: int
        followers: int
        verified: boolean
    
    Tweet:
        tweet_id: int
        retweet_count: int
        reply_count: int 
        like_count: int 
        quote_count: int

### TASK_DATA

    TaskDataContract:
        id: int
        tweets: [ProcessedTweet]
    
    
    ProcessedTweet:
        tweet_id: int
        text: String (Cleaned)
        metrics: {User, Tweet}

### INFLUENTIAL_TASK

    InfluentialTask:
        id: int
        X: [PredictTweet]
    
    PredictTweet:
        tweet_id: int
        text: string

### BULK_TASK
    
    BulkTask:
        id: int
        X: [PredictTweet]

### COMPLETED_INFLUENTIAL_TASK

    CompletedInfluentialTaskContract:
        id: int
        X: [PredictTweet]
        y: [Results]

    Results:
        tweet_id: int
        negative: float
        positive: float

### COMPLETED_BULK_TASK

    CompletedBulkTaskContract:
        id: int
        X: [PredictTweet]
        y: [Results]

    Results:
        tweet_id: int
        negative: float
        positive: float



