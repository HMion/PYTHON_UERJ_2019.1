def verif_interv(mínimo, máximo, valor):
    if mínimo <= valor <= máximo:
        print("O valor digitado está dentro do intervalo escolhido!")
    else:
        print("O valor digitado NÃO está dentro do intervalo escolhido!")
###############################################################################
mínimo=int(input("Entre com o valor inferior do intervalo:"))
máximo=int(input("Entre com o valor superior do intervalo:"))
valor=int(input("Entre com o valor a ser analisado:"))
verif_interv(mínimo, máximo, valor)