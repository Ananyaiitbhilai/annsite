from django.conf.urls import url,include
from django.urls import path

from . import views

app_name='twitter'

urlpatterns = [
    path('twitter_index',views.twitter_index, name='twitter_index'),
    url(r'^$', views.twitter_index,name='index'),
    url(r'^new/', views.form_data, name='new'),
]