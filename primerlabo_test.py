import io
import sys
from unittest import mock
from unittest import TestCase

import primerlabo


class PrimerLaboratorioTest(TestCase):

    @mock.patch('primerlabo.input', create=True)
    def test(self, entradas_de_prueba):
        entradas_de_prueba.side_effect = ["2", "3"]
        resultado_test = io.StringIO()
        sys.stdout = resultado_test

        primerlabo.primer_laboratorio()
        resultado_esperado = "x ** y = 8\nlog(x) = 1"
        self.assertEqual(resultado_test.getvalue().strip(), resultado_esperado)
