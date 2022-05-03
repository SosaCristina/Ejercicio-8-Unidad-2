class Conjunto:
    __Listanumeros=[]

    def __init__(self):
        self.__Listanumeros=[]

    def agregar (self,num):
        self.__Listanumeros.append(num)

    def obtenerLista (self):
        return self.__Listanumeros

    def __add__(self, otro):
        lista=self.__Listanumeros.copy()

        for i in range (len(otro.obtenerLista())):
            j=0
            while (j < len(self.__Listanumeros) and (self.__Listanumeros[j]!=otro.obtenerLista()[i])):
                j+=1
            if j>=len(self.__Listanumeros):
                lista.append(otro.obtenerLista()[i])
        print("UNION",lista)

    def __sub__(self, otro):
        lista=self.__Listanumeros.copy()
        for i in range (len(otro.obtenerLista())):
            j=0
            while (j < len(otro.obtenerLista()) and (self.__Listanumeros[j]!=otro.obtenerLista()[i])):
                j+=1
            if j<=len(otro.obtenerLista()):
                lista.pop(j)
        print("DIFERENCIA",lista)


    def __eq__(self, otro):
        if len(self.__Listanumeros) != len(otro.obtenerLista()):
            print("Los conjuntos son distintos")
        i=0
        bandera=True
        while (i < (len(otro.obtenerLista())) and (bandera==True)):
            j=0
            while (j< len(otro.obtenerLista()) and(self.__Listanumeros[j]!=otro.obtenerLista()[i])):
                j+=1


            if j>=len (otro.obtenerLista()):
                print("Los conjuntos son distintos")
                bandera=False
            i+=1

        if bandera==True:
            print("Los conjuntos son iguales")


