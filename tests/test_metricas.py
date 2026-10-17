import unittest
from src.metricas import contar_aciertos


class TestMetricas(unittest.TestCase):
    def test_cuenta_aciertos(self):
        self.assertEqual(contar_aciertos([1, 0, 1], [1, 1, 1]), 2)

    def test_rechaza_longitudes_distintas(self):
        with self.assertRaises(ValueError):
            contar_aciertos([1], [1, 0])


if __name__ == "__main__":
    unittest.main()
