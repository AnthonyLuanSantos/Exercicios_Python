# 26- Crie uma variável com valor inicial 0,
# enquanto o valor dessa variável for igual
# ou menos que 10, exiba em tela o próprio
# valor da variável:
# A cada execução, a mesma deve ter o seu valor
# atualizado, incrementado em 1 unidade.

var = 0

while var <= 10:
    print(var)
    var = var + 1

"""
Toda vez que seja necessário repetir determinada
instrução enquanto um determinado objetivo não
é atingido, podemos realizar essa repetição através
da estrutura de repetição " while ".
"""
"""
Quando usamos "while", definimos uma condição a ser
alcançada ou validada, e para que a execução do
código não entre em um loop infinito, também usamos
nessa estrutura de código de uma variável de controle. 
"""

# O retorno será:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10