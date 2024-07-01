import streamlit as st
import datetime
from utils.formatar_data import formatar_data
from utils.partidos_politicos import partidos_politicos

def add_trajetoria_politica():
    st.session_state.trajetorias_politicas.append({
        'cargo' : '',
        'ano_pleito' : '',
        'partido' : '',
        'votos' : '',
        'eleito' : False,
        'mandato' : '',
        'ano_fim' : '',
        'renuncia' : False,
        'renuncia_motivo' : '',
        'renuncia_data' : ''
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
                
            trajetoria_politica['ano_pleito'] = formatar_data(ano,mes,dia)
            
        trajetoria_politica['votos'] = st.number_input("Votos",
                                                       min_value=0,
                                                       value=None,
                                                       format="%d",
                                                       help="Quantidade de votos que o verbetado recebeu na candidatura.",
                                                       key=f"trajetoria_politica_{i}_votos")

                


