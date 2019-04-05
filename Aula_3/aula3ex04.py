def metros_milhas(metro):
    milha=metro/1609.34 #conversao de metro para milha.
    return(milha)
############################################################################
def milhas_metros(milha):
    metro=milha*1609.34 #conversao de milhas para metro.
    return(metro)
############################################################################
milhas = metros_milhas(10000) #retorna o valor em milhas referente a 10Km.
print('10.000 m equivalem a: {:.2f} milhas.'.format(milhas))

metros = milhas_metros(10) #retorna o valor em metros referente a 10 milhas.
print('10 milhas equivalem a: {:.2f} metros.'.format(metros))

############################################################################
def horas_seg(horas):
    segundos = horas*3600 #conversao de horas para segundos.
    return(segundos)
############################################################################
def segundos_horas(segundos):
    horas = segundos/3600 #conversao de horas para segundos.
    return(horas)
############################################################################
    
segundos = horas_seg(48) #retorna o valor em segundos referente a 48h.
print('48h equivalem a {:.2f} segundos!'.format(segundos))

horas = segundos_horas(54000) #retorna o valor em horas referente a 54mil segundos.
print('54 mil segundos equivalem a {:.2f} horas!'.format(horas))

quilometros = milhas_metros(4)/1000
velocidade = quilometros/0.5
tempo_medio=30/quilometros
print('Uma pessoa que demora 30 minutos para correr 4 milhas tem velocidade de {:.2f} km/h'.format(velocidade))
print("O tempo médio por quilômetro do trajeto acima descrito equivale a {:.2f} minutos.".format(tempo_medio))