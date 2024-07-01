import streamlit as st
import datetime
from utils.estados_br import estados_br
from utils.get_municipios import get_municipios

def add_formacao_academica():
    st.session_state.formacoes_academicas.append({
        'tipo' : '',
        'curso' : '',
        'instituicao' : '',
        'uf' : '',
        'municipio' : '',
        'ano_inicio' : '',
        'ano_fim' : ''
    })

def add_conteiner_formacao_academica(i, formacao_academica):
    st.caption(f"Formação Acadêmica {i+1}")
            
    col1, col2, col3 = st.columns(3)
    with col1:
        formacao_academica['tipo'] = st.selectbox("Tipo", 
                                                    ['Ensino Fundamental','Ensino Médio','Graduação','Pós-Graduação','Especialização'],
                                                    index=None,
                                                    help="Tipo de formação realizada pelo verbetado.",
                                                    key=f'formacao_academica_{i}_tipo'
                                                    )
        
        formacao_academica['uf'] = st.selectbox("UF de nascimento", 
                                  list(estados_br().values()),
                                  index=None,
                                  help="Estado da instituição de ensino onde o verbetado concluiu a formação.",
                                  key=f"formacao_academica_{i}_uf")
        
        formacao_academica['ano_inicio'] = st.selectbox("Ano Início", 
                                        range(1900, datetime.date.today().year+1), 
                                        index=None,
                                        help="Ano de inicio da formação.",
                                        key=f"formacao_academica_{i}_ano_inicio")      

    with col2:
        formacao_academica['curso'] = st.text_input("Curso", 
                                                    value=formacao_academica['curso'],
                                                    help="Nome do curso realizado pelo verbetado.  \nExemplo: Administração de Empresas, Ciência Política, etc.",
                                                    key=f'formacao_academica_{i}_curso')
        
        formacao_academica['municipio'] = st.selectbox("Município", 
                                          get_municipios(formacao_academica['uf']),
                                          index=None,
                                          help="Município da instituição de ensino onde o verbetado concluiu a formação.",
                                          key=f"formacao_academica_{i}_municipio")

        formacao_academica['ano_fim'] = st.selectbox("Ano Fim", 
                                        range(1900, datetime.date.today().year), 
                                        index=None,
                                        help="Ano de conclusão da formação.",
                                        key=f"formacao_academica_{i}_ano_fim")      
        
    with col3:
        formacao_academica['instituicao'] = st.text_input("Instituição", 
                                                    value=formacao_academica['curso'],
                                                    help="Nome da instituição de ensino onde o verbetado concluiu a formação.  \nExemplo: Fundação Getúlio Vargas, Universidade Federal do Rio de Janeiro, etc.",
                                                    key=f'formacao_academica_{i}_instituicao')

    st.button(":red[Deletar Formação Acadêmica]", 
              on_click=delete_formacao_academica,
              args=(i,),
              key=f"delete_formacao_academica_{i}")

# Função para deletar um subconteiner específico
def delete_formacao_academica(i):
    if 'formacoes_academicas' in st.session_state and 0 <= i < len(st.session_state.formacoes_academicas):
        st.session_state.formacoes_academicas.pop(i)
