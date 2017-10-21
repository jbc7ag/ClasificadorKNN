# ClasificadorKNN

## Descripcion
Mediante el algoritmo KNN o K vecinos mas cercanos, clasificaqueremos si el elemento dado pertenece a un grupo de animales (Actualmente entrenada solo con Perros y Gatos)


**Dato un dato clasificaremos si es un Perro o un Gato**

    clase Punto: X, Y , Distancia, Caracteristicas
    clase Caracteristicas: Clase (Gato o Perro), color, edad
	
  
**Algoritmo**

    Metodo para obtener distancia entre 2 Puntos
    Recibe, Punto1,Punto2
    Regresa, Distancia

    Metodo Puntos cercanos
    Recibe, Punto a evaluar, Matriz elementos, K,  donde  K = Es la cantidad de elementos cercanos
    Regresa arreglo los K puntos mas cercanos
