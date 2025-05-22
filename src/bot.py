import sys
import os

# Add parent folder to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now import the function
from twitter_python import get_api



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
def post_tweet(text) :
    api = get_api()
    try : 
        api.update_status(status=text)
        print(f"sucessfull")
    except Exception as e :
        print(f"failed")

def post_tweet(text) :
    api = get_api()
    try : 
        api.Client.create_tweet(status=text)
        print(f"sucessfull")
    except Exception as e :
        print(f"failed")
