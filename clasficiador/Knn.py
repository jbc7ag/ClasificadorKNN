import math

class Knn:

    def euclideanDistance(instance1, instance2):
    	distance = 0
    	distance = pow(( int(instance2.x) - int(instance1.x)), 2) +  pow(int(instance2.y) - int(instance1.y), 2)
    	return math.sqrt(distance)

    def setObjectsDistance(items, itemCompare):
        itemsDistancia = []
        for item in items:
            item.distancia =Knn.euclideanDistance(item, itemCompare)
            itemsDistancia.append(item)
        return itemsDistancia
