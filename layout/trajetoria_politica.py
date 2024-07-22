import streamlit as st
import datetime
from utils.formatar_data import formatar_data
from utils.partidos_politicos import partidos_politicos
from utils.legislaturas import legislaturas

def add_trajetoria_politica():
    st.session_state.trajetorias_politicas.append({
        'cargo' : '',
        'partido' : '',
        'votos' : '',
        'eleito' : False,
        'data_pleito' : {'dia':'',
                         'mes':'',
                         'ano':'',
                         'data':''}
    })
    
def add_conteiner_trajetoria_politica(i, trajetoria_politica):
    st.caption(f"Trajetória Política {i+1}")
            
    col1, col2 = st.columns(2)
    with col1:
        trajetoria_politica['cargo'] = st.text_input("Cargo", 
                                                    value=trajetoria_politica['cargo'],
                                                    help="Cargo ao qual o político verbetado se candidatou.",
                                                    key=f'trajetoria_politica_{i}_cargo')
        
        options = partidos_politicos()
        trajetoria_politica['partido'] = st.selectbox("Partido",
                                                      options,
                                                      index=options.index(trajetoria_politica['partido'])
                                                      if trajetoria_politica['partido'] 
                                                      in options
                                                      else None,
                                                      help="Partido pelo qual o político verbetado se candidatou.",
                                                      key=f'trajetoria_politica_{i}_partido')
        
        trajetoria_politica['eleito'] = st.checkbox("Foi eleito para o cargo?", 
                                        value = True if trajetoria_politica['eleito'] else False,
                                        help="Marque esta opção caso o candidato tenha sido eleito para o cargo disputado.",
                                        key=f"trajetoria_politica_{i}_eleito")

        
    with col2:
        st.markdown("""<div class="seletor_data">Data do pleito</div>""",
                    unsafe_allow_html=True,
                  help="Data em que o político verbetado se candidatou ao cargo (**DIA/MÊS/ANO**).  \nInsira todas as informações que possuir (apenas ano, mês/ano ou dia/mês/ano).  \nPara as informações que não possuir, deixar os campos em branco.")
        
        with st.container():
            col1,col2,col3 = st.columns([0.7,0.7,1])
            
            with col1:
                options = range(1,32)
                trajetoria_politica['data_pleito']['dia'] = st.selectbox("Dia", 
                            options,
                            index=options.index(trajetoria_politica['data_pleito']['dia'])
                                          if trajetoria_politica['data_pleito']['dia'] 
                                          in options
                                          else None,
                            label_visibility="collapsed",
                            key=f"trajetoria_politica_{i}_dia_pleito")
            with col2:
                options = range(1,13)
                trajetoria_politica['data_pleito']['mes'] = st.selectbox("Mes", 
                            options,
                            index=options.index(trajetoria_politica['data_pleito']['mes'])
                                          if trajetoria_politica['data_pleito']['mes'] 
                                          in options
                                          else None,
                            label_visibility="collapsed",
                            key=f"trajetoria_politica_{i}_mes_pleito")
            with col3:
                options = range(1900, datetime.date.today().year+1)
                trajetoria_politica['data_pleito']['ano'] = st.selectbox("Ano", 
                                           options,
                                           index=options.index(trajetoria_politica['data_pleito']['ano'])
                                           if trajetoria_politica['data_pleito']['ano'] 
                                           in options
                                           else None,
                        label_visibility="collapsed",
                        key=f"trajetoria_politica_{i}_ano_pleito")
                
            trajetoria_politica['data_pleito']['data'] = formatar_data(trajetoria_politica['data_pleito']['ano'],
                                                                       trajetoria_politica['data_pleito']['mes'],
                                                                       trajetoria_politica['data_pleito']['dia'])
            
        trajetoria_politica['votos'] = st.number_input("Votos",
                                                       min_value=0,
                                                       value=trajetoria_politica['votos'] if trajetoria_politica['votos'] else None,
                                                       format="%d",
                                                       help="Quantidade de votos que o verbetado recebeu na candidatura.",
                                                       key=f"trajetoria_politica_{i}_votos")
        
    if st.session_state[f"trajetoria_politica_{i}_eleito"]:
        
        st.session_state.trajetorias_politicas[i].update({'mandato' : '',
        'renuncia' : False
        })
        
        options = legislaturas()
        trajetoria_politica['mandato'] = st.selectbox("Mandato",
                                                    legislaturas(),
                                                    index=trajetoria_politica['mandato']
                                                    if trajetoria_politica['mandato'] 
                                                    in options
                                                    else None,
                                                    help='Legislatura ou período em para o qual o político verbetado foi empossado.',
                                                    key=f'trajetoria_politica_{i}_legislatura')
                        
        trajetoria_politica['renuncia'] = st.checkbox("Renunciou ao cargo?", 
                                                      value = True if trajetoria_politica['renuncia'] else False,
                                        help='Marque esta opçào caso o candidato tenha renunciado ao cargo durante o exercício do mandato.',
                                        key=f"trajetoria_politica_{i}_renuncia")
        
        if st.session_state[f"trajetoria_politica_{i}_renuncia"]:
            
            st.session_state.trajetorias_politicas[i].update({'renuncia_motivo' : '',
            'renuncia_data' : {'dia':'',
                               'mes':'',
                               'ano':'',
                               'data':''}
            })
            
            col1,col2 = st.columns(2)
            with col1:
                trajetoria_politica['renuncia_motivo'] = st.text_input("Motivo da renúncia", 
                                                            value=trajetoria_politica['renuncia_motivo'],
                                                            help='Motivo noticiado/alegado pelo verbetado para a renúncia ao cargo.',
                                                            key=f'trajetoria_politica_{i}_renuncia_motivo')
                
            with col2:
                st.markdown("""<div class="seletor_data">Data da renúncia</div>""",
                            unsafe_allow_html=True,
                          help="Data da renúncia do verbetado ao cargo (**DIA/MÊS/ANO**).  \nInsira todas as informações que possuir (apenas ano, mês/ano ou dia/mês/ano).  \nPara as informações que não possuir, deixar os campos em branco.")
                
                with st.container():
                    col3,col4,col5 = st.columns([0.7,0.7,1])
                    with col3:
                        options = range(1,32)
                        trajetoria_politica['renuncia_data']['dia'] = st.selectbox("Dia", 
                                    options,
                                    index=trajetoria_politica['renuncia_data']['dia']
                                    if trajetoria_politica['renuncia_data']['dia']
                                    in options
                                    else None,
                                    label_visibility="collapsed",
                                    key=f"trajetoria_politica_{i}_dia_renuncia")
                    with col4:
                        options = range(1,13)
                        trajetoria_politica['renuncia_data']['mes'] = st.selectbox("Mes", 
                                    options,
                                    index=trajetoria_politica['renuncia_data']['mes']
                                    if trajetoria_politica['renuncia_data']['mes']
                                    in options
                                    else None,
                                    label_visibility="collapsed",
                                    key=f"trajetoria_politica_{i}_mes_renuncia")
                    with col5:
                        options = range(1900, datetime.date.today().year+1)
                        trajetoria_politica['renuncia_data']['ano'] = st.selectbox("Ano", 
                                options,
                                index=trajetoria_politica['renuncia_data']['ano']
                                if trajetoria_politica['renuncia_data']['ano']
                                in options
                                else None,
                                label_visibility="collapsed",
                                key=f"trajetoria_politica_{i}_ano_renuncia")
                        
                    trajetoria_politica['renuncia_data']['data'] = formatar_data(trajetoria_politica['renuncia_data']['ano'],
                                                                                 trajetoria_politica['renuncia_data']['mes'],
                                                                                 trajetoria_politica['renuncia_data']['dia'])
                    
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

    st.button(":red[Deletar Trajetória Política]", 
              on_click=delete_trajetoria_politica,
              args=(i,),
              key=f"deleteTrajetoriaPolitica{i}")

# Função para deletar um subconteiner específico
def delete_trajetoria_politica(i):
    if 'trajetorias_politicas' in st.session_state and 0 <= i < len(st.session_state.trajetorias_politicas):
        st.session_state.trajetorias_politicas.pop(i)

