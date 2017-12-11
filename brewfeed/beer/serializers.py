from rest_framework import serializers
from .models import FeedItem

class FeedItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeedItem
        # fields = '__all__'
        fields = ('title', 'url', 'style', 'description')