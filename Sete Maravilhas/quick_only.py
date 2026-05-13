def quick_sort(lista, inicio, fim):
    if inicio >= fim:
        return
    
    # Escolhendo pivo
    pivo = lista[fim]
    
    # Loop de Separação
    area_menores = inicio - 1
    for valor in range(inicio, fim):
        if lista[valor] <= pivo:
            area_menores += 1
            lista[area_menores], lista[valor] = lista[valor], lista[area_menores]
            
    # Posicionando pivo
    lista[area_menores + 1], lista[fim] = lista[fim], lista[area_menores + 1]
    
    # Recursão
    quick_sort(lista, inicio, area_menores) # esquerda
    quick_sort(lista, area_menores + 2, fim) # direita
