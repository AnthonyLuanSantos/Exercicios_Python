# 29- Crie um programa que leia um valor de início
# e um valor final, exibindo em tela a contagem
# dos números dentro desse intervalo.

inicio = int(input("Digite um valor de início: ")) # 0
fim = int(input("Digite um valor final: ")) # 10

for i in range(inicio, fim + 1):
    print(i)

"""
Sempre que temos um intervalo numérico com início e
fim pré-estabelecidos, podemos usar do método range()
para ler todos elementos desse intervalo. Associando
o operador lógico " in ", usando range() dentro de um
laço for, é possível percorrer e iterar sobre cada
elemento dentro do intervalo.
"""
"""
Sendo assim, apenas como exemplo, para percorrer
elementos dentro de um intervalo entre 0 e 10 temos
de parametrizar nosso range() com números entre 0 e 11.
"""
"""
Caso não fosse definido fim + 1 como parâmetro em
range() a contagem encerraria em 9, não concordando
com o enunciado da questão.
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
