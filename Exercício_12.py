# 12- Some os valores das variáveis num1 e num2,
# atribuindo o resultado da soma a uma nova variável
# homônica. Exiba em tela o conteúdo desta variável.

num1 = 85
num2 = 175
soma = num1 + num2

print(soma)

"""
No exemplo anterior, ao executar a operação matemática
diretamente como parâmetro de nossa função print(), o
resultado foi exibido em tela porém após o enceramento
desse bloco de código tal dado, como esperado, foi
descarregado da memória.
"""
"""
Para guardar essa informação de forma "permanente" é
nessessário realizar a operação atribuída a uma variável.
Desse modo, podemos exibir o dado em tela parametrizando
a função print() com a variável em questão, e encerado
o processo o dado continua guardado na variável para reutilização.
"""

# O retorno será:
# 260