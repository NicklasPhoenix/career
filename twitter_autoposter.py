import tweepy
import random
import os
from datetime import datetime

# Twitter API credentials
auth = tweepy.OAuthHandler(
    os.environ['TWITTER_API_KEY'],
    os.environ['TWITTER_API_SECRET']
)
auth.set_access_token(
    os.environ['TWITTER_ACCESS_TOKEN'],
    os.environ['TWITTER_ACCESS_SECRET']
)
api = tweepy.API(auth)

TWEETS = [
    "🎯 Not sure what career to pursue? Our free analyzer matches your skills with high-paying careers. No signup required → ",
    "📊 Latest data: 65% of professionals want to change careers but don't know where to start. Try our free career matcher → ",
    "💼 From teacher to tech? Nurse to analyst? Our tool shows you exactly how to transition careers (free, no ads) → ",
    "🚀 Discover careers that match your skills + see real salaries + get transition roadmaps. 100% free tool → ",
    "📈 Average salary increase after strategic career change: 23%. Find your match with our free analyzer → "
]

HASHTAGS = [
    "#CareerChange #CareerAdvice",
    "#JobSearch #CareerTransition", 
    "#NewCareer #ProfessionalDevelopment",
    "#CareerGrowth #JobHunt",
    "#RemoteWork #CareerGoals"
]

def post_tweet():
    tweet_text = random.choice(TWEETS)
    hashtags = random.choice(HASHTAGS)
    url = "https://nicklasphoenix.github.io/career"
    
    full_tweet = f"{tweet_text}{url} {hashtags}"
    
    try:
        api.update_status(full_tweet)
        print(f"Tweeted: {full_tweet}")
    except Exception as e:
        print(f"Error tweeting: {e}")

if __name__ == "__main__":
    post_tweet()