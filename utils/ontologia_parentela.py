def masculina():
    with open('dicts/ontologia_parentela_masculina.txt', 'r') as f:
        masculina = [line.strip() for line in f]
        
    return masculina
        
def feminina():
    with open('dicts/ontologia_parentela_feminina.txt', 'r') as f:
        feminina = [line.strip() for line in f]
        
    return feminina