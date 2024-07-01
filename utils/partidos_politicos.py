def partidos_politicos():
    
    with open('./dicts/partidos.txt', 'r', encoding='UTF-8') as f:
        partidos_politicos = [line.strip() for line in f]
        return partidos_politicos