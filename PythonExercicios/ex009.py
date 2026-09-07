numero = int(input('Digite um número: '))
limite = int(input('Digite o limite do multiplicador, deve ser >0: '))

print('Tabuada de {} até {}'.format(numero,limite))
for i in range(1,limite+1):
    resultado = numero * i
    print('|{} * {:>2} = {:<3}|'.format(numero,i,resultado))