# YouTube Telegram Watcher

A simple Python script that checks for new videos uploaded to specified YouTube channels and sends notifications through a Telegram bot. Made to keep informed about the latest content from specified channels in a convenient and timely manner.

## Features

- Monitors specified YouTube channels for new video uploads.
- Sends notifications to a Telegram group or chat through a dedicated bot.
- Option to pin messages in the group for easy access to the latest videos.


## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/GentleClash/yt-tg-watcher.git
   cd YouTube-Telegram-Notifier
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Configuration:**
   - Configure the channels you want to monitor in the `configurations_.py` file.

4. **Run the Script:**
   ```bash
   python bot.py
   ```

## Configuration

- **Telegram Bot Token (`TG_TOKEN`):** Your Telegram bot token.
- **Chat ID (`CHANNEL_ID`):** The ID of the Telegram group or chat where notifications will be sent.
- **Message Thread ID:** The ID of topic in the group where notifications will be sent, None otherwise.
- **YouTube API Key (`GOOGLE_API`):** Your YouTube Data API key.
- **YouTube Channel IDs (`YOUTUBE_CHANNEL_ID_LIST`):** List of YouTube channel IDs to monitor. DO NOT ENTER YOUTUBE USERHANDLE, REFER TO SECTIONS BELOW TO KNOW HOW TO OBTAIN CHANNEL ID.

## Customization

- **Notification Pinning (`PIN_MESSAGE`):** Set to `True` if you want to pin notifications in the Telegram group, `False` otherwise.
- **Sleep Time (`SLEEP_TIME`):** Time interval (in seconds) between consecutive API calls. Adjust based on your API usage limits.

## Obtaining the Google API Key

To use the YouTube Data API and get notifications for new videos, you'll need to set up a Google API Key. Follow these steps to obtain your API key:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).

2. In the navigation bar, click "Select a project" and then click "New project" to create a new project.

3. Once your project is created, click on the sidebar, navigate to "APIs & Services," and then click on "Credentials."

4. Click on the "+ Create Credentials" button, then choose "API key," and copy the generated API key.

5. Important Step: Go to "Enabled APIs and Services" on the sidebar and click on "+ Enabled APIs and Services" in the navigation bar.

6. Search for "YouTube Data API v3" and select the first result.

7. Click the "Enable" button to enable the YouTube Data API for your project.

Now you have successfully obtained your Google API Key, and the YouTube Data API is enabled for your project. You can use this key in the configuration of your YouTube Telegram Notifier script.

## Obtaining YouTube Channel ID from Channel Username

To get the YouTube Channel ID from a channel username, you can use the following steps:

1. Go to [StreamWeasels YouTube Channel ID and User ID Converter](https://www.streamweasels.com/tools/youtube-channel-id-and-user-id-convertor/).

2. Scroll down to find the field where you can enter the channel username (handle). Enter the channel username without the '@' symbol.

3. Click on the channel URL that appears below the field to verify that the correct channel is selected.

**Note:**
- Ensure you enter the channel username (handle) correctly.
- Do not include the '@' symbol in the field.
- If the provided website stops working, you can search for free alternatives to obtain the YouTube Channel ID from the channel handle.

## Warning: Updating YouTube Channel List in `configurations_.py`

**Important Note:**
- The only supported change in the `YOUTUBE_CHANNEL_LIST` field in `configurations_.py` is adding more channels.
- If you need to make changes to an already present channel or remove a channel, manual adjustments in the `result_.json` file are required.
- In case you are replacing or removing a channel, find the channel ID from the `channels` list in `result_.json` and make the necessary modifications.
- If you are replacing a channel, ensure to replace the corresponding channel ID. Changing the video ID might not be necessary.
  
**Example:**

1. **Adding Channels (You need not to do any manual change except for configurations_.py):**
   - Add channels to `YOUTUBE_CHANNEL_LIST` in `configurations_.py`.
   - Run the script to initialize the structure.

2. **Manual Modification(For removing a channel or modifying the already present one):**
   - Open `result_.json` and manually add the necessary details for each channel:
   - Before: 

     ```json
     {
       "structured": true,
       "total_channels": 2,
       "channels": [
         {"channel_id": "channel_id_1", "latest_video_id": null},
         {"channel_id": "channel_id_2", "latest_video_id": null}
       ]
     }
     ```

   - After:

     ```json
     {
       "structured": true,
       "total_channels": 1,
       "channels": [
         {"channel_id": "changed_channel_id_1", "latest_video_id": null}
       ]
     }
     ```

3. **Updating Channels:**
   - If you need to change or remove a channel:
     - Find the channel ID in `result_.json`.
     - Make the necessary changes or remove the channel.
     - If replacing a channel, replace the channel ID.

4. **Reflecting Changes in `configurations_.py`:**
   - Update `YOUTUBE_CHANNEL_LIST` in `configurations_.py` to match the modified channels.

**Advice:**
- It is recommended to monitor only one channel at a time for not exceeding free quota.

## Contributors

- [Ayush](https://github.com/GentleClash) : [Connect to me on telegram](https://t.me/Donutkno) 

## License

This project is licensed under the [MIT License](LICENSE).

