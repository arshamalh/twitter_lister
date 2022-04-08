from pymongo import MongoClient
from config import get_config

client = MongoClient(get_config("MONGODB_URI", "mongodb://Arsham:tmdbTops@localhost:27008/tweets?authSource=admin"))
database = client.get_database(get_config("DATABASE_NAME", "tweets"))
LikedTweetsCollection = database.get_collection("liked_tweets")
InfluencersTweetCollection = database.get_collection("influencers_tweets")
