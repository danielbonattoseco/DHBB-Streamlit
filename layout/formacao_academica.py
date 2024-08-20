import streamlit as st
import datetime
from utils.estados_br import estados_br
from utils.get_municipios import get_municipios

def add_formacao_academica():
    st.session_state.formacoesAcademicas.append({
        'tipo' : '',
        'curso' : '',
        'instituicao' : '',
        'uf' : '',
        'municipio' : '',
        'anoInicio' : '',
        'anoFim' : ''
    })

def add_conteiner_formacao_academica(i, formacao_academica):
    st.caption(f"Formação Acadêmica {i+1}")
            
    col1, col2, col3 = st.columns(3)
    with col1:
        options = ['Ensino Fundamental','Ensino Médio','Graduação','Pós-Graduação','Especialização']
        formacao_academica['tipo'] = st.selectbox("Tipo", 
                                                    options,
                                                    index=options.index(formacao_academica['tipo'])
                                                    if formacao_academica['tipo'] 
                                                    in options
                                                    else None,
                                                    help="Tipo de formação realizada pelo verbetado.",
                                                    key=f'formacaoAcademica{i}tipo'
                                                    )

        options = list(estados_br().values())        
        formacao_academica['uf'] = st.selectbox("UF de formação", 
                                  options,
                                  index=options.index(formacao_academica['uf'])
                                  if formacao_academica['uf'] 
                                  in options
                                  else None,
                                  help="Estado da instituição de ensino onde o verbetado concluiu a formação.",
                                  key=f"formacaoAcademica{i}uf")

        options = range(1900, datetime.date.today().year+1)             
        formacao_academica['anoInicio'] = st.selectbox("Ano Início", 
                                        options, 
                                        index=options.index(formacao_academica['anoInicio'])
                                        if formacao_academica['anoInicio'] 
                                        in options
                                        else None,
                                        help="Ano de inicio da formação.",
                                        key=f"formacaoAcademica{i}anoInicio")      

    with col2:
        formacao_academica['curso'] = st.text_input("Curso", 
                                                    value=formacao_academica['curso'],
                                                    help="Nome do curso realizado pelo verbetado.  \nExemplo: Administração de Empresas, Ciência Política, etc.",
                                                    key=f'formacaoAcademica{i}Curso')
        
        options = get_municipios(formacao_academica['uf'])
        formacao_academica['municipio'] = st.selectbox("Município", 
                                          options,
                                          index=options.index(formacao_academica['municipio'])
                                          if formacao_academica['municipio'] 
                                          in options
                                          else None,
                                          help="Município da instituição de ensino onde o verbetado concluiu a formação.",
                                          key=f"formacaoAcademica{i}Municipio")

        options = range(1900, datetime.date.today().year)
        formacao_academica['anoFim'] = st.selectbox("Ano Fim", 
                                        options, 
                                        index=options.index(formacao_academica['anoFim'])
                                        if formacao_academica['anoFim'] 
                                        in options
                                        else None,                                        
                                        help="Ano de conclusão da formação.",
                                        key=f"formacaoAcademica{i}anoFim")      
        
    with col3:
        formacao_academica['instituicao'] = st.text_input("Instituição", 
                                                    value=formacao_academica['instituicao'],
                                                    help="Nome da instituição de ensino onde o verbetado concluiu a formação.  \nExemplo: Fundação Getúlio Vargas, Universidade Federal do Rio de Janeiro, etc.",
                                                    key=f'formacaoAcademica{i}instituicao')

    st.button(":red[Deletar Formação Acadêmica]", 
              on_click=delete_formacao_academica,
              args=(i,),
              key=f"deleteFormacaoAcademica{i}")

# Função para deletar um subconteiner específico
def delete_formacao_academica(i):
    if 'formacoesAcademicas' in st.session_state and 0 <= i < len(st.session_state.formacoesAcademicas):
        st.session_state.formacoesAcademicas.pop(i)
