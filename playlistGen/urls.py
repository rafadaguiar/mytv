from django.conf.urls import url
from playlistGen import views


urlpatterns = [
    url(r'^$', views.index, name='index')
]
