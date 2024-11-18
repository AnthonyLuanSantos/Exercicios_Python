# 8- Peça para que o usuário digite um número, em
# seguida o converta para float, exibindo em tela
# tanto o número em si quanto o seu tipo de dado:

numero = input("Digite um número: ")
numero = float(numero)

print(numero)
print(type(numero))

"""
Uma vez criada nossa variável numero, com seu conteúdo
vindo da interação com o usuário, podemos atualizar o
conteúdo dessa variável, mudando inclusive o tipo de dado.
Para isso, nossa variável numero recebe como atributo
o método float() parametrizado com ela mesma.
"""
"""
Dessa forma, i conteúdo atribuído a variável numero é
convertido de formato e salvo sobrescrevendo o conteúdo
antigo dessa variável. Por meio da função print() podemos
exibir em tela tanto o tipo quanto o conteúdo da variável
numero.
"""

# Supondo que o usuário tenha digitado 15, o retorno será:
# 15
# float