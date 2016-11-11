# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

print("""No output necessary although you 
	can print out a success/failure message if you want to.""")

import tweepy

consumer_key = "I1NE9EwNVekvFYkeiiwaoT3iZ"
consumer_secret = "injoKb5LWmAekKH9ALdscuG9B00Gs456kKi3Ykt2uwD3OD5QVM"
access_token = "250423934-mYtCr5i8RHFAN6bXl3sM9QxzgvNeqyazq19BlTbq"
access_secret = "J7rhELXeHkPQ6xDfMtqtxqrctiCmzCO8ZimcZrHnQ7ZDU"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

img = 'smile.png' 
txt = '#UMSI-206 #Proj3'

api.update_with_media(img,status=txt)

print ('The image was tweeted successfully')