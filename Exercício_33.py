# 33- Crie um programa que realiza a
# contagem regressiva de 20 segundos:

from time import sleep

for i in range(20, -1, -1):
    print(i)
    sleep(1)
    
print("Contagem finalizada!")

"""
Para esse exercício, uma forma automatizada
e otimizada de gerar um mecanismo de contagem
regressiva é usando do módulo " sleep " da 
biblioteca " time ". Para isso, via comando
" from time import sleep " importamos tal módulo
e suas funcionalidades.
"""
"""
Na sequência, para gerar a contagem regressiva
podemos usar de um laço for com o método range()
de modo que o valor inicial da contagem é 20,
o valor final definido em -1 fará a contagem 
decrescente até 0, sendo o último parâmetro,
referente ao intervalo de números, definido
também como negativo para que a contagem aconteça
de forma decrescente.
"""
"""
Podemos observar o bloco do laço for, a cada execução
é exibida em tela o número referente ao passo, assim
como chamando a função sleep() parametrizada em 1, 
é definido que a cada execução do laço haverá um tempo
de espera de 1 segundo. Dessa forma, teremos não apenas
uma contagem regressiva de 20 para 0, mas tal contagem
será exibida sincronizada de 1 em 1 segundo.
"""
"""
Ao sair do laço for, através da função print(), será
exibida a mensagem dizendo que a contagem regressiva
chegou ao fim.
"""

# O retorno será:
# 20
# 19
# 18
# 17
# 16
# 15
# 14
# 13
# 12
# 11
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0
# Contagem finalizada!