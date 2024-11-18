# 10- Mostre o tamanho da lista nomes /
# o número de elementos da lista nomes:
# Mostre separadamente apenas o
# terceiro elemento dessa lista:

nomes = ["Luciano", "DuLoL", "Levi", "Gut", "Symon"]

print(len(nomes))
print(nomes[2])

"""
Em nossa função print() usando do método len() por
sua vez parametrizado com a variável nomes, o retorno
esperado é o número de elementos que compõe essa lista.
"""
"""
Para instanciar apenas um determinado elemento, devemos
fazer referência ao mesmo por meio de seu número de 
índice, sendo o primeiro elemento o valor 0, o segundo
elemento o valor 1, e assim por diante.
"""
"""
Para exibir em tela apenas o terceiro elemento da lista
nomes, basta parametrizar nossa função print() com nomes[]
fazendo referência ao índice de número 3.
"""
# O retorno será:
# 5
# Levi