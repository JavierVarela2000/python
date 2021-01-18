#Regresion lineal(y=mx+b)
import funciones as fun#se incluyen las funciones para el calculo
def reg_lineal(X,Y):#funcion que recibe 2 matrices para calcular la regresion lineal
    n=len(X)#se asigna el valor de la longitud de la lista a la variable
    numerador = fun.sumatoria(fun.multi(X,Y))-((fun.sumatoria(X)*fun.sumatoria(Y))/n)#se calcula del numerador para el calculo de la pendiente m
    denominador = fun.sumatoria(fun.eleva(X,2))-((fun.sumatoria(X)**2)/n)#se calcula el denominador para el calculo de la pendiente m
    m=numerador/denominador#se calcula la pendiente divideinto el numerador y el denominador previamente calculados
    b = (fun.sumatoria(Y)/n)-(m*fun.sumatoria(X)/n) # se calcula el coeficiente b de la formula
    print("y = "+"%.3g" % (m)+"x "+"%+.3g" % (b))# se imprimen y=mx+b de acuerdo con el calculo previo

    