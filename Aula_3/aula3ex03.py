import math
def angulo_zenital(altura,sombra):
    theta_zenital=math.degrees(math.atan(sombra/altura))
    return(theta_zenital)
######################################################
theta=angulo_zenital(5,0.5)
print('O ângulo zenital do Sol que incide sobre um poste de 5 metros de altura fazendo uma sombra de 50 cm é: {:.2f} graus.'.format(theta))