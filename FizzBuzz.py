#Criar uma lista de 1 a 100
# Encontrar números pares
#Encontrar números divisíveis por 3
# encontrar números ímpares

lista_numeros = list(range(1,101))

lista_par = [x for x in lista_numeros if x % 2 ==0]

lista_impar = [x for x in lista_numeros if x % 2 != 0]

div_tres = [x for x in lista_numeros if x % 3 == 0]

print(lista_impar)
print(lista_par)
print(div_tres)