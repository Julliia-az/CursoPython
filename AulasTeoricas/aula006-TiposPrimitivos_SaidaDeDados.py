# O código nas próximas três linhas não funciona como deveria, pois o valor recebido pelo input é tratado como string e não com int, com isso ele apenas junta os valores digitados e não os soma
# a = input('Primeiro número = ')
# b = input('Segundo número = ')
# print('A soma vale:',a+b)

a = int(input('Primeiro número = '))
b = int(input('Segundo número = '))
print('A soma vale:',a+b)
