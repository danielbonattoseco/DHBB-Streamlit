import requests
import streamlit as st
import json

# DICIONARIO DE CÓDIGOS DE MUNICÍPIOS
with open("dicts/estados_br.json") as f:
    estados_br = json.load(f)

@st.cache_data(ttl=3600)
def get_municipios_IBGE(sigla_estado):
    """Utiliza a API do IBGE para retornar a lista de municípios no campo correspondente
    do módulo a partir do estado selecionado na UI."""
    try:
        response = requests.get(f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{sigla_estado}/municipios')
        return response.json()
    except requests.exceptions.RequestException:
        return {}

def get_municipios(sigla_UF, *args):
    """Retorna para a UI a lista de municípios."""
    if sigla_UF:
        sigla_estado = {v: k for k, v in estados_br.items()}[sigla_UF]
    
        municipios = get_municipios_IBGE(sigla_estado)
        
        if municipios:
            return [municipio['nome'] for municipio in municipios]
        else:
            st.error("Erro ao buscar municípios.")
    
    else:
        return ''
