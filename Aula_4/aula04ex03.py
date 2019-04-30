def Comparar(a,b):
    if a > b:
        print(a,"é maior que", b)
        return(a)
    elif a < b:
        print(a,"é menor que", b)
        return(b)
    else:
        print(a,"é igual a", b)
        return(a)
###############################################################################
x=int(input("Entre com o valor do primeiro número:"))
y=int(input("Entre com o valor do segundo número:"))
print(Comparar(x,y))