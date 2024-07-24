import streamlit as st
import datetime
from utils.formatar_data import formatar_data

def add_atuacao_imprensa():
    st.session_state.atuacoesImprensa.append({
        'nomeJornal' : '',
        'funcaoExercida' : '',
        'dataInicio' : {'dia':'',
                        'mes':'',
                        'ano':'',
                        'data':''},
        'dataFim' : {'dia':'',
                     'mes':'',
                     'ano':'',
                     'data':''}
    })

def add_conteiner_atuacao_imprensa(i, atuacao_imprensa):
        
    st.caption(f"Atuação na Imprensa {i+1}")
            
    col1, col2 = st.columns(2)
    with col1:
        atuacao_imprensa['nomeJornal'] = st.text_input("Nome do Jornal", 
                                                    value=atuacao_imprensa['nomeJornal'],
                                                    help="Nome do jornal/periódico ou afins em que o verbetado atuava.",
                                                    key=f'atuacaoImprensa{i}nomeJornal')
        
        ###SELETOR DE DATAS DINÂMICO###
        st.markdown("""<div class="seletor_data">Data de início</div>""",
                    unsafe_allow_html=True,
                  help="Data em que o verbetado iniciou as atividades na função. (**DIA/MÊS/ANO**).  \nInsira todas as informações que possuir (apenas ano, mês/ano ou dia/mês/ano).  \nPara as informações que não possuir, deixar os campos em branco.")
        
        with st.container():
            col3,col4,col5 = st.columns([0.7,0.7,1])
            with col3:
                options = range(1,32)
                atuacao_imprensa['dataInicio']['dia'] = st.selectbox("Dia", 
                                                                    options,
                                                                    index=options.index(atuacao_imprensa['dataInicio']['dia'])
                                                                    if atuacao_imprensa['dataInicio']['dia']
                                                                    in options
                                                                    else None,
                                                                    label_visibility="collapsed",
                                                                    key=f"atuacaoImprensa{i}diaInicio")
            with col4:
                options = range(1,13)
                atuacao_imprensa['dataInicio']['mes'] = st.selectbox("Mes", 
                            options,
                            index=options.index(atuacao_imprensa['dataInicio']['mes'])
                            if atuacao_imprensa['dataInicio']['mes']
                            in options
                            else None,
                            label_visibility="collapsed",
                            key=f"atuacaoImprensa{i}mesInicio")
            with col5:
                options = range(1900, datetime.date.today().year+1)
                atuacao_imprensa['dataInicio']['ano'] = st.selectbox("Ano", 
                        options,
                        index=options.index(atuacao_imprensa['dataInicio']['ano'])
                        if atuacao_imprensa['dataInicio']['ano']
                        in options
                        else None,
                        label_visibility="collapsed",
                        key=f"atuacaoImprensa{i}anoInicio")
                
            atuacao_imprensa['dataInicio']['data']  = formatar_data(atuacao_imprensa['dataInicio']['ano'],
                                                                    atuacao_imprensa['dataInicio']['mes'],
                                                                    atuacao_imprensa['dataInicio']['dia'])
            ###SELETOR DE DATAS DINÂMICO###

        
    with col2:
        atuacao_imprensa['funcaoExercida'] = st.text_input("Função Exercida", 
                                                    value=atuacao_imprensa['funcaoExercida'],
                                                    help="Função exercida pelo verbetado durante atuação no jornal/periódico ou afins relacionado.",
                                                    key=f'atuacaoImprensa{i}funcaoExercida')

        ###SELETOR DE DATAS DINÂMICO###
        st.markdown("""<div class="seletor_data">Data de encerramento</div>""",
                    unsafe_allow_html=True,
                  help="Data em que o verbetado finalizou as atividades na função. (**DIA/MÊS/ANO**).  \nInsira todas as informações que possuir (apenas ano, mês/ano ou dia/mês/ano).  \nPara as informações que não possuir, deixar os campos em branco.")
        
        with st.container():
            col3,col4,col5 = st.columns([0.7,0.7,1])
            with col3:
                options = range(1,32)
                atuacao_imprensa['dataFim']['dia'] = st.selectbox("Dia", 
                                                            options,
                                                            index=options.index(atuacao_imprensa['dataFim']['dia'])
                                                            if atuacao_imprensa['dataFim']['dia']
                                                            in options
                                                            else None,
                                                            label_visibility="collapsed",
                                                            key=f"atuacaoImprensa{i}diaFim")
            with col4:
                options = range(1,13)
                atuacao_imprensa['dataFim']['mes'] = st.selectbox("Mes", 
                            options,
                            index=options.index(atuacao_imprensa['dataFim']['mes'])
                            if atuacao_imprensa['dataFim']['mes']
                            in options
                            else None,
                            label_visibility="collapsed",
                            key=f"atuacaoImprensa{i}mesFim")
            with col5:
                options = range(1900, datetime.date.today().year+1)
                atuacao_imprensa['dataFim']['ano'] = st.selectbox("Ano", 
                        options,
                        index=options.index(atuacao_imprensa['dataFim']['ano'])
                        if atuacao_imprensa['dataFim']['ano']
                        in options
                        else None,
                        label_visibility="collapsed",
                        key=f"atuacaoImprensa{i}anoFim")
                
            atuacao_imprensa['dataFim']['data']  = formatar_data(atuacao_imprensa['dataFim']['ano'],
                                                                 atuacao_imprensa['dataFim']['mes'],
                                                                 atuacao_imprensa['dataFim']['dia'])
            ###SELETOR DE DATAS DINÂMICO###    


    st.button(":red[Deletar Atuação na Imprensa]", 
              on_click=delete_atuacao_imprensa,
              args=(i,),
              key=f"deleteAtuacaoImprensa{i}")
    

# Função para deletar um subconteiner específico
def delete_atuacao_imprensa(i):
    if 'atuacoesImprensa' in st.session_state and 0 <= i < len(st.session_state.atuacoesImprensa):
        st.session_state.atuacoesImprensa.pop(i)
