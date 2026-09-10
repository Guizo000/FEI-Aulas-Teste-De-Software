import main
import pytest

def test_retirar_do_estoque(valores):
    assert main.retirar_do_estoque(qtd=valores["valor_menor"], estoque=valores["valor_maior"]) == 50

    with pytest.raises(
        ValueError, 
        match="Quantidade solicitada maior que o estoque disponível."):
            main.retirar_do_estoque(qtd=valores["valor_maior"], estoque=valores["valor_menor"])


@pytest.mark.parametrize("entrada, esperado", [
    (100, "Alto"),
    (20, "Médio"),
    (10, "Baixo")    
])
def test_classificar_estoque(entrada, esperado):
    assert main.classificar_estoque(entrada) == esperado


@pytest.mark.parametrize("entrada, esperado", [
    (0, True),
    (1000, True) ,
    (-10, False),
    (1100, False)  
])
def test_validar_quantidade(entrada, esperado):
     assert main.validar_quantidade(entrada) == esperado