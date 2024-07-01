def formatar_data(ano, mes, dia):
    if not dia and not mes and not ano:
        data = ""
    elif ano and not mes:
        data = str(ano)
    elif mes and ano and not dia:
        data = f"{mes}/{ano}"
    elif dia and mes and ano:
        data = f"{dia}/{mes}/{ano}"
    else:
        data = ""  # Caso não se encaixe em nenhum dos casos anteriores
    
    return data