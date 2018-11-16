from django.urls import path, include,re_path
from . import views

#namespacing urls

app_name = 'music'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    #/song/<albumm_id>/
    re_path(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),

    #song/album/add/
    re_path(r'^album/add/$',views.AlbumCreate.as_view(), name='album-add'),

    # song/album/2/
    re_path(r'^album/(?P<pk>[0-9]+)/$', views.AlbumCreate.as_view(), name='album-update'),

    # song/album/2/delete/
    re_path(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

]
