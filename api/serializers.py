from rest_framework import serializers

from api.models import ProblemPrototype, ProblemHead


class ProblemPrototypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemPrototype
        fields = ['id', 'name']


class ProblemHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemHead
        fields = ['id', 'problem']
