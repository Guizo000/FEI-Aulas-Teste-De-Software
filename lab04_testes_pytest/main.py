def validar_quantidade(qtd):
    return (qtd >= 0 and qtd <= 1000)

def calcular_valor_total(qtd, preco_unitario):
    return qtd * preco_unitario

def retirar_do_estoque(qtd, estoque):
    if qtd <= estoque:
        return estoque - qtd
    else:
        raise ValueError("Quantidade solicitada maior que o estoque disponível.")

def classificar_estoque(qtd):
    if qtd >= 100:
        return "Alto"
    elif qtd >= 20:
        return "Médio"
    else:
        return "Baixo"