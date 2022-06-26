# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 13:28:52 2022

@author: niyi3
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]