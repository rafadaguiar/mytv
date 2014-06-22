# from django.db import models
from youtubeOauth.models import get_authenticated_service
import urllib
import urllib2
import json
from string import Template


class Playlist(object):

    """
        Filter the user subscriptions (channels) and return the playlist object
        with the selected videos.
    """

    def __init__(self):
        self.user_channels = YoutubeRequest().proto_get_user_channels()

    # Receive a channel and return its latest video available.
    def latest(self):
        video_ids = []
        for channelId in self.user_channels.values():
            param = urllib.urlencode(
                dict(
                    part='id',
                    channelId=channelId,
                    order='date',
                    key='AIzaSyDxwFXVDTlO4JXkX0_NS6HwX28DikeEUyQ'
                )
            )
            url = "https://www.googleapis.com/youtube/v3/search?%s" % param
            response = json.loads(urllib2.urlopen(url).read())

            for item in response['items']:
                if item['id']['kind'] == 'youtube#video':
                    video_ids.append(item['id']['videoId'])
                    break
        return video_ids


class YoutubeRequest(object):

    def __init__(self):
        pass
        # self.youtube = get_authenticated_service()

    def get_user_channels(self):
        """ This method calls the youtube.subscriptions.list method to
            list all the channels that an user has subscribed to.
        """

        request = self.youtube.subscriptions().list(
            part='snippet',
            mine=True,
            order='alphabetical'
        )
        subscriptions = []
        while request:
            response = request.execute()
            subscriptions.append(response)
            request = self.youtube.subscriptions().list_next(request, response)

        channels = {}
        for subscription in subscriptions:
            for channel in subscription['items']:
                channel_title = channel['snippet']['title']
                channel_id = channel['snippet']['resourceId']['channelId']
                channels[channel_title] = channel_id

        return channels

    def proto_get_user_channels(self):
        return {
            u'Sauder School of Business at UBC': u'UC1lL9NvIkoqnE931f9j3mFw',
            u'Vevo': u'UC2pmfLm7iq6Ov1UwYrWYkZA',
            u'UBC': u'UC327M9im1ba32Pv32LR118w',
            u'serie3porcento': u'UCvuCK5C6XLduyJHw2zR37Fw',
            u'theartofphotography': u'UC7T8roVtC_3afWKTOGtLlBA',
            u'GoPro': u'UCqhnX4jA0A5paNd1v-zEysw',
            u'Adorama': u'UC8Pksdbj37CdE00kmE7Z1dw',
            u'DigitalRev TV': u'UCuw8B6Uv0cMWtV5vbNpeH_A',
            u'The Tonight Show Starring Jimmy Fallon': u'UC8-Th83bH_thdKZDJCrn88g',
            u'colinfurze': u'UCp68_FLety0O-n9QU6phsgw',
            u'Canon Australia': u'UCDUWA-cTYMcuURVGS2F4bJw',
            u'NewsyTech': u'UCB0QyTJ3lQUDmE0yZqiuQuA',
            u'Porta dos Fundos': u'UCEWHPFNilsT0IfQfutVzsag'
        }
