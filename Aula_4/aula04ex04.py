def Comparar_2(a,b):
    if a > b:
        print(a,"é maior que", b)
        t=[b,a]
        print(t)
    elif a < b:
        print(a,"é menor que", b)
        t=[a,b]
        print(t)
    else:
        print(a,"é igual a", b)
        t=[a]
        print(t)
###############################################################################
x=int(input("Entre com o valor do primeiro número:"))
y=int(input("Entre com o valor do segundo número:"))
Comparar_2(x,y)