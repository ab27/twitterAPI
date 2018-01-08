# twitterAPI

A python wrapper for the Twitter API

## Example Usage

```
>>> import twitter
>>> api = twitter.Api(consumer_key='consumer_key',
                      consumer_secret='consumer_secret',
                      access_token_key='access_token',
                      access_token_secret='access_token_secret')
>>> api.GetHomeTimeline()
```
