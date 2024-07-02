def legislaturas():
    
    with open('./dicts/legislaturas.txt', 'r', encoding='UTF-8') as f:
        legislaturas = [line.strip() for line in f]
        return legislaturas