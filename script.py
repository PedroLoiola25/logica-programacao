print("Olá, seja bem vindo a minha primeira calculadora")

num1 = input('Digite o primeiro número:')

operação = input('Digite a operação desejada(+,-,*,/),:')

soma = "+"

subtração = "-"

Mutiplicação = "*"

Divisão = "/"

tupla = ("+,-,*,/")

num2 = input('Digite o segundo número:')

num1_convert1 = int(num1)

num1_convert2 = int(num2)

if operação == soma:
  print( 'Resultado:', num1_convert1 + num1_convert2)
elif operação == subtração:
  print( 'Resultado:', num1_convert1 - num1_convert2)
elif operação == Mutiplicação:
  print( 'Resultado:', num1_convert1 * num1_convert2)
elif operação == Divisão:
  print( 'Resultado:', num1_convert1 / num1_convert2)
else:
  print("Resultado: Operação não pode ser realizada")
