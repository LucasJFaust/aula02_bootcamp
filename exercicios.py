# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# numero_01 = int(input("Digite um número inteiro: "))
# numero_02 = int(input("Digite novamente um número inteiro: "))
# soma_numeros = numero_01 + numero_02
# print(f"A soma dos números inteiros é igual a: {soma_numeros}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# n_usuarios = int(input("Coloque o número de usuários: "))
# DIVISOR = 5
# calculo = n_usuarios % DIVISOR
# print(f"O valor do resto da divisão do número de usuários por 5 é: {calculo}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# n1 = int(input("Digite o primeiro número: "))
# n2 = int(input("Digite o segundo número: "))
# multi = n1 * n2
# print(f"O resultado da multiplicação dos números fornecidos é: {multi}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# try:
#     numero_01 = int(input("Inserir um número inteiro: "))
#     numero_02 = int(input("Insira o outro número: "))
#     resultado = numero_01 // numero_02
#     print(resultado)
# except ZeroDivisionError:
#     print("integer division or modulo by zero")
# except KeyboardInterrupt:
#     print("Acho que você não quis inserir um numero")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# n1 = float(input("Digite um número: "))
# q_n1 = n1 ** 2
# print(f"O quadrado do numero ditado é: {q_n1}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# try:
#     n1 = float(input("Digite o primeiro número: "))
#     n2 = float(input("Digite o segundo número: "))
#     soma = n1+n2
#     print(f"Soma igual a: {soma}")
# except TypeError:
#     print("Erro de digitação")


# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# import statistics
# n1 = float(input("Digite o primeiro número: "))
# n2 = float(input("Digite o segundo número: "))
# mean = statistics.mean([n1, n2])
# print(f"A média dos números é: {mean:.3f}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# base = float(input("Digite o valor da base: "))
# exp = float(input("Digite o expoente: "))
# calc = base ** exp
# print(f"O valor da base é: {base}, o expoente: {exp} e o total é de:{calc:.2f}")


# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# criando uma fubção para resolver:
# def celsius_fahrenheit():
#    c = float(input('Digite a temperatura em °c: '))
#    f = float((9 * c) / 5) + 32

#    return print('A temperatura em fahrenheit: {0}°F'.format(f))

# celsius_fahrenheit()

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# import math
# raio_do_circulo = float(input("Digite o raio: "))
# area_do_circulo = math.pi * raio_do_circulo ** 2
# print(f"{area_do_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# st = str(input("Digite sua string: ").upper())
# print(st)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# st = str(input("Digite sua string: ").lower())
# print(st)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# st = str(input("   Digite sua string:   ").strip())
# print(st)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
# lista_dia_mes_ano = data_do_usuario.split("/")
# print(f"O elemento 1 é o: {lista_dia_mes_ano[0]}, o segundo é: {lista_dia_mes_ano[1]} e o terceiro é: {lista_dia_mes_ano[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# s1 = str(input("Digite o primeiro nome: "))
# s2 = str(input("Digite o segundo nome: "))
# conc = s1 + " " + s2
# print(conc)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# v1 = True
# v2 = False
# resultado = v1 and v2
# print(f"O resultado lógico é: {resultado}")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# v1 = True
# v2 = False
# resultado = v1 or v2
# print(f"O resultado lógico é: {resultado}")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

# valor1 = bool(input("Digite True ou False: "))
# resultado_not = not valor1
# print(f"Resultado do NOT lógico: {resultado_not}")

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

# n1 = int(input("Digite uma número: "))
# n2 = int(input("Digite uma número: "))

# if n1==n2:
#     print(f"O valor de n1 = {n1} é igual ao valor de n2 = {n2}, portanto os valores são iguais")
# else:
#     print("Valores diferentes")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# n1 = int(input("Digite uma número: "))
# n2 = int(input("Digite uma número: "))

# if n1 != n2:
#     print(f"O valor de n1 = {n1} é diferente do valor de n2 = {n2}")
# else:
#     print("Valores iguais")

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação