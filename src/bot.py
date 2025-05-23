import sys
import os

# Add parent folder to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now import the function
from twitter_python import get_api , get_client



# profile pic

def profile_image(filename) :
    api = get_api()
    try :
        api.update_profile_image(filename)
        print(f"Sucessfull")
    except Exception as e :
        print(f"Failed")
    
#info  or description 
def update_profile_info(name, bio, location, website):
    api = get_api()
    try :
        api.update_profile(name=name, description=bio, location=location, url=website)
        print(f"sucessfull")
    except Exception as e :
        print(f"failed")


#psot_tweet 
"""def post_tweet(text) :
    api = get_api()
    try : 
        api.update_status(status=text)
        print(f"sucessfull")
    except Exception as e :
        print(f"failed")
"""
 

#post_tweet , v2 tweepy
def post_tweet(text) :
    client = get_client()
    try : 
        client.create_tweet(text=text)
        print(f"sucessfull")
    except Exception as e :
        print(f"failed")

#upload_media 
def upload_media(text: str, filename: str) -> None:
    """
    Uploads media to Twitter and posts a tweet with the uploaded media.

    Parameters:
    - text (str): The tweet text.
    - filename (str): The path to the media file to upload.
    """
    client = get_client()
    api = get_api()
    try:
        media = api.media_upload(filename=filename)
        client.create_tweet(text=text, media_ids=[media.media_id_string])
        print("Tweet with media posted successfully.")
    except Exception as e:
        print(f"Failed to post tweet with media: {e}")


#retweet
def retweet(id,text) :
    client = get_client()
    try :
        client.create_tweet(in_reply_to_tweet_id = id , text = text )
        print(f"sucessfully retweet")
    except Exception as e :
        print(f"failed to retweet")

#unretweet use v2 client  x  api
def unretweet(id):
    api = get_api()
    client = get_client()
    client.unretweet(str(id))

# reply this wil mvp or greate pipeline later on 

"""def reply(tweet_id , message ) :
    api = get_api()
    tweet = api.get_status(str(tweet_id))
    print(tweet)"""

def reply(text,id):
    client = get_client()
    client.create_tweet(text = text , in_reply_to_tweet_id= id)


#try to fetch username :
def username(id):
    client = get_client()
    response = client.get_user(id=str(id))
    print(response)  # <-- Debug: See full response
    
    if response.data:
        print("Username:", response.data.username)
    else:
        print("User not found.")

username(1925612480862036470)





#timeline of home pages tweets 

# this is client based approach need x API V2 , but we dont need as per current requirement 
def fetch_home_timeline():
    api = get_api()
    try:
        tweets = api.home_timeline()
        for tweet in tweets:
            print(f"Tweet ID: {tweet.id}\nContent: {tweet.text}\n")
    except Exception as e:
        print(f"Failed to fetch home timeline. Error: {e}")



#interaction with tweets
#v1 old version

"""def favorite(tweet_id) :
    api = get_api()
    client = get_client()
    api.create_favorite(str(tweet_id))
"""

def like(id):
    client = get_client()
    try :
        client.like(id)
        print(f"sucessfull")
    except Exception as e :
        print(f"failed")



# v1 code giving error
"""def retweet2(tweet_id) :
    api = get_api
    try :
        api.retweet(str(tweet_id))
        print(f"sucess")
    except Exception as e  :
        print(f"error")"""

#unfavorite or unlike :
