def divisores(valor):
    for i in range(1, valor//2+1):
        if valor % i == 0: 
            yield i
    yield valor
###############################################################################
def num_perfeito(num):
    x=list(divisores(num))
#    print(x)
#    print(sum(x))
#    print(sum(x)-num)
#    print(int(sum(x)/2))
    if num > 0:
        if sum(x)-num == num:
            if int(sum(x)/2) == num:
                print("Este é um número perfeito!")
            else:
                print("Este número não é um número perfeito!")
        else:
            print("Este número não é um número perfeito!")
    else:
        print("Digite um valor positivo!")
#    else:
#        print("Este não é um número perfeito!")
###############################################################################
x=int(input("Entre com o número a ser analisado:"))
num_perfeito(x)