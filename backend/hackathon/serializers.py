

from .models import Hackathon
from backend.user import serializers


class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = '__all__'
