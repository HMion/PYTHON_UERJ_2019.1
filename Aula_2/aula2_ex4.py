lambda_vermelho=632.8 #em nanômetros
distancia_D=1.98 #em metros
distancia_d=0.250 #em milímetros

delta_y=(lambda_vermelho*(10**(-9))*distancia_D)/(distancia_d*10**(-3))
print('A distancia Delta_y entre dois máximos consecutivos de interferência é de', delta_y, ' m.')
