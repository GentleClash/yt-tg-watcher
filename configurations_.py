from dotenv import load_dotenv
import os

load_dotenv()

TG_TOKEN = os.getenv("TG_TOKEN") or None
CHANNEL_ID = os.getenv("CHANNEL_ID") or None
THREAD_ID = os.getenv("THREAD_ID") or None
GOOGLE_API = os.getenv("GOOGLE_API") or None


class Config:
    
    TELEGRAM_BOT_TOKEN = TG_TOKEN       # your telegram bot token
    CHAT_ID = CHANNEL_ID                # id of chat where bot will send message
    MESSAGE_THREAD_ID = THREAD_ID       # id of the thread group
                                        # Assign None if not available

    
    GOOGLE_API_KEY = GOOGLE_API         # your Google API key


    YOUTUBE_CHANNEL_LIST = []           # Enter the list of channels 
                                        # dont use large number of channels as it may exceed free quota
                                        # example = ["@PewDiePie", "@MrBeast"]


if __name__=="__main__":
    print("Nothing here.")
