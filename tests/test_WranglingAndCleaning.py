import unittest
import os
from openCleanlib.WranglingAndCleaning import (corrigirViolacaoDepend, dadosFaltantesLambdaFunc,
retirarDadosFaltantes)

class TestWranglingAndCleaning(unittest.TestCase):
    """
    Uma classe de casos de teste para testar as funções no módulo WranglingAndCleaning.
    """

    def setUp(self):
        """
        Configuração inicial para os testes.
        Cria um DataFrame de teste e salva como CSV para uso nos testes.
        """
        self.caminho = 'test_data.csv'
        import pandas as pd
        df = pd.DataFrame({
            'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
            'age': [25, 30, 35, None, 40],
            'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', None]
        })
        os.makedirs(os.path.join(os.getcwd(), 'source', 'data'), exist_ok=True)
        df.to_csv(os.path.join(os.getcwd(), 'source', 'data', self.caminho), index=False)

    def test_corrigirViolacaoDepend(self):
        """
        Testa a função corrigirViolacaoDepend.
        Verifica se a função corrige a violação de dependência entre as colunas corretamente.
        """
        corrigirViolacaoDepend(self.caminho, 'city', ['name'], ['David'])
        # Esta função imprime os resultados e não retorna, então o teste é visual

    def test_dadosFaltantesLambdaFunc(self):
        """
        Testa a função dadosFaltantesLambdaFunc.
        Verifica se a função retorna corretamente a contagem de dados faltantes na coluna especificada.
        """
        counts = dadosFaltantesLambdaFunc(self.caminho, 'city')
        self.assertEqual(counts['Unknown'], 1)

    def test_retirarDadosFaltantes(self):
        """
        Testa a função retirarDadosFaltantes.
        Verifica se a função remove corretamente os dados faltantes na coluna especificada.
        """
        counts = retirarDadosFaltantes(self.caminho, 'age')
        self.assertNotIn(None, counts.index)

    def tearDown(self):
        """
        Limpeza após os testes.
        Remove o arquivo CSV de teste criado durante a configuração inicial.
        """
        os.remove(os.path.join(os.getcwd(), 'source', 'data', self.caminho))

if __name__ == "__main__":
    unittest.main()
