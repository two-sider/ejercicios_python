# Ejercicios de prueba, practica.
#http://www.pythondiario.com/2013/05/ejercicios-en-python-parte-1.html
#https://www.discoduroderoer.es/ejercicios-propuestos-y-resueltos-basicos-en-python/
#Estudiar cadenas
#http://www.openbookproject.net/thinkcs/archive/python/spanish2e/cap07.html
print('Ejercicios')
# 1- Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
# Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un 
# muy buen ejercicio.

def max(numero1, numero2):
    if numero1 > numero2:
        print(numero1)
    elif numero2 > numero1:
        print(numero2)
    else:
        print("son iguales")
def ej1():
    print("Funcion que permite sacar el numero mayor")
    numero1 = int(input("Primer numero:"))
    numero2 = int(input("Segundo numero:"))
    max(numero1,numero2)

# 2- Definir una función max_de_tres(), 
# que tome tres números como argumentos y devuelva el mayor de ellos.
def max_de_tres(numero1, numero2, numero3):
    if numero1 > numero2 and numero1 > numero3:
        print(numero1)
    elif numero2 > numero1 and numero2 > numero3:
        print(numero2)
    elif numero3 > numero1 and numero3 > numero2:
        print(numero3)
    else:
        print("son iguales")
def ej2():
    print("Funcion que permite sacar el numero mayor entre 3 numeros")
    numero1 = int(input("Primer numero:"))
    numero2 = int(input("Segundo numero:"))
    numero3 = int(input("tercer numero:"))
    max_de_tres(numero1,numero2,numero3)
# 3- Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
def long_lista(cadena):
    cont = 0
    for i in cadena:
        cont +=1
    return cont

def ej3():
    print("Funcion que permite sacar la longitud de una cadena o lista")
    cadena = str(input("Escriba la cadena:"))
    valor = long_lista(cadena)
    print(valor)

    
# 4- Escribir una función que tome un carácter y devuelva True si es una vocal, 
# de lo contrario devuelve False.
def if_vocal(letra):
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        return True
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        return True
    else:
        return False
def ej4():
    print("Funcion que permite saber si la letra es una vocal")
    letra = str(input("Escriba un caracter:"))
    if_vocal(letra)
    

# 5- Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente 
# todos los números de una lista.
# Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

# 6- Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

# 7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

# 8- Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

# 9- Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

# 10- Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:


#Funcion para elegir ejercicio a mostrar
def ejercicios():
    ejercicio = int(input("Elija ejercicio 1-10 \n"))
    if ejercicio == 1:
        ej1()
    elif ejercicio == 2:
        ej2()
    elif ejercicio == 3:
        ej3()
    elif ejercicio == 4:
        ej4()
ejercicios()