def elementopar(lista):
    for elemento in lista:
        if elemento % 2 == 0:
            print(elemento)
##############################################################################
print("Para a lista =[1,2,3,4,5,6,7,8,9,10], os elementos pares são:")
elementopar([1,2,3,4,5,6,7,8,9,10])