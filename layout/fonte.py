import streamlit as st
import datetime
from utils.validate_dates import validate_dates

def add_fonte():
    st.session_state.fontes.append({
        'autor' : '',
        'titulo':'',
        'informacoesComplementares':'',
        'origem': '',
        })

def add_conteiner_fonte(i, fonte):
        
    st.caption(f"Fonte {i+1}")
            
    col1, col2 = st.columns(2)
    with col1:
        fonte['autor'] = st.text_input("Autor/Organização", 
                                        value=fonte['autor'],
                                        help='Autor ou organizador da fonte consultada.  \n(Ex: Nome de Autor(es) de artigo consultado, Portal da Câmara dos Deputados, Portal G1 de Notícias, etc.)',
                                        key=f'fonte{i}autor')
        
        fonte['informacoesComplementares'] = st.text_input("Informações Complementares", 
                                        value=fonte['informacoesComplementares'],
                                        help='Demais informações pertinentes à fonte consultada.',
                                        key=f'fonte{i}informacoesComplementares')
        
    with col2:
        fonte['titulo'] = st.text_input("Título", 
                                        value=fonte['titulo'],
                                        help='Título da página ou matéria da fonte consultada (Ex: Título de obra, bibliografia, artigo etc.)',
                                        key=f'fonte{i}titulo')
        
        options = ['Online','Offline']
        fonte['origem'] = st.radio('Origem',
                                   options,
                                   index=options.index(fonte['origem'])
                                   if fonte['origem']
                                   in options
                                   else None,
                                   horizontal=True,
                                   help="Informe se a fonte citada é de natureza Online (Ex: Site, Portal online de notícias etc.) ou Offline (Ex: Livro, Arquivo etc.)",
                                   key=f"fonte{i}origem")
        
    if fonte['origem'] == "Online":
        with st.container():
            col3, col4 = st.columns(2)
            st.session_state.fontes[i].update({'url':'',
                'dataAcesso' : ''
            })
    
            with col3:
                fonte['url'] = st.text_input("URL", 
                                                value=fonte['url'],
                                                help='URL da página ou matéria da fonte consultada.',
                                                key=f'fonte{i}url')
                
            with col4:
                fonte['dataAcesso'] = st.date_input("Data de acesso", 
                                format="DD-MM-YYYY", 
                                value=None,
                                max_value=datetime.date.today(),
                                min_value=datetime.datetime.strptime("01-01-1900", '%d-%m-%Y'),
                                help="Data de acesso da fonte citada.",
                                on_change=validate_dates,
                                key=f"fonte{i}dataAcesso")       
            
    else:
        for j in ['url',
                  'dataAcesso']:
            if j in fonte:
                del fonte[j]
            if f"fonte{i}{j}" in st.session_state:
                del st.session_state[f"fonte{i}{j}"]
        
    st.button(":red[Deletar Fonte]", 
              on_click=delete_fonte,
              args=(i,),
              key=f"deleteFonte{i}")
    
    
# Função para deletar um subconteiner específico
def delete_fonte(i):
    if 'fontes' in st.session_state and 0 <= i < len(st.session_state.fontes):
        st.session_state.fontes.pop(i)
