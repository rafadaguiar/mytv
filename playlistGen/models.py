from string import Template
# from django.db import models
import urllib2
import json


class PlaylistFilter(object):
    """
        Filter the user subscriptions (channels) and return the playlist object
        with the selected videos.
    """
    def __init__(self, arg):
        super(PlaylistFilter, self).__init__()
        self.arg = arg

    # Receive a channel and return its latest video available.
    def simple_filter(self, channel_id):
        # url = Template("https://www.googleapis.com/youtube/v3/subscriptions?part=$part&channelId=$channel_id&key=$API_KEY")
        # dict idea (API +BASE_URL) = "https://www.googleapis.com/youtube/v3/"
        url = Template("https://www.googleapis.com/youtube/v3/search?part=$part&channelId=$channel_id&order=$order&key=$API_KEY")
        url = url.substitute(part='id',
                             channel_id=channel_id,
                             order='date',
                             API_KEY='AIzaSyC1YiEb8X9des67iS2XUvN-vDZImtCtb4o')
        # Response is a json
        response = json.loads(urllib2.urlopen(url).read())
        return response['items'][0]['id']['videoId']
