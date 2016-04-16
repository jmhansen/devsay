from rest_framework import serializers

from .models import ForvoWord, ForvoPronunciation


class ForvoWordSerializer(serializers.ModelSerializer):

    class Meta:
        model = ForvoWord


class ForvoPronunciationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ForvoPronunciation
