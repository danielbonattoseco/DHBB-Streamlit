import json

def filtro_metadados(session_state):
    def reorder_keys(data, order):
        return {key: data[key] for key in order if key in data}
    
    # Mantenha os dados como dicionário, não como string
    json_data = {k: v for k, v in session_state.items()}
    
    key_order = ["nomeCivil", "nomeSocial", "nomePolitico", "genero", "dataNascimento",
                 "ufNascimento", "munNascimento", "nomePai", "profissaoPai", "nomeMae", 
                 "profissaoMae", "falecido", "dataFalecimento", "causaMorteConhecida", 
                 "ufFalecimento", "munFalecimento", "causaMorte", "parentelasPoliticas", 
                 "formacoesAcademicas", "trajetoriasPoliticas", "atuacoesLegislativas", 
                 "burocraciasEstatais", "atuacoesImprensa", "obrasDoVerbetado", 
                 "obrasSobreVerbetado", "processosCriminais", "conjuges", "fontes"]
    
    reordered_data = reorder_keys(json_data, key_order)
    
    new_json_data = json.dumps(reordered_data, ensure_ascii=False, indent=4)
    
    return new_json_data
