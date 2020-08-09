"""
Tipos de dados
str - String = textos 'Assim' "Assim"
int - Inteiro = -1 ou -65654 ou 0 ou 123456 (somente numero inteiro)
float - real/ponto flutuante = -1.1 ou 2.654 ou 125.254 (numero fracionado)
bool - booleano/logico = True ou False
"""
print('Luiz', type('Luiz'))
print(10, type(10))
print(10.1, type(10.1))
print(10 == 10, type(10 == 10))
print('l' == 'L', type('l' == 'L'))

print('10', type('10'), bool('10'))  # na maioria das vezes um campo preenchido retorna true
print('10', type('10'), type(int('10')))  # colocando uma string dentro de uma int eu converti a string em inteiro
print('10', float('10'))  # convertendo inteiro em flutuante

# criando cadastro simples de exercício

# String: nome
print('Geison', type('Geison'))

# Idade: int
print(30, type(30))

# Altura: float
print(1.70, type(1.70))

# Maior de idade: booleano
print(30 > 18, type(30 > 18))
