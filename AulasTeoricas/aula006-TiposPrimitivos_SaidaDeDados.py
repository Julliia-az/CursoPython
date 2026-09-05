# O código das próximas quatro linhas transforma o input em int, o que torna possivel a soma entre os valores fornecidos, sem isso ele apenas realizaria uma concatenação(jusnção de strings)
# a = int(input('Primeiro número = '))
# b = int(input('Segundo número = '))
# s = a+b
# print('A soma entre {} e {} vale {}'.format(a,b,s))

# o metodo 'is...()' mostra se é possivel converter o input para um determinado formato, você pode ver isso no PythonExercicios\ex004.py
n = input('Digite algo: ')
print(type(n))
print(n.isnumeric())