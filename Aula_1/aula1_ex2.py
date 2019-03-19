tempo=3 #segundos
velocidade_luz=3*(10**8) # m/s
velocidade_som=343 #m/s

distancia=((3*velocidade_som)/((velocidade_luz-velocidade_som)/velocidade_luz))/1000
print('A distância entre você e os fogos de artifício é de aproximadamente: {:.2f} km.'.format(distancia))
