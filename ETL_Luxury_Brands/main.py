import sqlalchemy as sa 
import pandas as pd
import numpy as np
import tweepy
import os

bearer_token = os.getenv("BEARER_TOKEN")

client = tweepy.Client(bearer_token=bearer_token)
