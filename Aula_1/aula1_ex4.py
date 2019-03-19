import math

altura=5 #em metros
sombra=0.5 #em metros
angulo_zenital=math.atan(sombra/altura)
print('O ângulo zenital é: {:.2f} radianos.'.format(angulo_zenital))