from rest_framework import serializers

from . import models

class projetoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.projeto
        fields = [
            "last_updated",
            "created",
        ]
