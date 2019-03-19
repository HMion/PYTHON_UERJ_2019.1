A=3 #coeficiente que acompanha x²
B=-4 #coeficiente que acompanha x
C=-10 #coeficiente

y1=(-B+(((B**2)-4*A*C)**0.5))/2*A
y2=(-B-(((B**2)-4*A*C)**0.5))/2*A

print('As raízes da equação -3x²-4x-10 são: {:.2f} e {:.2f}.'.format(y1,y2))
