from math import cos, sin, tan, radians
an = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))

print('O ângulo de {} têm: \nSeno de {:.2f} \nCosseno de {:.2f} \nTangente de {:.2f}'.format(an, seno, cosseno, tangente))