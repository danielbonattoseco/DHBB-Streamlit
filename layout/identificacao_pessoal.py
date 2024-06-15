import streamlit as st
import datetime
from utils.validate_dates import validate_dates
from utils.estados_br import estados_br
from utils.get_municipios import get_municipios

def add_conteiner_identificacao_pessoal():
    col1,col2 = st.columns(2)
    with col1:
        st.text_input("Nome civil", 
                        help="Nome completo no registro civil oficial do verbetado.",
                        key="nome_civil")
        st.text_input("Nome social",
                      help="Nome que o político verbetado adotou para adequar a sua identidade referenciando o nome que o representa.",
                      key="nome_social")
        
    with col2:
        st.selectbox("Gênero", 
                     ['Masculino','Feminino'],
                     index=None,
                     help='Gênero do verbetado',
                     key="genero")
        st.text_input("Nome político",
                      help="Nome político/fantasia pelo qual o verbetado é conhecido na política.",
                      key="nome_politico")

        
    with st.container():
        col3,col4,col5 = st.columns(3)
        with col3:
            st.date_input("Data de nascimento", 
                            format="DD-MM-YYYY", 
                            value=None,
                            max_value=datetime.date.today(),
                            min_value=datetime.datetime.strptime("01-01-1900", '%d-%m-%Y'),
                            help="Data de nascimento do verbetado.",
                            on_change=validate_dates,
                            key="data_nascimento")                
        with col4:
            st.selectbox("UF de nascimento", 
                          list(estados_br()),
                          index=None,
                          help="Estado da federação onde o verbetado nasceu.",
                          key="uf_nascimento")
        
        with col5:
            st.selectbox("Município de nascimento", 
                          get_municipios(st.session_state.uf_nascimento),
                          index=None,
                          help="Município da federação onde o verbetado nasceu.  \n:gray-background[(selecione a UF de nascimento para habilitar este campo)]",
                          key="mun_nascimento")

    col7,col8 = st.columns(2)
    with col7:
        st.text_input("Nome do pai", 
                        help="Nome civil do pai do verbetado.",
                        key="nome_pai")
        st.text_input("Nome da mãe", 
                        help="Nome civil da mãe do verbetado.",
                        key="nome_mae")
        
        st.checkbox("Falecido(a)?", 
                        help="Marque esta opção caso o verbetado já tenha falecido.",
                        key="falecido")
        
    if st.session_state.falecido:
        with st.container():
            col4,col5,col6 = st.columns(3)
            with col4:
                st.date_input("Data de falecimento", 
                                format="DD-MM-YYYY", 
                                value=None,
                                max_value=datetime.date.today(),
                                min_value=datetime.datetime.strptime("01-01-1900", '%d-%m-%Y'),
                                help="Data de falecimento do verbetado.",
                                on_change=validate_dates,
                                key="data_falecimento")
                st.checkbox("Causa da morte conhecida?", 
                                help="Marque esta opção caso a causa da morte do verbetado seja conhecida.",
                                key="causa_morte_conhecida")
                
            with col5:
                st.selectbox("UF de falecimento", 
                             list(estados_br.values()),
                             index=None,
                             help="Estado da federação onde o verbetado faleceu.",
                             key="uf_falecimento")
            with col6:
                st.selectbox("Município de falecimento", 
                             get_municipios(st.session_state.uf_falecimento),
                             index=None,
                             help="Município da federação onde o verbetado faleceu.  \n:gray-background[(selecione a UF de falecimento para habilitar este campo)]",
                            key="mun_falecimento")

    with col8:
        st.text_input("Profissão do pai",
                      help="Profissão principal exercida pelo pai do verbetado.",
                      key="profissao_pai")
        st.text_input("Profissão da mae",
                      help="Profissão principal exercida pela mãe do verbetado.",
                      key="profissao_mae")
    
    if "causa_morte_conhecida" not in st.session_state: 
        st.session_state['causa_morte_conhecida'] = False
    if st.session_state['falecido'] == False:
        st.session_state['causa_morte_conhecida'] = False
    
    if st.session_state.causa_morte_conhecida:
        st.text_input(
            "Causa da morte",
            help="Causa da morte conhecida. Exemplo: Causa natural, suicídio...  \n(Esta informação não integra o corpo do verbete, sendo armazenada apenas como um metadado)",
            key="causa_morte"
        )