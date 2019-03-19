distancia_km=10
tempo=43.5 #em minutos
distancia_milha=distancia_km/1.61
tempo_medio=tempo/distancia_milha
velocidade=distancia_milha/(tempo/60)

print('O tempo médio por milha é: {:.2f} minutos.'.format(tempo_medio))
print('A velocidade média é: {:.2f} milhas/hora.'.format(velocidade))
