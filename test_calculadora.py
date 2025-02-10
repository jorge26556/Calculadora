import unittest
import tkinter as tk
from unittest.mock import patch
# Asegúrate de importar el nombre del archivo correcto:
# Si tu calculadora está en "calculadora.py", usa:
from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.calc = Calculadora(self.root)

    def tearDown(self):
        self.root.destroy()

    def _click_sequence(self, sequence):
        for char in sequence:
            self.calc.on_button_click(char)

    # --------------
    # TEST BÁSICOS
    # --------------

    def test_suma_basica(self):
        """Prueba de suma simple: 2 + 3 = 5"""
        self._click_sequence("2+3=")
        self.assertEqual(self.calc.input_text.get(), "5")

    def test_resta_basica(self):
        """Prueba de resta simple: 9 - 4 = 5"""
        self._click_sequence("9-4=")
        self.assertEqual(self.calc.input_text.get(), "5")

    def test_multiplicacion_basica(self):
        """Prueba de multiplicación: 3 * 4 = 12"""
        self._click_sequence("3*4=")
        self.assertEqual(self.calc.input_text.get(), "12")

    def test_division_basica(self):
        """
        Prueba de división: 8 / 2 = 4
        La calculadora devuelve '4.0', por lo que usamos float.
        """
        self._click_sequence("8/2=")
        self.assertAlmostEqual(float(self.calc.input_text.get()), 4.0, places=6)

    def test_division_por_cero(self):
        """Prueba de división entre cero: 8 / 0 = Error"""
        self._click_sequence("8/0=")
        self.assertEqual(self.calc.input_text.get(), "Error")

    # --------------------
    # TEST BOTONES ESPECIALES
    # --------------------

    def test_boton_C(self):
        """Prueba del botón C (Clear): limpia la pantalla."""
        self._click_sequence("12+3")
        self.calc.on_button_click('C')
        self.assertEqual(self.calc.input_text.get(), "")

    def test_boton_flecha(self):
        """Prueba del botón ←: borra el último dígito."""
        self._click_sequence("12+3")
        self.calc.on_button_click('←')
        self.assertEqual(self.calc.input_text.get(), "12+")

    @patch('calculadora.Calculadora.exit_app')
    def test_exit_button(self, mock_exit):
        """
        Prueba que el botón EXIT invoque exit_app.
        Se parchea usando el nombre del módulo: 'calculadora.Calculadora.exit_app'.
        """
        self.calc.on_button_click('EXIT')
        mock_exit.assert_called_once()

    # --------------
    # TEST PORCENTAJE
    # --------------

    def test_porcentaje_solo(self):
        """Prueba ingresar sólo 20% = 0.2"""
        self._click_sequence("20%=")
        self.assertEqual(self.calc.input_text.get(), "0.2")

    def test_suma_con_porcentaje(self):
        """Prueba 100 + 10% = 110"""
        self._click_sequence("100+10%=")
        # Convertimos a float, comparamos con 110
        self.assertAlmostEqual(float(self.calc.input_text.get()), 110.0)

    def test_resta_con_porcentaje(self):
        """Prueba 40 - 20% = 32"""
        self._click_sequence("40-20%=")
        self.assertAlmostEqual(float(self.calc.input_text.get()), 32.0)

    def test_multiplicacion_con_porcentaje(self):
        """Prueba 90 * 6% = 5.4"""
        self._click_sequence("90*6%=")
        self.assertAlmostEqual(float(self.calc.input_text.get()), 5.4, places=6)

    def test_division_con_porcentaje(self):
        """Prueba 90 / 9% = 1000"""
        self._click_sequence("90/9%=")
        self.assertAlmostEqual(float(self.calc.input_text.get()), 1000, places=6)

    def test_porcentaje_al_principio(self):
        """Prueba de poner porcentaje antes: 20% + 30 = 30.2"""
        self._click_sequence("20%+30=")
        self.assertAlmostEqual(float(self.calc.input_text.get()), 30.2, places=6)


if __name__ == '__main__':
    unittest.main()
