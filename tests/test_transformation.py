import unittest
import os
from openCleanlib.transformation import (selecionarColunas, inserirColuna, inserirLinhas,
atualizarNomeColuna, filtrarValorPorColuna,moverColuna, moverLinha, ordenarValorDescendenteColuna)


class TestTransformation(unittest.TestCase):
    def setUp(self):
        self.caminho = 'test_data.csv'
        # Crie um DataFrame de teste e salve como CSV para uso nos testes
        import pandas as pd
        df = pd.DataFrame({
            'name': ['Alice', 'Bob', 'Charlie'],
            'age': [25, 30, 35],
            'city': ['New York', 'Los Angeles', 'Chicago']
        })
        os.makedirs(os.path.join(os.getcwd(), 'source', 'data'), exist_ok=True)
        df.to_csv(os.path.join(os.getcwd(), 'source', 'data', self.caminho), index=False)

    def test_selecionarColunas(self):
        """
        Testa a função selecionarColunas.
        """
        selected = selecionarColunas(self.caminho, 'name', 'age')
        self.assertEqual(list(selected.columns), ['name', 'age'])

    def test_inserirColuna(self):
        """
        Testa a função inserirColuna.
        """
        new_col = inserirColuna(self.caminho, 'salary', 3, 50000)
        self.assertIn('salary', new_col.columns)

    def test_inserirLinhas(self):
        """
        Testa a função inserirLinhas.
        """
        new_row = inserirLinhas(self.caminho, 1, 'David', 40, 'Houston')
        self.assertEqual(new_row.iloc[1]['name'], 'David')

    def test_atualizarNomeColuna(self):
        """
        Testa a função atualizarNomeColuna.
        """
        updated = atualizarNomeColuna(self.caminho, 'name')
        self.assertEqual(updated.iloc[0]['name'], 'Alice')

    def test_filtrarValorPorColuna(self):
        """
        Testa a função filtrarValorPorColuna.
        """
        filtered = filtrarValorPorColuna(self.caminho, 'city', 'New York')
        self.assertEqual(filtered.iloc[0]['city'], 'New York')

    def test_moverColuna(self):
        """
        Testa a função moverColuna.
        """
        moved_col = moverColuna(self.caminho, 'city', 0)
        self.assertEqual(moved_col.columns[0], 'city')

    def test_moverLinha(self):
        """
        Testa a função moverLinha.
        """
        moved_row = moverLinha(self.caminho, 0, 2)
        self.assertEqual(moved_row.iloc[2]['name'], 'Alice')

    def test_ordenarValorDescendenteColuna(self):
        """
        Testa a função ordenarValorDescendenteColuna.
        """
        sorted_df = ordenarValorDescendenteColuna(self.caminho, 'age')
        self.assertEqual(sorted_df.iloc[0]['age'], 35)

    def tearDown(self):
        os.remove(os.path.join(os.getcwd(), 'source', 'data', self.caminho))

if __name__ == "__main__":
    unittest.main()
