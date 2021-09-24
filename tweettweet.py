import tweepy
import time

auth = tweepy.OAuthHandler("PW09ETtPTSjC8AhuWWWuk1DoM", "V0qwoJloGaROVpvlGFS5mY08ugAdRKgLA4LfTPCDjhtiDrIrgk")
auth.set_access_token("1250596077562138624-K37ep1LFWvSl5zrJ7AIlw6rphAbxpm", "tUKoC6BWsCHhmOqBBn3bbf7Cnf2gJjR9VOpFIVdrKfvg4")

api = tweepy.API(auth) # we now have access to api
user = api.me()

def limit_handler(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(1000)



#Generous Bot
#for follower in tweepy.Cursor(api.followers).items():
	#if follower.name == "RAZE《》C0rrupted_id3ntity":
		#follower.follow()
		#break

search_string = "python"
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
	try:
		tweet.favorite()
		print("i liked that tweet")
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break