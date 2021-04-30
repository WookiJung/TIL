from rest_framework import serializers
from .models import Artist, Music

class MusicSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length= 100)

    class Meta:
        model = Music
        fields = '__all__'
        read_only_fields = ('artist',)

class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('pk', 'name',)
        read_only_fields=fields


class ArtistSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length = 100)
    music_set = MusicSerializer(many=True, read_only=True)
    music_count = serializers.IntegerField(source='music_set.count', read_only=True)
    class Meta:
        model = Artist
        fields = '__all__'
        # read_only_fields = ('music_set', 'music_count',)

class MusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('pk', 'title')
        read_only_fields=fields
