from math import hypot

c_oposto = float(input('Digite o comprimento do cateto oposto: '))
c_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = hypot(c_oposto, c_adjacente)

print('O comprimento da hipotenusa é: {:.2f}'.format(hipotenusa))