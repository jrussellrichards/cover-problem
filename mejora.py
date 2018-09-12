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

def ciudad_menor_cobertura(centros):
    ciudades=[]
    min_count=999
    for ciudad in range(30):
        # print("ciudad",ciudad)
        count=0
        for centro in centros:
            if(centros[centro][ciudad] == 1):
                count+=1
        if(count<min_count and count!=0):
            min_count=count
            ciudades=[]
            ciudades.append(ciudad)
        elif(count == min_count):
            ciudades.append(ciudad)           

    centros_escogidos={}
    def verificar(ciudades_escogidas):  #funcion para escoger los centros que contienen a las ciudades con menor interseccion
        for centro in centros:
            seleccionado=0
            for ciudad in ciudades_escogidas:
                if(centros[centro][ciudad]==1):
                    seleccionado=1
            if(seleccionado==1):
                centros_escogidos[centro]=centros[centro]
    
    verificar(ciudades)


    # list(filter(lambda x: x not in clientes_a_eliminar, centros))
    # for ciudad in ciudades:
    #     centros_escogidos[ciudad+1]=centros[ciudad+1]
    
    return centros_escogidos
        


def set_cover(centros,clientes):
    centros_utilizados=[]
    # zeros=np.zeros(len(clientes))

    while(len(clientes) > 0 and len(centros) > 0): #Mientras queden clientes por servir o existan centros se ejecutará el prgorama
        # print("clientes a servir: ",clientes)
        # print("los centros actuales son: ",centros)
        ciudades_candidatas=ciudad_menor_cobertura(centros)
        # print("ciudades",ciudades_candidatas)
        
        max_cover=max(ciudades_candidatas,key = lambda i: covertura(centros[i])) #Se escoge el que tenga mayor cobertura
        # if(centros[max_cover]==list(zeros)): #Si el que estoy añadiendo no cubre ningun cliente, entonces detengo el programa
        #     break       
        centros_utilizados.append(max_cover) #Añado a mi solucion el centro escogido
        # print("El que cubre la mayor cantidad es",max_cover) 
        clientes_a_eliminar=clientes_servidos(centros[max_cover]) #Son los clientes que fueron servidor por el centro utilizado
        # print("Todos estos clientes fueron servidos",clientes_a_eliminar)    
        centros.pop(max_cover)#Se elimina el centro utilizado para recalcular con los restantes     
        centros=generar_matriz(clientes_a_eliminar,centros)#Creo nuevamente la matriz de cobertura con los clientes y centros restantes
        clientes = list(filter(lambda x: x not in clientes_a_eliminar, clientes))#Los nuevos clientes a servir son los clientes totales menos los clientes servidos
        # print("\n")
    return centros_utilizados
        



if __name__ == "__main__":
    clientes=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
    
	
    centros={
		1:[1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
        2:[0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
        3:[0,0,1,0,0,0,0,0,1,1,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0],
        4:[0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
        5:[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		6:[0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		7:[1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
		8:[0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0],
		9:[0,0,1,0,0,0,0,0,1,1,0,0,0,1,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,0],
	   10:[0,0,1,0,0,0,0,0,1,1,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0],
	   11:[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	   12:[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	   13:[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	   14:[0,1,1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0],
	   15:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
	   16:[0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,0],
	   17:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],
	   18:[0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
	   19:[0,0,1,0,0,0,0,0,1,1,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0],
	   20:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0],
	   21:[0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
	   22:[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
	   23:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
	   24:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],
	   25:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0],
	   26:[1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
	   27:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
	   28:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
	   29:[0,0,1,0,0,0,0,0,1,1,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0],
	   30:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1]

        }
    solucion=set_cover(centros,clientes)
    print("Los centros a utilizar son: ",solucion)
    # print(centros)
    # city=ciudad_menor_cobertura(centros)
    # print(city)
  