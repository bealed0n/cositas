def pascal(num):
    # Verifica
    if num == 0:
        return []
    elif num == 1:
        return [1]
    #Principal 
    else:
        NvaFila = [1]
        ultimaFila = pascal(num-1)
        for i in range(len(ultimaFila)-1):
            NvaFila.append(ultimaFila[i] + ultimaFila[i+1])
        NvaFila += [1]
    return NvaFila
    
#Numero de filas del triangulo
num = 9
# ciclo para generar triangulo
for i in range(num):
    print(pascal(i))
