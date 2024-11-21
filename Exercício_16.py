# 16- Escreva um programa que pede que o
# usuário dê entrada em dois valores,
# em seguida, exiba em tela o resultado da
# soma, subtração, multiplicação e divisão
# desses números:

num1 = int(input("Por favor, digite o primeiro valor: "))
num2 = int(input("Por favor, digite o segundo valor: "))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

"""
Como feito em exemplos anteriores, por meio
da função input() podemos pedir que o usuário
digite dois números que ficarão atribuídos a
duas variáveis distintas: num1 e num2.
"""
"""
Em seguida, por meio de nossa função print()
por sua vez parametrizada por uma f'string,
conseguimos em máscaras de substituição
instanciar tanto os valores de num1 quanto
os valores de num2, realizando também as devidas
operações matemáticas dentro de uma máscara de
substituição. 
"""

# O retorno será:
# 14
# -4
# 45
# 0.5555555555555556