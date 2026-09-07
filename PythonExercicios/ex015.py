d = int(input('Quantos dias alugado? '))
km = float(input('Quantos km rodados? '))
v = (60 * d) + (0.15 * km)
print('O total a pagar é de {}'.format(v))