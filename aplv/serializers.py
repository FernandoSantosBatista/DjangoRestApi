from rest_framework import serializers
from aplv.models import Aplv

class AplvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aplv
        fields = ('id', 'name', 'district', 'city', 'email')