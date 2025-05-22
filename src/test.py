from bot import profile_image , update_profile_info , post_tweet

filename  = r'C:\Users\punee\Pictures\Screenshots\Screenshot 2025-05-22 104150.png'

profile_image(filename)



#tesing bio 
update_profile_info(
    name='SPARKIE NEWS 24/7',
    bio='Automated AI bot delivering real-time news on X',
    location='India',
    website='https://x.com/Puneet0_0?t=ndXMQZk10S3MGgP2dHx2Pw&s=08'
)


post_tweet('this is the first manuall from backend tweet for testing ')