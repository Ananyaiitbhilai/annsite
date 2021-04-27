"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import index
from django.conf.urls import url,include
from django.conf.urls import url,include
from django.urls import path

from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


app_name='twitter'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.homepg,name='homepg'),
    
    path('ananyapg',index.ananyapg, name='ananyapg'),
    path('vaibhavpg',index.vaibhavpg, name='vaibhavpg'),
    path('pravinpg',index.pravinpg, name='pravinpg'),
    path('buzzinga',index.buzzinga, name='buzzinga'),
    path('party',index.party, name='party'),
    path('signupforms',index.signupforms, name='signupforms'),
    path('team',index.team, name='team'),
    path('tictac',index.tictac, name='tictac'),
    path('blogwrite',index.blogwrite, name='blogwrite'),
    path('after',index.after, name='after'),
    path('tileslide',index.tileslide, name='tileslide'),
    path('services',index.services, name='services'),
    path('loginform',index.loginform, name='loginform'),
    path('games',index.games, name='games'),
    path('contact',index.contact, name='contact'),
    path('quiz',index.quiz, name='quiz'),
    path('community',index.community, name='community'),
    path('covidquiz',index.covidquiz, name='covidquiz'),
    path('cause',index.cause, name='cause'),
    path('social',index.social, name='social'),
    path('neon',index.neon, name='neon'),
    path('Flappybird',index.Flappybird, name='Flappybird'),
    path('covidquizt',index.covidquizt, name='covidquizt'),
    path('err404',index.err404, name='err404'),
    path('logout',index.logout, name='logout'),
    path('logintile',index.logintile, name='logintile'),
    path('pythontweet',index.pythontweet, name='pythontweet'),
    path('twitter_home',index.twitter_home, name='twitter_home'),
    
    url(r'^external', index.external),
    url(r'',include('twitter.urls', namespace='twitter')),
  
    
    


    
    
    
    
    
]

