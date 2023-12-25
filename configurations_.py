from dotenv import load_dotenv
import os

load_dotenv()

TG_TOKEN = os.getenv("TG_TOKEN") or None
CHANNEL_ID = os.getenv("CHANNEL_ID") or None
THREAD_ID = os.getenv("THREAD_ID") or None
GOOGLE_API = os.getenv("GOOGLE_API") or None
YOUTUBE_CHANNEL_ID_LIST = os.getenv("YOUTUBE_CHANNEL_ID_LIST") or None


class Config:
    
    TELEGRAM_BOT_TOKEN = TG_TOKEN       # your telegram bot token
    CHAT_ID = CHANNEL_ID                # id of chat where bot will send message
    PIN_MESSAGE = True                  # Whether to pin the messages or not
    MESSAGE_THREAD_ID = None            # id of the group topic
                                        # Assign None if not available
    
    
    GOOGLE_API_KEY = GOOGLE_API         # your Google API key


    YOUTUBE_CHANNEL_LIST = [YOUTUBE_CHANNEL_ID_LIST]# DO NOT ENTER CHANNEL USERNAME
                                        # Refer to readme to know how to find channel id
                                        # Enter the list of channels ids
                                        # dont use large number of channels as it may exceed free quota
                                        
    SLEEP_TIME = 900  # How much time to wait in seconds before making API call?
                      # 900 seconds ( 15 minutes ) wait time is perfect for free quota per day considering only 1 channel

if __name__=="__main__":
    config = Config()
    print("Telegram bot token : ", config.TELEGRAM_BOT_TOKEN)
    print("Chat ID : ", config.CHAT_ID)
    print("Google API : ", config.GOOGLE_API_KEY)
    print("Total youtube channels : ", len(config.YOUTUBE_CHANNEL_LIST))
