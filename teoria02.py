# Exemplo que causa TypeError

# try:
#     resultado = len(3)
#     print(resultado)
# except TypeError as e:
#     print(e)
# else:
#     print("Tudo ocorreu bem")
# finally:
#     print("O important é participar")

# numero = int(input("Insira um numero:"))
# if isinstance(numero, int):
#     print("A variável é um inteiro.")
# else:
#     print("A variável não é um inteiro.")

idade = 22 

IDADE_MINIMA_PARA_DIRIGIR = 18
IDADE_PARA_TIRAR_A_CARTEIRA =18

if idade <= IDADE_MINIMA_PARA_DIRIGIR:
    print("Não pode dirigir")
elif idade == 18:
    print("Pode tirar a carteira esse ano")
else:
    print("Pode dirigir")