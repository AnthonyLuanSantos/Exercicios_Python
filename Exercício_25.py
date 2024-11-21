# 25- Peça para que o usuário digite um número,
# em seguida exiba em tela uma mensagem dizendo
# se tal número é PAR ou ÍMPAR:

numero = int(input("Por favor, digite um número: ")) # Número digitado = 8

if (numero % 2) == 0:
    print("O número digitado é PAR.")
else:
    print("O número digitado é ÍMPAR.")
    
"""
Após criar a linha de código responsável por pedir
ao usuário que o mesmo digite um número, validando
esse número como do tipo inteiro e atribuindo o número
em si a uma variável, vamos a estrutura condicional.
"""
"""
Para verificar se um determinado número é par, simplesmente
o resto da divisão desse número por 2 deve ser igual a 0.
Logo, criamos uma condição onde se o resto da divisão de
numero por 2 for igual a 0, será exibida uma frase dizendo
que a variável é PAR, caso a condição seja falsa, será exibida
uma frase dizendo que a variável é ÍMPAR.
"""

# O retorno será:
# O número digitado é PAR.