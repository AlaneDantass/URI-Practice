primeiro = input().split(' ')

x1 = float(primeiro[0])
y1 = float(primeiro[1])

segundo = input().split(' ')

x2 = float(segundo[0])
y2  = float(segundo[1])

distancia = (((x2-x1)**2)+((y2-y1)**2))**0.5

print('{:.4f}'.format(distancia))