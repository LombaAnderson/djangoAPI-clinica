from rest_framework import serializers, viewsets

from agendamentos.models import Agendamentos
from agendamentos.api.serializers import AgendamentosSerializer


class AgendamentosViewSet(viewsets.ModelViewSet):
    queryset = Agendamentos.objects.all().order_by('data_hora')
    serializer_class = AgendamentosSerializer
