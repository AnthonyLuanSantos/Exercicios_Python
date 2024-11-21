# 28- Crie uma lista com 8 elementos de uma
# lista de compras de supermercado:
# Por meio de um laço de repetição for,
# liste individualmente cada um dos ítens.

lista8 = ["Arroz", "Feijão", "Mandioca", "Batata",
          "Açucar", "Leite", "Bacon", "Alface"]

for i in lista8:
    print(i)
    
"""
Quando estamos a percorrer os elementos de uma lista
por meio de um laço for, cada elemento dentro de seu
separador será lido individualmente, tendo seu conteúdo
(independentemente do tipo de dado) sendo assossiado 
a variável temporária i.
"""

# O retorno será:
# Arroz
# Feijão
# Mandioca
# Batata
# Açucar
# Leite
# Bacon
# Alface