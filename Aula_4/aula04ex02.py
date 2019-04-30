def Fatorial(n):
    i=2
    x=1
    while n >= i:
       x=x*i
       i=i+1

    return(x)
###############################################################################
n = int(input("Digite o valor do número para calcular o fatorial: "))
fatorial = Fatorial(n)
print("O valor de %d! é =" %n, fatorial)