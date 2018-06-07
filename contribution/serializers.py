from rest_framework import serializers
from contribution.models import Language, Data


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'code')


class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('id', 'user', 'language', 'text', 'file')
