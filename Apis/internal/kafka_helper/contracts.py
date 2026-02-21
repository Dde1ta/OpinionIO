from pydantic import BaseModel


class BaseContract(BaseModel):
    id: int


class UserMetrics(BaseModel):
    user_id: int
    followers: int
    verified: int


class TweetMetrics(BaseModel):
    tweet_id: int
    retweet_count: int
    reply_count: int
    like_count: int
    quote_count: int


class Metrics(BaseModel):
    user: UserMetrics
    tweet: TweetMetrics


class Tweet(BaseModel):
    tweet_id: int
    text: str
    lang: str
    metrics: Metrics


class MetaDataContract(BaseContract):
    tweets: list[Tweet]


class TaskDataContract(MetaDataContract):
    ...


class ToPredictTweet(BaseModel):
    tweet_id: int
    text: str


class InfluentialTask(BaseContract):
    X: list[ToPredictTweet]


class BulkTask(InfluentialTask):
    ...


class Results(BaseModel):
    tweet_id: int
    negative: float
    positive: float


class CompletedInfluentialTaskContract(InfluentialTask):
    y: list[Results]


class CompletedBulkTaskContract(CompletedInfluentialTaskContract):
    ...

