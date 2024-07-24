import streamlit as st
import datetime
from utils.formatar_data import formatar_data
from utils.partidos_politicos import partidos_politicos
from utils.legislaturas import legislaturas

def add_trajetoria_politica():
    st.session_state.trajetoriasPoliticas.append({
        'cargo' : '',
        'partido' : '',
        'votos' : '',
        'eleito' : False,
        'dataPleito' : {'dia':'',
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
                                                    key=f'trajetoriaPolitica{i}cargo')
        
        options = partidos_politicos()
        trajetoria_politica['partido'] = st.selectbox("Partido",
                                                      options,
                                                      index=options.index(trajetoria_politica['partido'])
                                                      if trajetoria_politica['partido'] 
                                                      in options
                                                      else None,
                                                      help="Partido pelo qual o político verbetado se candidatou.",
                                                      key=f'trajetoriaPolitica{i}partido')
        
        trajetoria_politica['eleito'] = st.checkbox("Foi eleito para o cargo?", 
                                        value = True if trajetoria_politica['eleito'] else False,
                                        help="Marque esta opção caso o candidato tenha sido eleito para o cargo disputado.",
                                        key=f"trajetoriaPolitica{i}eleito")

        
    with col2:
        st.markdown("""<div class="seletor_data">Data do pleito</div>""",
                    unsafe_allow_html=True,
                  help="Data em que o político verbetado se candidatou ao cargo (**DIA/MÊS/ANO**).  \nInsira todas as informações que possuir (apenas ano, mês/ano ou dia/mês/ano).  \nPara as informações que não possuir, deixar os campos em branco.")
        
        with st.container():
            col1,col2,col3 = st.columns([0.7,0.7,1])
            
            with col1:
                options = range(1,32)
                trajetoria_politica['dataPleito']['dia'] = st.selectbox("Dia", 
                            options,
                            index=options.index(trajetoria_politica['dataPleito']['dia'])
                                          if trajetoria_politica['dataPleito']['dia'] 
                                          in options
                                          else None,
                            label_visibility="collapsed",
                            key=f"trajetoriaPolitica{i}diaPleito")
            with col2:
                options = range(1,13)
                trajetoria_politica['dataPleito']['mes'] = st.selectbox("Mes", 
                            options,
                            index=options.index(trajetoria_politica['dataPleito']['mes'])
                                          if trajetoria_politica['dataPleito']['mes'] 
                                          in options
                                          else None,
                            label_visibility="collapsed",
                            key=f"trajetoriaPolitica{i}mesPleito")
            with col3:
                options = range(1900, datetime.date.today().year+1)
                trajetoria_politica['dataPleito']['ano'] = st.selectbox("Ano", 
                                           options,
                                           index=options.index(trajetoria_politica['dataPleito']['ano'])
                                           if trajetoria_politica['dataPleito']['ano'] 
                                           in options
                                           else None,
                        label_visibility="collapsed",
                        key=f"trajetoriaPolitica{i}anoPleito")
                
            trajetoria_politica['dataPleito']['data'] = formatar_data(trajetoria_politica['dataPleito']['ano'],
                                                                       trajetoria_politica['dataPleito']['mes'],
                                                                       trajetoria_politica['dataPleito']['dia'])
            
        trajetoria_politica['votos'] = st.number_input("Votos",
                                                       min_value=0,
                                                       value=trajetoria_politica['votos'] if trajetoria_politica['votos'] else None,
                                                       format="%d",
                                                       help="Quantidade de votos que o verbetado recebeu na candidatura.",
                                                       key=f"trajetoriaPolitica{i}votos")
        
    if st.session_state[f"trajetoriaPolitica{i}eleito"]:
        
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
                                                    key=f'trajetoriaPolitica{i}legislatura')
                        
        trajetoria_politica['renuncia'] = st.checkbox("Renunciou ao cargo?", 
                                                      value = True if trajetoria_politica['renuncia'] else False,
                                        help='Marque esta opçào caso o candidato tenha renunciado ao cargo durante o exercício do mandato.',
                                        key=f"trajetoriaPolitica{i}renuncia")
        
        if st.session_state[f"trajetoriaPolitica{i}renuncia"]:
            
            st.session_state.trajetorias_politicas[i].update({'renunciaMotivo' : '',
            'renunciaData' : {'dia':'',
                               'mes':'',
                               'ano':'',
                               'data':''}
            })
            
            col1,col2 = st.columns(2)
            with col1:
                trajetoria_politica['renunciaMotivo'] = st.text_input("Motivo da renúncia", 
                                                            value=trajetoria_politica['renuncia_motivo'],
                                                            help='Motivo noticiado/alegado pelo verbetado para a renúncia ao cargo.',
                                                            key=f'trajetoriaPolitica{i}renunciaMotivo')
                
            with col2:
                st.markdown("""<div class="seletor_data">Data da renúncia</div>""",
                            unsafe_allow_html=True,
                          help="Data da renúncia do verbetado ao cargo (**DIA/MÊS/ANO**).  \nInsira todas as informações que possuir (apenas ano, mês/ano ou dia/mês/ano).  \nPara as informações que não possuir, deixar os campos em branco.")
                
                with st.container():
                    col3,col4,col5 = st.columns([0.7,0.7,1])
                    with col3:
                        options = range(1,32)
                        trajetoria_politica['renunciaData']['dia'] = st.selectbox("Dia", 
                                    options,
                                    index=trajetoria_politica['renunciaData']['dia']
                                    if trajetoria_politica['renunciaData']['dia']
                                    in options
                                    else None,
                                    label_visibility="collapsed",
                                    key=f"trajetoriaPolitica{i}diaRenuncia")
                    with col4:
                        options = range(1,13)
                        trajetoria_politica['renunciaData']['mes'] = st.selectbox("Mes", 
                                    options,
                                    index=trajetoria_politica['renunciaData']['mes']
                                    if trajetoria_politica['renunciaData']['mes']
                                    in options
                                    else None,
                                    label_visibility="collapsed",
                                    key=f"trajetoriaPolitica{i}mesRenuncia")
                    with col5:
                        options = range(1900, datetime.date.today().year+1)
                        trajetoria_politica['renunciaData']['ano'] = st.selectbox("Ano", 
                                options,
                                index=trajetoria_politica['renunciaData']['ano']
                                if trajetoria_politica['renunciaData']['ano']
                                in options
                                else None,
                                label_visibility="collapsed",
                                key=f"trajetoriaPolitica{i}anoRenuncia")
                        
                    trajetoria_politica['renunciaData']['data'] = formatar_data(trajetoria_politica['renunciaData']['ano'],
                                                                                 trajetoria_politica['renunciaData']['mes'],
                                                                                 trajetoria_politica['renunciaData']['dia'])
                    
        else:
            for j in ['renunciaMotivo',
                      'renunciaData',
                      'diaRenuncia',
                      'mesRenuncia',
                      'anoRenuncia']:
                if j in trajetoria_politica:
                    if f"trajetoriaPolitica{i}{j}" in st.session_state:
                        del st.session_state[f"trajetoriaPolitica{i}{j}"]
                    del trajetoria_politica[j]
            
    else:
        for j in ['mandato',
                  'renuncia',
                  'renunciaMotivo',
                  'renunciaData',
                  'diaRenuncia',
                  'mesRenuncia',
                  'anoRenuncia']:
            if j in trajetoria_politica:
                if f"trajetoriaPolitica{i}{j}" in st.session_state:
                    del st.session_state[f"trajetoriaPolitica{i}{j}"]
                del trajetoria_politica[j]

    st.button(":red[Deletar Trajetória Política]", 
              on_click=delete_trajetoria_politica,
              args=(i,),
              key=f"deleteTrajetoriaPolitica{i}")

# Função para deletar um subconteiner específico
def delete_trajetoria_politica(i):
    if 'trajetoriasPoliticas' in st.session_state and 0 <= i < len(st.session_state.trajetoriasPoliticas):
        st.session_state.trajetoriasPoliticas.pop(i)

