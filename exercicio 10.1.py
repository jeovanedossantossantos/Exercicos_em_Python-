Ponto1=input()
Ponto2=input()

Ponto1r = (Ponto1.split())
Ponto2r = (Ponto2.split())

xp1 = float(Ponto1r[0])
yp1 = float(Ponto1r[1])
xp2 = float(Ponto2r[0])
yp2 = float(Ponto2r[1])

distancia=(((xp2-xp1)**2)+((yp2-yp1)**2))**0.5

print("{:.4f}".format(distancia))
