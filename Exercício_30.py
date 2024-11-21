# 30- Crie um programa que realiza a contagem de
# 0 a 20, exibindo apenas os números pares:

# Ex.1:
inicio = 0
fim = 20

for i in range(0, 21):
    if i % 2 == 0:
        print(i)

"""
Da mesma forma como no exemplo anterior, usando do 
método range() parametrizado com o valor de início
e de fim (acressido de 1 unidade), podemos definir
que serão exibidos apenas os números pares simples-
mente criando uma condição onde apenas serão exibidos
os números que o resto da divisão por 2 seja 0.
"""

# Ex.2:
for i in range(0, 21, 2):
    print(i)
    
"""
Uma forma alternativa que temos para resolver esse
exercício é usando do terceiro paâmetro em justaposição
de dois em dois, parametrizando o método range() em
seu terceiro parâmetro justaposto com o número 2,
indiretamente exibindo apenas os números pares.
"""

# O retorno será:
# 0
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20