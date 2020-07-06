from rest_framework import viewsets, permissions

from . import serializers
from . import models


class projetoViewSet(viewsets.ModelViewSet):
    """ViewSet for the carrinho class"""

    queryset = models.projeto.objects.all()
    serializer_class = serializers.projetoSerializer
    permission_classes = [permissions.IsAuthenticated]
