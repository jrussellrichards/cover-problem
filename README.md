# cover-problem

Una empresa plantea la ubicación de centros de distribución para dar servicios a sus clientes, que residen en 30 ciudades diferentes. Es posible ubicar almacenes en cualquiera de las 30 ciudades. El objetivo de la empresa es otorgar un servicio que no exceda los 15 minutos desde que se recibe el pedido hasta que el producto llega a su punto de destino. Se ha realizado un estudio de tiempos de servicio en función de los puntos de origen y destino. Tiempo necesario para servir desde Ci a Cj se presenta en la matriz:

-- Matriz en código: 1 representa la posibilidad de realizar el servicio y 0 la imposibilidad de hacerlo--

1- Proponer un método de solución

Algoritmo:

1- Ubicar el centro que cubre la mayor cantidad de ciudades
2- Instalar el centro detectado en el paso 1
3- Borrar del listado las ciudades cubiertas por el centro. Si aún quedan ciudades sin cubrir volver al paso 1

2- Proponer una mejora a la heurística planteada

Mejora:

1-Seleccionar las ciudades que son servidas por la menor cantidad de almacenes
2-Seleccionar los almacenes que satisfacen esas ciudades
3-Instalar el almacen que satisface la mayor cantidad de ciudades
4-Borrar del listado las ciudades cubiertas por el centro. Si aún quedan ciudades sin cubrir volver al paso 1
