from django.shortcuts import render
from playlistGen.models import PlaylistFilter


def index(request):
    pf = PlaylistFilter('')
    videoids = [pf.simple_filter('UCEWHPFNilsT0IfQfutVzsag'),
                pf.simple_filter('UCB0QyTJ3lQUDmE0yZqiuQuA')]
    context = {'url-list': ['www'],
               'videoids': videoids
               }
    return render(request, 'sublimevideo/index.html', context)
