import urllib.request, json, asyncio, time
from configurations_ import Config
from youtube_updates import YouTubeUpdater
from telegram import Bot

async def send_and_pin_message(token, chat_id, text, message_thread_id, pin_message):
    bot = Bot(token)
    if message_thread_id:
        message = await bot.send_message(chat_id=chat_id, text=text, reply_to_message_id=message_thread_id, disable_web_page_preview=False)
    else:
        message = await bot.send_message(chat_id=chat_id, text=text, disable_web_page_preview=False)

    if pin_message:
        await bot.pin_chat_message(chat_id=chat_id, message_id=message.message_id)

async def main():
    while True:
        youtube_updater = YouTubeUpdater()
        new_videos = youtube_updater.get_latest_video()

        for video_url in new_videos:
            await send_and_pin_message(Config.TELEGRAM_BOT_TOKEN, Config.CHAT_ID, video_url, Config.MESSAGE_THREAD_ID, Config.PIN_MESSAGE)

        time.sleep(Config.SLEEP_TIME)

if __name__ == "__main__":
    asyncio.run(main())