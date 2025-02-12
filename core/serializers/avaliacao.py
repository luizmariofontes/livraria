from rest_framework.serializers import ModelSerializer
from core.models.avaliacao import Avaliacao

class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'