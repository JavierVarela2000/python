import regresionlineal as reg_l# se importa el ajuste por regresion lineal
import regresionexponencial as reg_e# Se importa el ajuste exponencial
import regresionpol as reg_p
#import regresionpolinomial as reg_p por implementar
def Menu():#menu principal
    op=1#variable para moverse por el menu
    while(op):#inicio del menu repetitivo
        #imprimir las opciones del menu
        op=int(input("Menu\n1.Ingreso de datos\n2.ajuste por minimos cuadrados\n3.ajuste exponencial\n4.ajuste polinomial\n5.Salir\nescoge una opcion: "))
        #comprobar si la opcion escogida esta dentro de las permitidas
        while(op<0 or op>5):
            op=int(input("ingrese una opcion valida: "))#vuelve a preguntar la opcion
        if (op==1):#Ingreso de datos
            #guia al usuario sobre como ingresar los datos de X
            print("Ingrese los valores de X separados por un espacio y precione enter, de la siguiente manera:1 2 3 . . ")
            x=[float(x) for x in input("X=").split()]#crea una lista con los datos ingresados 
            #guia al usuario sobre como ingresar los datos de Y
            print("Ingrese los valores de Y separados por un espacio y precione enter, de la siguiente manera:1 2 3 . . ")
            y=[float(y) for y in input("Y=").split()]#crea una lista con los datos ingresados
        elif(op==2):#ajuste por minimos cuadrados
            #excepcion 1
            try:
                print("\n\nminimos cuadrados\n\n")
                reg_l.reg_lineal(x,y)#llamado a la funcion que calcula minimos cuadrados
            except UnboundLocalError:#en caso de no haber ingresado datos previos imprimira lo siguiente
                print("primero ingresa los datos")
            except IndexError:
                print("Para poder realizar el calculo debes ingresar correctamente los datos")                
        elif(op==3):#ajuste exponencial
            #excepcion 2
            try:
                print("\n\najuste exponencial\n\n")
                reg_e.regresion_exponencial(x,y)#llamado a la funcion que calcula el ajuste exponencial
            except UnboundLocalError:#en caso de no haber ingresado datos previos imprimira lo siguiente
                print("primero ingresa los datos") 
            except IndexError:
                print("Para poder realizar el calculo debes ingresar correctamente los datos")            
        elif(op==4):#ajuste polinomial
            try:
                print("ajuste polinomial")
                reg_p.minimos_cuadrados(x,y)
            except UnboundLocalError: 
                print("primero ingresa los datos") 
            except IndexError:
                print("Para poder realizar el calculo debes ingresar correctamente los datos")
                
        elif(op==5):#Salir
            print("Fin del programa")
            op=0#define la variable opcion en 0 para que salga del bucle donde se encuentra el menu repetitivo
             
if __name__ == '__main__':#ejecuciion del menu
    Menu()        
