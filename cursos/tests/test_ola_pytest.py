def soma(n, n2):
    return n + n2


def test_meu_primeiro_teste():
    resultado = soma(1, 1)
    resultado_esperado = 2
    assert resultado == resultado_esperado


def test_meu_segundo_teste():
    resultado = soma(2, 1)
    resultado_esperado = 3
    assert resultado == resultado_esperado
