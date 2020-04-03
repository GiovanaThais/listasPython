#comando para teste
#pytest-3 -s teste.py

from ME_Giovana import cad
from ME_Giovana import listar
from ME_Giovana import custos
import ME_Giovana as atv


def test_cadastro():
    assert cad() == 0, 'Cadastro feito com sucesso'
    pass

def test_listar():
    assert listar() != None, 'Registros Vazios'
    pass

def test_custo():
    assert custos() != None, 'Registros de custos vazios'
    pass