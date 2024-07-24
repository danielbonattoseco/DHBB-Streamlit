import streamlit as st
import datetime
from utils.formatar_data import formatar_data

def add_obra_do_verbetado():
    st.session_state.obrasDoVerbetado.append({
        'nomeObra' : '',
        'dataPublicacao' : {'dia':'',
                            'mes':'',
                            'ano':'',
                            'data':''},
    })

def add_conteiner_obra_do_verbetado(i, obra_do_verbetado):
        
    st.caption(f"Obra Escrita pelo Verbetado {i+1}")
            
    col1, col2 = st.columns(2)
    with col1:
        obra_do_verbetado['nomeObra'] = st.text_input("Nome da Obra", 
                                                    value=obra_do_verbetado['nomeObra'],
                                                    help='Nome da obra sobre o verbetado.',
                                                    key=f'obraDoVerbetado{i}nomeObra')
        
        
    with col2:
        ###SELETOR DE DATAS DINÂMICO###
        st.markdown("""<div class="seletor_data">Data de publicação</div>""",
                    unsafe_allow_html=True,
                  help="Data de publicação da obra relacionada. (**DIA/MÊS/ANO**).  \nInsira todas as informações que possuir (apenas ano, mês/ano ou dia/mês/ano).  \nPara as informações que não possuir, deixar os campos em branco.")
        
        with st.container():
            col3,col4,col5 = st.columns([0.7,0.7,1])
            with col3:
                options = range(1,32)
                obra_do_verbetado['dataPublicacao']['dia'] = st.selectbox("Dia", 
                                                            options,
                                                            index=options.index(obra_do_verbetado['dataPublicacao']['dia'])
                                                            if obra_do_verbetado['dataPublicacao']['dia']
                                                            in options
                                                            else None,
                                                            label_visibility="collapsed",
                                                            key=f"obraDoVerbetado{i}diaPublicacao")
            with col4:
                options = range(1,13)
                obra_do_verbetado['dataPublicacao']['mes'] = st.selectbox("Mes", 
                            options,
                            index=options.index(obra_do_verbetado['dataPublicacao']['mes'])
                            if obra_do_verbetado['dataPublicacao']['mes']
                            in options
                            else None,
                            label_visibility="collapsed",
                            key=f"obraDoVerbetado{i}mesPublicacao")
            with col5:
                options = range(1900, datetime.date.today().year+1)
                obra_do_verbetado['dataPublicacao']['ano'] = st.selectbox("Ano", 
                        options,
                        index=options.index(obra_do_verbetado['dataPublicacao']['ano'])
                        if obra_do_verbetado['dataPublicacao']['ano']
                        in options
                        else None,
                        label_visibility="collapsed",
                        key=f"obraDoVerbetado{i}anoPublicacao")
                
            obra_do_verbetado['dataPublicacao']['data']  = formatar_data(obra_do_verbetado['dataPublicacao']['ano'],
                                                                 obra_do_verbetado['dataPublicacao']['mes'],
                                                                 obra_do_verbetado['dataPublicacao']['dia'])
            ###SELETOR DE DATAS DINÂMICO###    


    st.button(":red[Deletar Obra Escrita pelo Verbetado]", 
              on_click=delete_obra_do_verbetado,
              args=(i,),
              key=f"deleteObraDoVerbetado{i}")
    

# Função para deletar um subconteiner específico
def delete_obra_do_verbetado(i):
    if 'obrasDoVerbetado' in st.session_state and 0 <= i < len(st.session_state.obrasDoVerbetado):
        st.session_state.obrasDoVerbetado.pop(i)
