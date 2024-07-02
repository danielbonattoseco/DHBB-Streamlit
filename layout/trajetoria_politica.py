import streamlit as st
import datetime
from utils.formatar_data import formatar_data
from utils.partidos_politicos import partidos_politicos
from utils.legislaturas import legislaturas

def add_trajetoria_politica():
    st.session_state.trajetorias_politicas.append({
        'cargo' : '',
        'data_pleito' : '',
        'partido' : '',
        'votos' : '',
        'eleito' : False
    })

def add_conteiner_trajetoria_politica(i, trajetoria_politica):
    st.caption(f"Trajetória Política {i+1}")
            
    col1, col2 = st.columns(2)
    with col1:
        trajetoria_politica['cargo'] = st.text_input("Cargo", 
                                                    value=trajetoria_politica['cargo'],
                                                    help="Cargo ao qual o político verbetado se candidatou.",
                                                    key=f'trajetoria_politica_{i}_cargo')
        
        trajetoria_politica['partido'] = st.selectbox("Partido",
                                                      partidos_politicos(),
                                                      index=None,
                                                      help="Partido pelo qual o político verbetado se candidatou.",
                                                      key=f'trajetoria_politica_{i}_partido')
        
        trajetoria_politica['eleito'] = st.checkbox("Foi eleito para o cargo?", 
                                        help="Marque esta opção caso o candidato tenha sido eleito para o cargo disputado.",
                                        key=f"trajetoria_politica_{i}_eleito")

        
    with col2:
        st.markdown("""<div class="seletor_data">Data do pleito</div>""",
                    unsafe_allow_html=True,
                  help="Data em que o político verbetado se candidatou ao cargo (**DIA/MÊS/ANO**).  \nInsira todas as informações que possuir (apenas ano, mês/ano ou dia/mês/ano).  \nPara as informações que não possuir, deixar os campos em branco.")
        
        with st.container():
            col1,col2,col3 = st.columns([0.7,0.7,1])
            with col1:
                dia = st.selectbox("Dia", 
                            range(1,32),
                            index=None,
                            label_visibility="collapsed",
                            key=f"trajetoria_politica_{i}_dia_pleito")
            with col2:
                mes = st.selectbox("Mes", 
                            range(1,13),
                            index=None,
                            label_visibility="collapsed",
                            key=f"trajetoria_politica_{i}_mes_pleito")
            with col3:
                ano = st.selectbox("Ano", 
                        range(1900, datetime.date.today().year+1),
                        index=None,
                        label_visibility="collapsed",
                        key=f"trajetoria_politica_{i}_ano_pleito")
                
            trajetoria_politica['data_pleito'] = formatar_data(ano,mes,dia)
            
        trajetoria_politica['votos'] = st.number_input("Votos",
                                                       min_value=0,
                                                       value=None,
                                                       format="%d",
                                                       help="Quantidade de votos que o verbetado recebeu na candidatura.",
                                                       key=f"trajetoria_politica_{i}_votos")
        
    if st.session_state[f"trajetoria_politica_{i}_eleito"]:
        
        st.session_state.trajetorias_politicas[i].update({'mandato' : '',
        'renuncia' : False
        })
        

        trajetoria_politica['mandato'] = st.selectbox("Mandato",
                                                    legislaturas(),
                                                    index=None,
                                                    help='Legislatura ou período em para o qual o político verbetado foi empossado.',
                                                    key=f'trajetoria_politica_{i}_legislatura')
                        
        trajetoria_politica['renuncia'] = st.checkbox("Renunciou ao cargo?", 
                                        help='Marque esta opçào caso o candidato tenha renunciado ao cargo durante o exercício do mandato.',
                                        key=f"trajetoria_politica_{i}_renuncia")
        
        if st.session_state[f"trajetoria_politica_{i}_renuncia"]:
            
            st.session_state.trajetorias_politicas[i].update({'renuncia_motivo' : '',
            'renuncia_data' : ''
            })
            
            col1,col2 = st.columns(2)
            with col1:
                trajetoria_politica['renuncia_motivo'] = st.text_input("Motivo da renúncia", 
                                                            value=trajetoria_politica['cargo'],
                                                            help='Motivo noticiado/alegado pelo verbetado para a renúncia ao cargo.',
                                                            key=f'trajetoria_politica_{i}_renuncia_motivo')
                
            with col2:
                st.markdown("""<div class="seletor_data">Data da renúncia</div>""",
                            unsafe_allow_html=True,
                          help="Data da renúncia do verbetado ao cargo (**DIA/MÊS/ANO**).  \nInsira todas as informações que possuir (apenas ano, mês/ano ou dia/mês/ano).  \nPara as informações que não possuir, deixar os campos em branco.")
                
                with st.container():
                    col3,col4,col5 = st.columns([0.7,0.7,1])
                    with col3:
                        dia = st.selectbox("Dia", 
                                    range(1,32),
                                    index=None,
                                    label_visibility="collapsed",
                                    key=f"trajetoria_politica_{i}_dia_renuncia")
                    with col4:
                        mes = st.selectbox("Mes", 
                                    range(1,13),
                                    index=None,
                                    label_visibility="collapsed",
                                    key=f"trajetoria_politica_{i}_mes_renuncia")
                    with col5:
                        ano = st.selectbox("Ano", 
                                range(1900, datetime.date.today().year+1),
                                index=None,
                                label_visibility="collapsed",
                                key=f"trajetoria_politica_{i}_ano_renuncia")
                        
                    trajetoria_politica['renuncia_data'] = formatar_data(ano,mes,dia)
                    
        else:
            for j in ['renuncia_motivo',
                      'renuncia_data',
                      'dia_renuncia',
                      'mes_renuncia',
                      'ano_renuncia']:
                if j in trajetoria_politica:
                    if f"trajetoria_politica_{i}_{j}" in st.session_state:
                        del st.session_state[f"trajetoria_politica_{i}_{j}"]
                    del trajetoria_politica[j]
            
    else:
        for j in ['mandato',
                  'renuncia',
                  'renuncia_motivo',
                  'renuncia_data',
                  'dia_renuncia',
                  'mes_renuncia',
                  'ano_renuncia']:
            if j in trajetoria_politica:
                if f"trajetoria_politica_{i}_{j}" in st.session_state:
                    del st.session_state[f"trajetoria_politica_{i}_{j}"]
                del trajetoria_politica[j]











