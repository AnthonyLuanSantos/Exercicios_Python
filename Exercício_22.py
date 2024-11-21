# 22- Verifique se os valores de num1 ou de num2
# são iguais ou maiores que 100:

num1 = 93
num2 = 100

print(num1 >= 100 or num2 >= 100)

"""
Diferentemente do exercício anterior, agora utilizamos
do operador " or " podemos criar expressões lógicas
onde basta uma das expressões ser verdadeira para que 
todo o contexto seja validado.
"""
"""
Note que na primeira expressão, o valor de num1 é menor
que 100, já o valor de num2 não é maior, mas é igual a 100,
em função do operador " or ", mesmo caso um dos resultados
da expressão fose False, o retorno seria True.
"""

# O retorno será:
# True