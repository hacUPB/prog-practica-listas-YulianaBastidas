# Ejercicio 1: Suma de elementos en una lista de listas
def suma_matriz(matriz):
  # Recibe una lista de listas y devuelve la suma de todos sus elementos.
  suma = 0 # crea un acumulador
  for fila in matriz: # itera cada fila en la matriz
    for elemento in fila: # itera cada número dentro de la sublista
      suma += elemento # suma el elemento al acumulador
  return suma

suma_matriz([[1, 2], [3, 4]]) 

    

# Ejercicio 2: Encontrar el valor máximo en una matriz
def maximo_matriz(matriz):
  # Recibe una lista de listas y devuelve el valor máximo.
  maximo = matriz[0][0] # asume que el primer elemento es el mayor inicialmente
  for fila in matriz: # itera cada sublista (fila)
    for elemento in fila: # itera cada número dentro de la sublista
      if elemento > maximo: # compara si el elemento actual es mayor que el máximo actual
        maximo = elemento # actualiza el valor máximo
  return maximo

maximo_matriz([[3, 7], [2, 9]]) # devuelve 9

 

# Ejercicio 3: Verificar si un número es primo
def es_primo(n):
  # Recibe un número y devuelve True si es primo, False en caso contrario.
  if n <= 1:  # Los números menores o iguales a 1 no son primos
    return False
  for i in range(2, int(n**0.5) + 1):  # Solo es necesario verificar hasta la raíz cuadrada de n
    if n % i == 0:  # Si n es divisible por cualquier número, no es primo
      return False
  return True  # Si no se encontró ningún divisor, es primo

# Ejemplo de prueba
es_primo(7)  # devuelve True
es_primo(4)  # devuelve False


# Ejercicio 4 (versión con bucles for)
def transponer_matriz(matriz):
  # Creamos una lista vacía donde guardaremos la matriz transpuesta
  transpuesta = []

  # Recorremos las columnas de la matriz original
  for i in range(len(matriz[0])):  # Esto recorre las columnas
    fila_transpuesta = []  # Creamos una nueva fila para la transposición

    # Recorremos las filas de la matriz original
    for j in range(len(matriz)):  # Esto recorre las filas
      fila_transpuesta.append(matriz[j][i])  # Agregamos el elemento de la columna i

    # Agregamos la fila transpuesta a la matriz transpuesta
    transpuesta.append(fila_transpuesta)

  return transpuesta

# Ejemplo de prueba
print(transponer_matriz([[1, 2], [3, 4]]))  # Devuelve [[1, 3], [2, 4]]


# Ejercicio 5: Filtrar números pares
def filtrar_pares(lista):
     pares = []   # crea lista de pares
     for i in lista: # Itera cada item de la lista
  # Revisa si es par, y si lo es sumar al contador.
  # Si el residuo del numero divido 2 es 0 significa que es par, osea 8 % 2 = 0, pero 7 % 2 = 1 por que es impar
      if i % 2 == 0:
        pares.append(i)
      return pares
filtrar_pares([1, 2, 3, 4])
    

# Ejercicio 6: Contar la cantidad de palabras en una frase
def contar_palabras(frase):
    frase = frase.split(' ') # divide un string en varias partes según el separador (espacio en este caso)
    return len(frase) # Retorna el tamaño del arreglo, osea la cantidad de palabras que habia en la frase

contar_palabras("susie tiene heterocromía")
   

# Ejercicio 7: Crear una tabla de multiplicar
def tabla_multiplicar(n):
    tabla = [] # crea arreglo
    for i in range(1,11): # Itera 10 veces
     tabla.append(n*i) # Multiplica en numero por i (1-10)
    return tabla

tabla_multiplicar(10)
    

# Ejercicio 8: Contar números negativos en una lista
def contar_negativos(lista):
     cont = 0 # crea contador
     for i in lista: # Itera cada item de la lista
      if i < 0:     # Revisa si es negativo, y si lo es sumar al contador
       cont += 1
     return cont

contar_negativos([-1, 0, 1, 2, -3])
  

# Ejercicio 9: Determinar si una lista está ordenada
def lista_ordenada(lista):
      #Itera cada elemento de la lista hasta el penultimo elemento, y revisa si el valor actual es mayor al siguiente, en caso de que lo sea no estaria ordenado de menor mayor y retorna falso.Si la condicion no se cumple para ningun elemento, osea que cada elemento es menor o igual que el siguiente, se cumple el ordenamiento de menor a mayor.
  for i in range(len(lista) - 1):
    if lista[i] > lista[i+1]:
      return False
  return True

print(lista_ordenada([1, 2, 3, 4]))
print(lista_ordenada([1, 3, 2, 4]))

# Ejercicio 10: Cifrar un texto con el cifrado César

def cifrado_cesar(texto, desplazamiento):
   abecedario = "abcdefghijklmnñopqrstuvwxyz" # Se tiene todo el abecedario en español
   cifrado = "" #El texto resultante
  # Se itera por cada letra en el texto
   for letra in texto:
    indice = abecedario.index(letra) # Se obtiene el indice de la letra en el abecedario

    # Se desplaza el indice de la letra, y se utiliza el operador modulo por si en caso de que
    # Se tenga un valor mayor a la cantidad de letras en el abecedario se empieze a contar desde los valores desde el inicio, ej 30 % 27 = 3
    nuevo_indice = (indice + desplazamiento) % len(abecedario)
    cifrado += abecedario[nuevo_indice]
   return cifrado
cifrado_cesar("abcd",1)
    


#Aquí comienza el progrma principal. No modifiques el código debajo de esta línea.
def main():
    pass


if __name__ == "__main__":
    main()