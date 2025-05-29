#this file is contain langchain to generate headline 

#BETA version 1
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import getpass
import os

# Load environment variables from .env file
load_dotenv()



model =  ChatGoogleGenerativeAI(model= "gemini-1.5-flash" ,temperature = 1.0 )
messages = [("system", "you are the cheif head of articles where your jobs is to make simple attractive and eye catching headline form news articles , you have to breakdown articles and then use chain thought that what should be article heading from that and use stragtery for make it more viral and eye catching , if you did you job best you get promotion and you have limit of 280 charaters to make heading . some time user or client by mistake give you unnessary data with articles you can able to serpate useless data and use rest for heading"),
("human" , "i love programing")
]
ai_msg = model.invoke(messages)

print(ai_msg.content)