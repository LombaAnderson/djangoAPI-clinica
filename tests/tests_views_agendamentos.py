from django.test import TestCase

from tests_views_agendamentos import Agendamentos


class AgendamentoTestCase(TestCase):

    def setUp(self):
        Agendamentos.objects.create(
            nome="Agendamento"
        )


def test_retorno_str(self):
    p1 = Agendamentos.objects.get(nome='Agendamento')
    self.assertEquals(p1.__str__(), 'Agendamento')
