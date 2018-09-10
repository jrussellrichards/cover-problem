# cover-problem

Una empresa plantea la ubicación de centros de distribución para dar servicios a sus clientes, que residen en 6 ciudades diferentes. Es posible ubicar almacenes en cualquiera de las 6 ciudades. El objetivo de la empresa es otorgar un servicio que no exceda los 15 minutos desde que se recibe el pedido hasta que el producto llega a su punto de destino. Se ha realizado un estudio de tiempos de servicio en función de los puntos de origen y destino. Tiempo necesario para servir desde Ci a Cj se presenta en la matriz:

-- Matriz--

1- Encontrar el número óptimo de almacenes y su localización de manera que se de el servicio deseado. 
2- Proponer un método de solución


Algoritmo:

1- Ubicar el centro que cubre la mayor cantidad de clientes
2- Instalar el centro detectado en el paso 1
3- Borrar del listado los clientes cubiertos del centro. Si aún quedan clientes volver al paso 1