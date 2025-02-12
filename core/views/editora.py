from rest_framework.viewsets import ModelViewSet

from core.models import Editora
from core.serializers import EditoraSerializer


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter



class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ["email"]
    search_fields = ["nome"]
    ordering_fields = ["nome", "email", "cidade", "site"]
    ordering = ["nome"]