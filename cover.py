from functools import reduce #Se importa la funcion reduce
import numpy as np 

#Se define la funcion generar_matriz.Se crea una nueva matriz en base
#a los clientes restantes    
def generar_matriz(clientes,centros): 
    for centro in centros:
        for cliente in clientes:
            centros[centro][cliente]=0
    return centros
#Retorna la covertura de un centro
def covertura(centro):
    covertura=reduce((lambda x,y: x+y),centro)
    return covertura

def clientes_servidos(centro):
    clientes=[]
    for posicion,cliente in enumerate(centro):
        if(cliente==1):
            clientes.append(posicion)
    return clientes

def set_cover(centros,clientes):
    centros_utilizados=[]
    zeros=np.zeros(len(clientes))

    while(len(clientes) > 0 and len(centros) > 0): #Mientras queden clientes por servir o existan centros se ejecutará el prgorama
        print("clientes a servir: ",clientes)
        print("los centros actuales son: ",centros)
        max_cover=max(centros,key = lambda i: covertura(centros[i])) #Se escoge el que tenga mayor cobertura
        if(centros[max_cover]==list(zeros)): #Si el que estoy añadiendo no cubre ningun cliente, entonces detengo el programa
            break       
        centros_utilizados.append(max_cover) #Añado a mi solucion el centro escogido
        print("El que cubre la mayor cantidad es",max_cover) 
        clientes_a_eliminar=clientes_servidos(centros[max_cover]) #Son los clientes que fueron servidor por el centro utilizado
        print("Todos estos clientes fueron servidos",clientes_a_eliminar)    
        centros.pop(max_cover)#Se elimina el centro utilizado para recalcular con los restantes     
        centros=generar_matriz(clientes_a_eliminar,centros)#Creo nuevamente la matriz de cobertura con los clientes y centros restantes
        clientes = list(filter(lambda x: x not in clientes_a_eliminar, clientes))#Los nuevos clientes a servir son los clientes totales menos los clientes servidos
        print("\n")
    return centros_utilizados
        



if __name__ == "__main__":
    clientes=[0,1,2,3,4,5,6]
    centros={
        1:[1,0,0,0,0,0,0],
        2:[1,1,1,0,0,0,0],
        3:[0,0,0,0,1,1,0],
        4:[0,0,0,0,0,0,1]
        }
    solucion=set_cover(centros,clientes)
    print(solucion)
    
    
    