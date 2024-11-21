# 24- Crie duas variáveis com dois valores numéricos
# inteiros digitados pelo usuário, caso o primeiro valor
# seja maior que o segundo, exiba em tela uma mensagem
# de acordo, caso contrário, exiba em tela uma mensagem
# dizendo que o primeiro valor digitado é menor que o segundo:

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

if num1 > num2:
    print("O primeiro valor é maior que o segundo.")
else:
    print("O primeiro valor é menor que o segundo.")
    
"""
Lembrando que em uma estrutura condicional simples,
criamos um objetivo a ser alcançado/atingido, executando
blocos de código de acordo com as condições impostas.
"""
"""
Nesse caso, como temos apenas dois possíveis desfechos
de acordo com a condição, supondo que o usuário tenha
digitado 25 e 26, respectivamente, o resultado exibido
seria "O primeiro valor é menor que o segundo.", uma vez
que a primeira condição (se num1 for maior que num2)
não seja válida.
"""

# O retorno será:
# O primeiro valor é menor que o segundo.