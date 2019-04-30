def Multiplicar(lista):
    x=1
    for elementos in lista:
        x *= elementos
    return(x)
##############################################################################

print(Multiplicar([2, 4, 5, 6, 10]))