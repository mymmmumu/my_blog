# -*- coding: utf-8 -*-
from django.conf.urls import   url
from django.contrib import admin
from article.views import detail,home,test
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^(?P<my_args>\d+)/$', detail, name='detail'),
    url(r'^test/$', test),
]
