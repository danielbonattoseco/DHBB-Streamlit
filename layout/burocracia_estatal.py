import streamlit as st
import datetime
from utils.formatar_data import formatar_data

def add_burocracia_estatal():
    st.session_state.burocraciasEstatais.append({
        'cargoNomeado' : '',
        'orgao' : '',
        'dataNomeacao' : {'dia':'',
                         'mes':'',
                         'ano':'',
                         'data':''},
        'exonerado' : False
    })

def add_conteiner_burocracia_estatal(i, burocracia_estatal):
    st.caption(f"Trajetória na Burocracia Estatal {i+1}")
            
    col1, col2 = st.columns(2)
    with col1:
        burocracia_estatal['cargoNomeado'] = st.text_input("Cargo nomeado", 
                                                    value=burocracia_estatal['cargoNomeado'],
                                                    help='Cargo para o qual o verbetado foi nomeado.',
                                                    key=f'burocraciaEstatal{i}cargoNomeado')
        
        st.markdown("""<div class="seletor_data">Data de nomeação</div>""",
                    unsafe_allow_html=True,
                  help="Data em que o político verbetado foi nomeado ao cargo (**DIA/MÊS/ANO**).  \nInsira todas as informações que possuir (apenas ano, mês/ano ou dia/mês/ano).  \nPara as informações que não possuir, deixar os campos em branco.")
        
        with st.container():
            col3,col4,col5 = st.columns([0.7,0.7,1])
            with col3:
                options = range(1,32)
                burocracia_estatal['dataNomeacao']['dia'] = st.selectbox("Dia", 
                                                            options,
                                                            index=options.index(burocracia_estatal['dataNomeacao']['dia'])
                                                            if burocracia_estatal['dataNomeacao']['dia']
                                                            in options
                                                            else None,
                                                            label_visibility="collapsed",
                                                            key=f"burocraciaEstatal{i}diaNomeacao")
            with col4:
                options = range(1,13)
                burocracia_estatal['dataNomeacao']['mes'] = st.selectbox("Mes", 
                            options,
                            index=options.index(burocracia_estatal['dataNomeacao']['mes'])
                            if burocracia_estatal['dataNomeacao']['mes']
                            in options
                            else None,
                            label_visibility="collapsed",
                            key=f"burocraciaEstatal{i}mesNomeacao")
            with col5:
                options = range(1900, datetime.date.today().year+1)
                burocracia_estatal['dataNomeacao']['ano'] = st.selectbox("Ano", 
                        options,
                        index=options.index(burocracia_estatal['dataNomeacao']['ano'])
                        if burocracia_estatal['dataNomeacao']['ano']
                        in options
                        else None,
                        label_visibility="collapsed",
                        key=f"burocraciaEstatal{i}anoNomeacao")
                
            burocracia_estatal['dataNomeacao']['data']  = formatar_data(burocracia_estatal['dataNomeacao']['ano'],
                                                                         burocracia_estatal['dataNomeacao']['mes'],
                                                                         burocracia_estatal['dataNomeacao']['dia'])

        
        burocracia_estatal['exonerado'] = st.checkbox("Exonerado?", 
                                        value = True if burocracia_estatal['exonerado'] else False,
                                        help="Marque esta opção caso o candidato tenha sido exonerado do cargo em exercício.",
                                        key=f"burocraciaEstatal{i}exonerado")

        
    with col2:
        burocracia_estatal['orgao'] = st.text_input("Órgão", 
                                                    value=burocracia_estatal['orgao'],
                                                    help='Órgão ao qual o verbetado foi vinculado no exercício de seu cargo.',
                                                    key=f'burocraciaEstatal{i}orgao')
            
    if st.session_state[f"burocraciaEstatal{i}exonerado"]:
        
        st.session_state.burocraciasEstatais[i].update({'exoneracaoData' : {'dia':'',
                                                                             'mes':'',
                                                                             'ano':'',
                                                                             'data':''},
                                                         'exoneracaoMotivo' : ''
        })
        
        col1, col2 = st.columns(2)
        
        with col1:
            
            st.markdown("""<div class="seletor_data">Data de exoneração </div>""",
                        unsafe_allow_html=True,
                      help="Data em que o político verbetado foi exnonerado do cargo (**DIA/MÊS/ANO**).  \nInsira todas as informações que possuir (apenas ano, mês/ano ou dia/mês/ano).  \nPara as informações que não possuir, deixar os campos em branco.")

            with st.container():
                col3,col4,col5 = st.columns([0.7,0.7,1])
                with col3:
                    options = range(1,32)
                    burocracia_estatal['exoneracaoData']['dia'] = st.selectbox("Dia", 
                                options,
                                index=options.index(burocracia_estatal['exoneracaoData']['dia'])
                                if burocracia_estatal['exoneracaoData']['dia']
                                in options
                                else None,
                                label_visibility="collapsed",
                                key=f"burocraciaEstatal{i}diaExoneracao")
                with col4:
                    options = range(1,13)
                    burocracia_estatal['exoneracaoData']['mes'] = st.selectbox("Mes", 
                                options,
                                index=options.index(burocracia_estatal['exoneracaoData']['mes'])
                                if burocracia_estatal['exoneracaoData']['mes']
                                in options
                                else None,
                                label_visibility="collapsed",
                                key=f"burocraciaEstatal{i}mesExoneracao")
                with col5:
                    options = range(1900, datetime.date.today().year+1)
                    burocracia_estatal['exoneracaoData']['ano'] = st.selectbox("Ano", 
                            options,
                            index=options.index(burocracia_estatal['exoneracaoData']['ano'])
                            if burocracia_estatal['exoneracaoData']['ano']
                            in options
                            else None,
                            label_visibility="collapsed",
                            key=f"burocraciaEstatal{i}anoExoneracao")
                    
                burocracia_estatal['exoneracaoData']['data']  = formatar_data(burocracia_estatal['exoneracaoData']['ano'],
                                                                              burocracia_estatal['exoneracaoData']['mes'],
                                                                              burocracia_estatal['exoneracaoData']['dia'])
                
        with col2:
            burocracia_estatal['exoneracaoMotivo'] = st.text_input("Motivo da exoneração", 
                                                        value=burocracia_estatal['exoneracaoMotivo'],
                                                        help='Motivo conhecido da exoneração do verbetado do cargo.',
                                                        key=f'burocraciaEstatal{i}exoneracaoMotivo')
            
    else:
        for j in ['exoneracaoData',
                  'exoneracaoMotivo']:
            if j in burocracia_estatal:
                if f"burocraciaEstatal{i}{j}" in st.session_state:
                    del st.session_state[f"burocraciaEstatal{i}{j}"]
                del burocracia_estatal[j]

    st.button(":red[Deletar Trajetória na Burocracia Estatal]", 
              on_click=delete_burocracia_estatal,
              args=(i,),
              key=f"deleteBurocraciaEstatal{i}")

# Função para deletar um subconteiner específico
def delete_burocracia_estatal(i):
    if 'burocraciasEstatais' in st.session_state and 0 <= i < len(st.session_state.burocraciasEstatais):
        st.session_state.burocraciasEstatais.pop(i)
