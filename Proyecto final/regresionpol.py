import funciones as f
def minimos_cuadrados(X,Y):#pendiente
    n=len(X)
    x_2= f.eleva(X,2)#eleva los de las liosta al cuadrado
    x_3= f.eleva(X,3)#eleva los elementos de la lista al cubo
    x_4= f.eleva(X,4)#eleva los elementos de la lista a la cuarta
    #crea una matriz con sublistas que contienen los coeficientes para calcular las incognitas
    m=[[n,f.sumatoria(X),f.sumatoria(x_2)],[f.sumatoria(X),f.sumatoria(x_2),f.sumatoria(x_3)],[f.sumatoria(x_2),f.sumatoria(x_3),f.sumatoria(x_4)]]
    vadj=[f.sumatoria(Y),f.sumatoria(f.multi(X,Y)),f.sumatoria(f.multi(x_2,Y))]#cumple la funcion de ampliada de la matriz anterior
    sol=gauss(m,vadj)#guarda las incognitas obetnidas con la eliminacion gaussiana
    a0=sol[0]#coeficiente 1 
    a1=sol[1]#coeficiente 2
    a2=sol[2]#coeficiente 3
    print("y = "+"%.3g" % (a2)+"x^2 "+"%+.3g" % (a1)+"x "+"%+.3g" % (a0))# imprime la ecuacion junto sus coeficientes   
def gauss(m,vadj): #eliminacion gaussiana
    vsol=[0 for i in range(3)]#crea un arreglo conpuesto por 3 ceros
    #eliminacion por gauss jordan
    for i in range(0,3):#obtiene la matriz inversa
        for r in range(i+1,3):
            factor=(m[r][i]/m[i][i])
            vadj[r]-=(factor*vadj[i])
            for c in range(0,3):
                    m[r][c]=m[r][c]-(factor*m[i][c])
                    
    vsol[2]=vadj[2]/m[2][2]# obtiene la primera incognita y la almacena en el ultimo elemento de la respuesta

    for i in range(1,-1,-1):#obtiene las ultimas 2 incognitas y retorna la matriz respuestra
        suma=0
        for c in range(0,3):
            suma=suma+m[i][c]*vsol[c]
        vsol[i]=(vadj[i]-suma)/m[i][i] 
    return vsol