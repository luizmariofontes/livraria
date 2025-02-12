from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from core.models.avaliacao import Avaliacao
from core.serializers.avaliacao import AvaliacaoSerializer

class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    @action(detail=False, methods=['get'])
    def notas_altas(self, request):
        avaliacoes = Avaliacao.objects.filter(nota__gt=4)  
        serializer = self.get_serializer(avaliacoes, many=True)
        return Response(serializer.data)