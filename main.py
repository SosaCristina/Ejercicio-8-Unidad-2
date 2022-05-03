from ClaseConjunto import Conjunto

if __name__=="__main__":
    conjunto1=Conjunto()
    conjunto2=Conjunto()
    conjunto1.agregar(1)
    conjunto1.agregar(2)
    conjunto1.agregar(3)
    conjunto2.agregar(3)
    conjunto2.agregar(4)
    conjunto2.agregar(5)
    print(conjunto1.obtenerLista())
    print(conjunto2.obtenerLista())
    opcion= 0
    def menu():
        opc= int(input("Menu Principal\n" +
                      "1)Union de conjuntos (item 1)\n" +
                      "2)Diferencia de conjuntos (item 2)\n" +
                      "3)Verificar si dos conjuntos son iguales (item 3)\n" +
                      "4)Finalizar\n"+
                      "Elija una opcion\n"))
        return opc
    while opcion!=4:
        opcion=menu()
        if opcion == 1:

            C=conjunto1+conjunto2


        if opcion == 2:
            C=conjunto1-conjunto2

        if opcion == 3:
            conjunto1==conjunto2

