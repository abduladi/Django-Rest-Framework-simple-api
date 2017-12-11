# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from . import models, serializers

# Create your views here.

class FeedItemList(generics.ListAPIView):
    serializer_class = serializers.FeedItemSerializer
    query_set = models.FeedItem.objects.all()
