# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin

from inventory import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
]
