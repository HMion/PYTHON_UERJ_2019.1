import math

def IMC(altura,massa):
    imc=massa/(altura**2)
    return(imc)

def Volume_esfera(raio):
    volume=(4/3)*math.pi*(raio**3)
    return(volume)

def Delta_y(comp_onda,D,d):
    delta_y=(comp_onda*(10**(-9))*D)/(d*10**(-3))
    return(delta_y)
###############################################################################
print("Entre com sua altura (m) e sua massa (kg):")
altura=float(input())
massa=float(input())
imc=IMC(altura,massa)
print("Seu IMC equivale a {:.2f}!".format(imc))

print("Agora, entre com o valor do raio, em metros, da esfera em questão:")
raio=float(input())
volume=Volume_esfera(raio)
print("O volume da esfera de raio {:.2f} metros é {:.2f} m³.".format(raio,volume))

print("Por fim, entre com o comprimento de onda, em nanometros, a distância D até o anteparo , em metros, e a distância d entre as fendas, em milímetros:")
comprimento_onda=float(input())
D=float(input())
d=float(input())
delta_y=Delta_y(comprimento_onda,D,d)
print("A distância entre dois maximos consegutivos para o comprimento de onda {:.2f} nanometros, distância D até o anteparo de {:.2f} metros e a distância d entre as fendas de {:.2f} milímetros equivale a {:.2f} metros".format(comprimento_onda,D,d,delta_y))