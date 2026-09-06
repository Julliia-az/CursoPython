# + = adição
# - = subtração
# * = multiplicação
# / = divisão
# ** = potência
# // = divisão inteira
# % = resto da divisão

# Ordem de precedencia:
# 1° = ()
# 2° = **
# 3° = *, /, //, %
# 4° = +, -

# nome = input('Qual é seu nome? ')
# print('Prazer em te conhecer, {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
rd = n1 % n2
print('A adição é: {};\n'
      'A subtração é: {};\n'
      'A multiplicação é: {};\n'
      'A divisão é: {:.3f};\n'
      'A divisão inteira é: {};\n'
      'A potência é: {};\n'
      'O resto da divisão é: {}.'.format(a,s,m,d,di,p,rd))