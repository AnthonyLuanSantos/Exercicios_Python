# 31- Crie um programa que realiza a Progressão
# Aritimética de 20 elementos, com primeiro termo
# e razão definidos pelo usuário:

termo = int(input("Digite o primeiro termo: ")) # 10
razao = int(input("Digite a razão: ")) # 3

pa = termo + (20 - 1) * razao

for i in range(termo, pa + razao, razao):
    print(i)
    
"""
Lembrando que uma progressão aritimética é uma
operação onde definimos um número inicial e uma
constante, também chamados de termo e razão,
respectivamente. A progressão em si nada mais é
do que a soma do termo anterior com a constante.
"""
"""
Para nosso exercício pedimos que o usuário dê entrada
tanto no termo (valor inicial) quanto na razão (constante)
por meio da função input() atribuindo esses valores
a suas respectivas variáveis.
"""
"""
Na sequência criamos uma variável de nome "pa" que
contextualizando a fórmula de uma progressão aritimética,
pega o valor de termo, somando com a constante 
multiplicada pela razão. Lembrando de realizar a
subtração da constante em 1 para que tenhamos o 
gatilho para finalizar a progressão dentro do valor definido.
"""
"""
Com isso, podemos simplesmente criar um laço for que
utilizando o método range() define o valor de termo
como valor inicial, pa + razão como valor final, 
exibindo no intervalo estipulado por razão. Sendo que
a cada execução do laço é exibido em tela o valor da
progressão por meio da função print().
"""

# O retorno será:
# 10
# 13
# 16
# 19
# 22
# 25
# 28
# 31
# 34
# 37
# 40
# 43
# 46
# 49
# 52
# 55
# 58
# 61
# 64
# 67