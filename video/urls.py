from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('videos/<int:vid>', views.videos, name='videos'),
    path('videos1/<int:vid>', views.getVideos, name='videos1'),
    path('profile/', views.getProfile, name='profile'),
    path('userprofile/', views.setProfile, name='userprofile'),
    path('mychannel/', views.myChannel, name='mychannel'),
    path('createchannel/', views.createChannel, name='createchannel'),
    path('channel/<int:cid>', views.getChannel, name='channel'),
    path('showChannel/<name>', views.showChannel, name='showChannel'),
    path('login/', views.getLogin, name='login'),
    path('register/', views.getRegister, name='register'),
    path('logout/', views.getLogout, name='logout'),
    path('upload/', views.setUpload, name='upload'),
    path('subscribe/', views.setSubscribe, name='subscribe')
]