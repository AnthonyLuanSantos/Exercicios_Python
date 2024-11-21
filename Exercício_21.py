# 21- Verifique se os valores de num1 e de num2
# são iguais ou menores que 100:

num1 = 78
num2 = 100

print(num1 <= 100 and num2 <= 100)

"""
Para esse exemplo, temos de fato uma estrutura 
condicional composta, onde além das condições 
de cada expressão, temos o operador " and " que
determina que ambas a expressões também sejam
verdadeiras para que sej obtido um retorno True.
"""
"""
Em outras palavras, temos na primeira expressão
"o valor de num1 é menor ou igual a 100" assim
como na segunda expressão temos "o valor de num2
é menor ou igual a 100", entre as mesmas temos o
operador " and ", que por sua vez coloca a condição
"a primeira e a segunda expressão são verdadeiras?",
somente retornando True caso ambas sejam.
"""
'''
Pela tabela verdade AND, True e True = True.
(caso uma das expressões fosse False, o retorno
seria False.Ex.: True e False = False, False e True = False.)
'''
'''
A mesma expressão poderia ser reescrita de forma
reduzida, como: print(num1 and num2 <= 100), gerando
o mesmo retorno.
'''

# O retorno será:
# True