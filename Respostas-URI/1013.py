numero = input().split(' ')
numeroMaior  =  0
for i in range(3):
    
    if int(numero[i]) > numeroMaior:
        numeroMaior = int(numero[i])
print("%d eh o maior"%numeroMaior)