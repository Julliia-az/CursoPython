#  °F = (°C x (9/5) + 32); K = °C + 273.15
c = float(input('Digite a temperatura em °C: '))
f = c * 9/5 + 32
k = c + 273.15
print('{}°C é igual a {}°F e {}°K'.format(c,f,k))