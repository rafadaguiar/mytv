from django.shortcuts import render
from playlistGen.models import Playlist


def index(request):
    pf = Playlist()
    videos = pf.latest()
    context = {'url-list': ['www'],
               'videos': videos
               }
    return render(request, 'playlistGen/index.html', context)


# try:
#             channels = get_user_channels(self.youtube)
#         except HttpError, e:
#             return "An HTTP error %d occurred:\n%s" % (
#                 e.resp.status, e.content
#             )
#         else:
#             return channels