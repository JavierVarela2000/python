#y = Ae^(Bx)
import math #importar libreria math
import funciones as f# importar funciones

def regresion_exponencial(X,Y):# funcion para calcular el ajuste de curvas exponencial
    n=len(X)#se signa el numero de elementos ingresados a la variable n
    ln_y=f.list_ln(Y)# se asigna el valor que retorna la fucion a la variable ln_y
    B_num=(n*f.sumatoria(f.multi(X,ln_y)))-(f.sumatoria(X)*f.sumatoria(ln_y))#se calcula el numerador del coeficiente B
    B_den=(n*f.sumatoria(f.eleva(X,2)))-(f.sumatoria(X)**2)#se calcula el denmominador del coeficiente B
    B=B_num/B_den#se se dividen el numerador y el denominador para calcular el coeficiente B
    
    A=math.e**((f.sumatoria(ln_y)/n)-(B*f.sumatoria(X)/n))#Se calcula el coeficiente A
    print("y = "+"%.3g" %(A)+"e ^(%.3gx)" %(B))#Se imprime el ajuste y = Ae^(Bx)
    
    
    
