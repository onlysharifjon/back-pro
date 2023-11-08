from .models import UserApplicationpss
from rest_framework.serializers import ModelSerializer, Serializer


class ApplicationSerializer(ModelSerializer):
    class Meta:
        model = UserApplicationpss
        fields = '__all__'


class Sort_srl(ModelSerializer):
    class Meta:
        model = UserApplicationpss
        fields = ("password", )




