from rest_framework.viewsets import ModelViewSet

from core.models import Autor
from core.serializers import AutorSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter




class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    search_fields = ["nome"]
    ordering_fields = ["nome", "email"]
    ordering = ["nome"]
