import os
from openclean.data.load import dataset
from openclean.operator.transform.select import select
from openclean.operator.transform.insert import inscol
from openclean.function.eval.base import Const
from openclean.operator.transform.insert import insrow
from openclean.operator.transform.update import update
from openclean.operator.transform.filter import filter
from openclean.function.eval.base import Col
from openclean.operator.transform.move import movecols
from openclean.operator.transform.move import move_rows
from openclean.operator.transform.sort import order_by

def selecionarColunas(caminho, *args, isDataFull=False):
    """
    Seleciona colunas específicas de um conjunto de dados.

    Args:
        caminho (str): O caminho para o arquivo de dados.
        *args (str): Os nomes das colunas a serem selecionadas.
        isDataFull (bool, optional): Indica se deve retornar o conjunto de dados completo ou apenas as primeiras linhas. O padrão é False.

    Returns:
        openclean.data.DataFrame: O conjunto de dados com as colunas selecionadas.
    """
    path_to_file = os.path.join(os.getcwd(), 'source', 'data')
    ds = dataset(os.path.join(path_to_file, caminho))
    colunas = []
    for i in args:
        colunas.append(i)
    selected = select(ds, columns = colunas)
    if isDataFull == True:
        return selected
    else:
        return selected.head()

def inserirColuna(caminho, coluna, posicao, valor, isDataFull=False):
    """
    Insere uma nova coluna em um conjunto de dados.

    Args:
        caminho (str): O caminho para o arquivo de dados.
        coluna (str): O nome da nova coluna a ser inserida.
        posicao (int): A posição em que a nova coluna deve ser inserida.
        valor (Any): O valor constante a ser atribuído a todas as linhas da nova coluna.
        isDataFull (bool, optional): Indica se deve retornar o conjunto de dados completo ou apenas as primeiras linhas. O padrão é False.

    Returns:
        openclean.data.DataFrame: O conjunto de dados com a nova coluna inserida.
    """
    path_to_file = os.path.join(os.getcwd(), 'source', 'data')
    ds = dataset(os.path.join(path_to_file, caminho))
    new_col = inscol(ds, names = [coluna], pos=posicao, values= Const(valor))
    if isDataFull == True:
        return new_col
    else:
        return new_col.head()

def inserirLinhas(caminho, posicao,*args, isDataFull=False):
    """
    Insere novas linhas em um conjunto de dados.

    Args:
        caminho (str): O caminho para o arquivo de dados.
        posicao (int): A posição em que as novas linhas devem ser inseridas.
        *args (list): Os valores das novas linhas a serem inseridas.
        isDataFull (bool, optional): Indica se deve retornar o conjunto de dados completo ou apenas as primeiras linhas. O padrão é False.

    Returns:
        openclean.data.DataFrame: O conjunto de dados com as novas linhas inseridas.
    """
    path_to_file = os.path.join(os.getcwd(), 'source', 'data')
    ds = dataset(os.path.join(path_to_file, caminho))
    valoresLinha = []
    for i in args:
        valoresLinha.append(i)
    new_row = insrow(ds, pos=posicao, values = valoresLinha)
    if isDataFull == True:
        return new_row
    else:
        return new_row.head()

def atualizarNomeColuna(caminho,coluna, isDataFull=False):
    """
    Atualiza o nome de uma coluna em um conjunto de dados.

    Args:
        caminho (str): O caminho para o arquivo de dados.
        coluna (str): O nome da coluna a ser atualizada.
        isDataFull (bool, optional): Indica se deve retornar o conjunto de dados completo ou apenas as primeiras linhas. O padrão é False.

    Returns:
        openclean.data.DataFrame: O conjunto de dados com o nome da coluna atualizado.
    """
    path_to_file = os.path.join(os.getcwd(), 'source', 'data')
    ds = dataset(os.path.join(path_to_file, caminho))
    title_case = update(ds, columns = coluna, func = str.title)
    if isDataFull == True:
        return title_case
    else:
        return title_case.head()

def filtrarValorPorColuna(caminho, coluna, valor, isDataFull=False):
    """
    Filtra um conjunto de dados com base em um valor específico em uma coluna.

    Args:
        caminho (str): O caminho para o arquivo de dados.
        coluna (str): O nome da coluna a ser filtrada.
        valor (Any): O valor a ser filtrado.
        isDataFull (bool, optional): Indica se deve retornar o conjunto de dados completo ou apenas as primeiras linhas. O padrão é False.

    Returns:
        openclean.data.DataFrame: O conjunto de dados filtrado.
    """
    path_to_file = os.path.join(os.getcwd(), 'source', 'data')
    ds = dataset(os.path.join(path_to_file, caminho))
    filtered = filter(ds, predicate = Col(coluna)==valor)
    if isDataFull == True:
        return filtered
    else:
        return filtered.head()

def moverColuna(caminho, coluna, posicao, isDataFull=False):
    """
    Move uma coluna para uma nova posição em um conjunto de dados.

    Args:
        caminho (str): O caminho para o arquivo de dados.
        coluna (str): O nome da coluna a ser movida.
        posicao (int): A nova posição da coluna.
        isDataFull (bool, optional): Indica se deve retornar o conjunto de dados completo ou apenas as primeiras linhas. O padrão é False.

    Returns:
        openclean.data.DataFrame: O conjunto de dados com a coluna movida.
    """
    path_to_file = os.path.join(os.getcwd(), 'source', 'data')
    ds = dataset(os.path.join(path_to_file,caminho))
    moved_col = movecols(ds, coluna,posicao)
    if isDataFull == True:
        return moved_col
    else:
        return moved_col.head()

def moverLinha(caminho, posLinha, novaPosicao, isDataFull=False):
    """
    Move uma linha para uma nova posição em um conjunto de dados.

    Args:
        caminho (str): O caminho para o arquivo de dados.
        posLinha (int): A posição da linha a ser movida.
        novaPosicao (int): A nova posição da linha.
        isDataFull (bool, optional): Indica se deve retornar o conjunto de dados completo ou apenas as primeiras linhas. O padrão é False.

    Returns:
        openclean.data.DataFrame: O conjunto de dados com a linha movida.
    """
    path_to_file = os.path.join(os.getcwd(), 'source', 'data')
    ds = dataset(os.path.join(path_to_file,caminho))
    moved_row = move_rows(ds, posLinha, novaPosicao)
    if isDataFull == True:
        return moved_row
    else:
        return moved_row.head()

def ordenarValorDescendenteColuna(caminho, coluna, isDataFull=False):
    """
    Ordena um conjunto de dados em ordem descendente com base em uma coluna.

    Args:
        caminho (str): O caminho para o arquivo de dados.
        coluna (str): O nome da coluna a ser ordenada.
        isDataFull (bool, optional): Indica se deve retornar o conjunto de dados completo ou apenas as primeiras linhas. O padrão é False.

    Returns:
        openclean.data.DataFrame: O conjunto de dados ordenado em ordem descendente.
    """
    path_to_file = os.path.join(os.getcwd(), 'source', 'data')
    ds = dataset(os.path.join(path_to_file,caminho))
    sorted = order_by(ds, columns = coluna, reversed=True)
    if isDataFull == True:
        return sorted
    else:
        return sorted.head()