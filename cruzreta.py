print('Calculadora de posicao')
print("Digite a posição da camera 1 em seus respectivos eixos")
xc1 = float(input('Eixo x = '))
yc1 = float(input('Eixo y = '))
zc1 = float(input('Eixo z = '))
print(80*'\n')

print("Digite a posição da camera 2 em seus respectivos eixos")
xc2 = float(input('Eixo x = '))
yc2 = float(input('Eixo y = '))
zc2 = float(input('Eixo z = '))
print(80*'\n')

print("Digite a posição da projeção do objeto na camera 1 em seus respectivos eixos")
xp1 = float(input('Eixo x = '))
yp1 = float(input('Eixo y = '))
zp1 = float(input('Eixo z = '))
print(80*'\n')

print("Digite a posição da projeção do ojeto na camera 2 em seus respectivos eixos")
xp2 = float(input('Eixo x = '))
yp2 = float(input('Eixo y = '))
zp2 = float(input('Eixo z = '))
print(80*'\n')

#Cálculos
vetc1 = [(xc1), (yc1), (zc1)]
vetc2 = [(xc2), (yc2), (zc2)]
vetp1 = [(xp1), (yp1), (zp1)]
vetp2 = [(xp2), (yp2), (zp2)]

mr1xy = (vetp1[1] - vetc1[1]) / (vetp1[0] - vetc1[0])
mr1xz = (vetp1[2] - vetc1[2]) / (vetp1[0] - vetc1[0])
mr1zy = (vetp1[1] - vetc1[1]) / (vetp1[2] - vetc1[2])

mr2xy = (vetp2[1] - vetc2[1]) / (vetp2[0] - vetc2[0])
mr2xz = (vetp2[2] - vetc2[2]) / (vetp2[0] - vetc2[0])
mr2zy = (vetp2[1] - vetc2[1]) / (vetp2[2] - vetc2[2]) 

x1 = (yc2 + (mr1xy * xc1) - (mr2xy * xc2) - yc1) / (mr1xy - mr2xy)
x2 = (zc2 + (mr1xz * xc1) - (mr2xz * xc2) - zc1) / (mr1xz - mr2xz)
y1 = ((mr1xy * x1) - (mr1xy * xc1) + yc1)
z2 = (yc2 + (mr1zy * zc1) - (mr2zy * zc2) - yc1) / (mr1zy - mr2zy)
y2 = ((mr1zy * z2) - (mr1zy * zc1) + yc1)
z1 = ((mr1xz * x2) - (mr1xz * xc1) + zc1)

x = (x1 + x2)/2
y= (y1 + y2)/2
z= (z1 + z2)/2



#para calcular a precisão
print('Deseja calcular a precisao? (s/n)')
resp = input()
if resp == 's':
    print('Agora digite a posição real do objeto')
    xr = float(input('x ='))
    yr = float(input('y ='))
    zr = float(input('z ='))

    errox = xr - x
    erroy = yr - y
    erroz = zr - z

    abx = abs(errox)
    aby = abs(erroy)
    abz = abs(erroz)

    total = (abx + aby + abz) / 3

    print('O objeto esta na posicao: ('+ str(x) + ", " + str(y)+", " + str(z) + ")")
    print('\n')
    print('O erro em cada eixo é de:')
    print('X: ' + str(errox))
    print('Y: ' + str(erroy))
    print('Z: ' + str(erroz))
    print('\n')
    print('O erro absoluto é de:')
    print('X: ' + str(abx))
    print('Y: ' + str(aby))
    print('Z: ' + str(abz))
    print('\n')
    print('O erro total é de: ' + str(total))
else:
    print('O objeto esta na posicao: ('+ str(x) + ", " + str(y)+", " + str(z) + ")")

#plotando grafico
from turtle import onclick
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')
X = [xc2, x, xp2]
Y = [yc2, y, yp2]
Z = [zc1, z, zp1]

X2 = [xc2, x, xp2]
Y2 = [yc2, y, yp2]
Z2 = [zc2, z, zp2]

plt.plot(X, Y, Z)
plt.plot(X2, Y2, Z2)

plt.show()




