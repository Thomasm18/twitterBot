import tweepy
import time
import Auth

auth = tweepy.OAuthHandler(Auth.CONSUMER_TOKEN, Auth.CONSUMER_SECRET)
auth.set_access_token(Auth.KEY, Auth.SECRET)

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor): 	#Incase of too many hits on Twitter API
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(300)	#Pause for .3 sec

#Like Tweet on a Topic
search_string = "Python"
numberOfTweets = 1
for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
	try:
		tweet.favorite()
		print("Liked that tweet")
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break

#Follow back All your followers
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
	follower.follow()
	print(follower.name + " Followed")
	break


