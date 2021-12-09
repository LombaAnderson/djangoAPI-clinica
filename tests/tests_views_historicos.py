from django.test import TestCase

from tests_views_historicos import Historicos


class HistoricoTestCase(TestCase):

    def setUp(self):
        Historicos.objects.create(
            nome="Historico"
        )


def test_retorno_str(self):
    p1 = Historicos.objects.get(nome='Historico')
    self.assertEquals(p1.__str__(), 'Historico')
