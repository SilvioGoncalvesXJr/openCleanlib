# tests/test_profiling.py

import unittest
import os
from openCleanlib.profiling import datasetStatistics, maxMinColuna, dataTypes

class TestProfiling(unittest.TestCase):
    def setUp(self):
        self.caminho = 'test_data.csv'
        # Crie um DataFrame de teste e salve como CSV para uso nos testes
        import pandas as pd
        df = pd.DataFrame({
            'name': ['Alice', 'Bob', 'Charlie'],
            'age': [25, 30, 35]
        })
        os.makedirs(os.path.join(os.getcwd(), 'source', 'data'), exist_ok=True)
        df.to_csv(os.path.join(os.getcwd(), 'source', 'data', self.caminho), index=False)

    def test_datasetStatistics(self):
        stats = datasetStatistics(self.caminho)
        self.assertIsNotNone(stats)

    def test_maxMinColuna(self):
        minmax = maxMinColuna(self.caminho, 'age')
        self.assertEqual(minmax['min'], 25)
        self.assertEqual(minmax['max'], 35)

    def test_dataTypes(self):
        types = dataTypes(self.caminho)
        self.assertIn('age', types)
        self.assertEqual(types['age'], 'int')

    def tearDown(self):
        os.remove(os.path.join(os.getcwd(), 'source', 'data', self.caminho))

if __name__ == "__main__":
    unittest.main()
