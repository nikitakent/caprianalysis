import sqlalchemy as sa 
import pandas as pd
import numpy as np
import tweepy
import os

bearer_token = os.getenv("BEARER_TOKEN")
client = tweepy.Client(bearer_token=bearer_token)

## Cannot really access historical data, so we will just have to generate frequent requests to generate a backlog of data.
# Measure: LVMH, Kering, Richemont, Michael Kors, Coach, 
## Measures of brand popularity:
## General attention (Number of posts)
## Sentiment (Percentage of Negative posts vs Positive posts)
## Engagement (Number of likes, retweets, comments)
