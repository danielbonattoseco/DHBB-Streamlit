import streamlit as st
import datetime
from utils.formatar_data import formatar_data

def add_processo_criminal():
    st.session_state.processosCriminais.append({
        'processo' : '',
        'codigoProcesso' : '',
        'motivoProcesso': '',
        'condenado':False
    })

def add_conteiner_processo_criminal(i, processo_criminal):
        
    st.caption(f"Processo Criminal {i+1}")
            
    col1, col2 = st.columns(2)
    with col1:
        processo_criminal['processo'] = st.text_input("Processo", 
                                                    value=processo_criminal['processo'],
                                                    help='Processo movido contra o verbetado.',
                                                    key=f'processoCriminal{i}processo')

        processo_criminal['motivoProcesso'] = st.text_input("Motivo do processo", 
                                                    value=processo_criminal['motivoProcesso'],
                                                    help='Motivo conhecido do processo movido contra o verbetado.',
                                                    key=f'processoCriminal{i}motivoProcesso')
        
        processo_criminal['condenado'] = st.checkbox("Condenado?", 
                                        value = True if processo_criminal['condenado'] else False,
                                        help="Marque esta opção caso o candidato tenha sido condenado no processo mencionado.",
                                        key=f"processoCriminal{i}condenado")
        
    with col2:
        
        processo_criminal['codigoProcesso'] = st.text_input("Código do processo", 
                                                    value=processo_criminal['codigoProcesso'],
                                                    help='Codigo do processo movido contra o verbetado.',
                                                    key=f'processoCriminal{i}codigoProcesso')


    if processo_criminal['condenado']:
        
        st.session_state.processosCriminais[i].update({'dataCondenacao' : {'dia':'',
                           'mes':'',
                           'ano':'',
                           'data':''}
        })

        ###SELETOR DE DATAS DINÂMICO###
        
        with col1:
            
            st.markdown("""<div class="seletor_data">Data de condenação</div>""",
                        unsafe_allow_html=True,
                      help="Data de condenação do verbetado no processo mencionado. (**DIA/MÊS/ANO**).  \nInsira todas as informações que possuir (apenas ano, mês/ano ou dia/mês/ano).  \nPara as informações que não possuir, deixar os campos em branco.")

            with st.container():
                col3,col4,col5 = st.columns([0.7,0.7,1])
                with col3:
                    options = range(1,32)
                    processo_criminal['dataCondenacao']['dia'] = st.selectbox("Dia", 
                                                                options,
                                                                index=options.index(processo_criminal['dataCondenacao']['dia'])
                                                                if processo_criminal['dataCondenacao']['dia']
                                                                in options
                                                                else None,
                                                                label_visibility="collapsed",
                                                                key=f"processoCriminal{i}diaCondenacao")
                with col4:
                    options = range(1,13)
                    processo_criminal['dataCondenacao']['mes'] = st.selectbox("Mes", 
                                options,
                                index=options.index(processo_criminal['dataCondenacao']['mes'])
                                if processo_criminal['dataCondenacao']['mes']
                                in options
                                else None,
                                label_visibility="collapsed",
                                key=f"processoCriminal{i}mesCondenacao")
                with col5:
                    options = range(1900, datetime.date.today().year+1)
                    processo_criminal['dataCondenacao']['ano'] = st.selectbox("Ano", 
                            options,
                            index=options.index(processo_criminal['dataCondenacao']['ano'])
                            if processo_criminal['dataCondenacao']['ano']
                            in options
                            else None,
                            label_visibility="collapsed",
                            key=f"processoCriminal{i}anoCondenacao")
                    
                processo_criminal['dataCondenacao']['data']  = formatar_data(processo_criminal['dataCondenacao']['ano'],
                                                                     processo_criminal['dataCondenacao']['mes'],
                                                                     processo_criminal['dataCondenacao']['dia'])
                ###SELETOR DE DATAS DINÂMICO###    

    else:
        for j in ['dataCondenacao',
                  'diaCondenacao',
                  'mesCondenacao',
                  'anoCondenacao']:
            if j in processo_criminal:
                del processo_criminal[j]
            if f"processoCriminal{i}{j}" in st.session_state:
                del st.session_state[f"processoCriminal{i}{j}"]

    st.button(":red[Deletar Processo Criminal]", 
              on_click=delete_processo_criminal,
              args=(i,),
              key=f"deleteProcessoCriminal{i}")

# Função para deletar um subconteiner específico
def delete_processo_criminal(i):
    if 'processosCriminais' in st.session_state and 0 <= i < len(st.session_state.processosCriminais):
        st.session_state.processosCriminais.pop(i)
