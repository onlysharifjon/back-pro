from .models import UserApplicationpss
from rest_framework.serializers import ModelSerializer

class ApplicationSerializer(ModelSerializer):
    class Meta:
        model = UserApplicationpss
        fields = '__all__'