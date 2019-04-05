def velocidade(So,S,t):
    if t==0:
     print('O tempo não pode ser zero!')
    else:
     v=(S-So)/t #fórmula usada paracalcular a velocidade.
     print(v)
    return(v)

################################################################
a=velocidade(2,5,2)

print('A velocidade para So=2m, S=5m e t=2s é:', a,' m/s.')
