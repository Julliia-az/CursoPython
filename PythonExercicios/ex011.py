l = float(input('Digite a largura em metros: '))
a = float(input('Digite a altura em metros: '))
area = l * a
tinta = area / 2
print('Sua parede tem a dimenção de {}x{} e sua área é de {}m² \nA quantidade de tinta necessária é igual a: {}l'.format(l, a, area, tinta))