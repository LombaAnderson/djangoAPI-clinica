from django.test import TestCase

from pacientes import Pacientes


class PacientesTestCase(TestCase):

    def setUp(self):
        Pacientes.objects.create(
            nome="Paciente",
            idade=41
        )


def test_retorno_str(self):
    p1 = Pacientes.objects.get(nome='Paciente')
    self.assertEquals(p1.__str__(), 'Paciente')
