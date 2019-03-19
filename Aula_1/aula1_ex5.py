altura=1.73 #em m
massa=70 #em kg
altura_bebe=0.7 #em m
massa_bebe=11 #em kg

meu_IMC=massa/(altura**2)
IMC_bebe=massa_bebe/(altura_bebe**2)

print('O meu IMC é: {:.2f} e o IMC do bebê gorducho é: {:.2f}.'.format(meu_IMC,IMC_bebe))
