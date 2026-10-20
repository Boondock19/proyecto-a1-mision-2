import unittest
from src.metricas import contar_aciertos
from src.metricas import precision

class TestMetricas(unittest.TestCase):
    def test_cuenta_aciertos(self):
        self.assertEqual(contar_aciertos([1, 0, 1], [1, 1, 1]), 2)

    def test_rechaza_longitudes_distintas(self):
        with self.assertRaises(ValueError):
            contar_aciertos([1], [1, 0])

    def test_cuenta_precision(self):
        
        self.assertEqual(precision([1, 0, 1], [1, 1, 1]), 2 / 3)
        self.assertEqual(precision([], []), 0.0)

    def test_contar_aciertos_no_iguales(self):
        self.assertNotEqual(
            contar_aciertos([0, 1, 3], [0, 2, 2]), 2
        )


if __name__ == "__main__":
    unittest.main()
