from configurations_ import Config
import urllib.request, json

class YouTubeUpdater:
    def __init__(self):
        self.api_key = Config.GOOGLE_API_KEY
        self.channel_list = Config.YOUTUBE_CHANNEL_LIST
        self.new_videos = []
        self.json_file = 'result_.json'

        self.initialize_structure()
    

    def initialize_structure(self):
        """
        Checks for any changes in the channel list or if the script is being run for the first time.
        Structures the result_.json accordingly.
        """
        try:
            with open(self.json_file, 'r') as json_file:
                data = json.load(json_file)
                
                if not data.get('structured') or data.get('total_channels') != len(self.channel_list):
                    data['structured'] = True
                    data['total_channels'] = len(self.channel_list)
                    
                    for channel_id in self.channel_list:
                        if not any(channel['channel_id'] == channel_id for channel in data['channels']):
                            data['channels'].append({
                                'channel_id': channel_id,
                                'latest_video_id': None
                            })

                    with open(self.json_file, 'w') as updated_json_file:
                        json.dump(data, updated_json_file, indent=2)
        except FileNotFoundError:
            data = {
                'structured': False,
                'total_channels': 0,
                'channels': []
            }

            for channel_id in self.channel_list:
                data['channels'].append({
                    'channel_id': channel_id,
                    'latest_video_id': None
                })

            with open(self.json_file, 'w') as new_json_file:
                json.dump(data, new_json_file, indent=2)
    def get_latest_video(self) -> list[str]:
        base_yt_url = 'https://www.youtube.com/watch?v='
        base_url = 'https://www.googleapis.com/youtube/v3/search?'
        self.new_videos = []

        for channel_id in self.channel_list:
            url = f'{base_url}key={self.api_key}&channelId={channel_id}&part=id&order=date&maxResults=1'
            with urllib.request.urlopen(url) as response:
                resp = json.load(response)
                try:
                    vid_id = resp['items'][0]['id']['videoId']
                except:
                    vid_id = None

            with open('result_.json', 'r') as json_file:
                data = json.load(json_file)
                channel_entry = next((channel for channel in data['channels'] if channel['channel_id'] == channel_id), None)
                if channel_entry:
                    if channel_entry['latest_video_id'] != vid_id:
                        channel_entry['latest_video_id'] = vid_id
                        with open('result_.json', 'w') as json_file:
                            json.dump(data, json_file, indent=2)

                        video_url = f'{base_yt_url}{vid_id}'
                        self.new_videos.append(video_url)

        return self.new_videos

if __name__=="__main__":
    checking = YouTubeUpdater()
    print(checking.get_latest_video())
    #Go check if the result_.json has changed