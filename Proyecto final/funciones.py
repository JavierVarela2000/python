import math
def sumatoria(X):#funcion para calcular la sumatoria de una lista
    suma=0#declaracion de la variable que almacenara la sumatoria de los elementos dentro de la lista ingresada
    for i in X:#ciclo que recorre los elementos de la lista ingresada almacenandolos en la variable i
        suma+=i#se calcula la sumatoria de los elementos de la lista
    return suma#retorna la sumatoria

def multi(X,Y):#funcion para calcular la multiplicacion de dos listas
    mult=[]#se define la lista en la que se almacenaran las multiplicaciones
    for i in range(len(X)):#ciclo que recorre de i=0 hasta el tamaño n-1 de la lista ingresada
        mult.append(X[i]*Y[i])#se agrega el producto de x[i]*y[i] al final de la lista mult   
    return mult#retorna la lista con las respectivas multiplicaciones

def eleva(x,n):#funcion que eleva al cuadrado cada elemento de una lista
    new_x=[]#se define la lista en la que se almacenaran los elementos al cuadrado
    for i in range(len(x)):#ciclo que recorre de i=0 hasta el tamaño n-1 de la lista ingresada
        new_x.append(x[i]**n)#se agregga el cuadrado de cada elemento de la lista al final de la lista new_x
    return new_x#retorna la lista con los elementos al cuadrado        

def list_ln(X):#funcion para calcular el logaritmo natural de cada elemento de una lista
    x_ln=[]# se declara una lista para almacenas los elementos a calcular
    for i in(X):#ciclo for que recorre los elementos de la lista ingresada
        x_ln.append(math.log(i))#se agrega el logaritmo narutal de cada elemento al final de la lista
    return x_ln#se retorna el resultado
    
    