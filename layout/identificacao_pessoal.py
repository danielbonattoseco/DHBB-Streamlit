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
                        key="nomeCivil")
        st.text_input("Nome social",
                      help="Nome que o político verbetado adotou para adequar a sua identidade referenciando o nome que o representa.",
                      key="nomeSocial")
        
    with col2:
        st.selectbox("Gênero", 
                     ['Masculino','Feminino'],
                     index=None,
                     help='Gênero do verbetado',
                     key="genero")
        st.text_input("Nome político",
                      help="Nome político/fantasia pelo qual o verbetado é conhecido na política.",
                      key="nomePolitico")

        
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
                            key="dataNascimento")                
        with col4:
            st.selectbox("UF de nascimento", 
                          list(estados_br().values()),
                          index=None,
                          help="Estado da federação onde o verbetado nasceu.",
                          key="ufNascimento")
        
        with col5:
            st.selectbox("Município de nascimento", 
                          get_municipios(st.session_state.ufNascimento),
                          index=None,
                          help="Município da federação onde o verbetado nasceu.  \n:gray-background[(selecione a UF de nascimento para habilitar este campo)]",
                          key="munNascimento")

    col7,col8 = st.columns(2)
    with col7:
        st.text_input("Nome do pai", 
                        help="Nome civil do pai do verbetado.",
                        key="nomePai")
        st.text_input("Nome da mãe", 
                        help="Nome civil da mãe do verbetado.",
                        key="nomeMae")
        
        st.checkbox("Falecido(a)?", 
                        help="Marque esta opção caso o verbetado já tenha falecido.",
                        key="falecido")
        
    with col8:
        st.text_input("Profissão do pai",
                      help="Profissão principal exercida pelo pai do verbetado.",
                      key="profissaoPai")
        st.text_input("Profissão da mae",
                      help="Profissão principal exercida pela mãe do verbetado.",
                      key="profissaoMae")


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
                                key="dataFalecimento")
                st.checkbox("Causa da morte conhecida?", 
                                help="Marque esta opção caso a causa da morte do verbetado seja conhecida.",
                                key="causaMorteConhecida")
                
            with col5:
                st.selectbox("UF de falecimento", 
                             list(estados_br().values()),
                             index=None,
                             help="Estado da federação onde o verbetado faleceu.",
                             key="ufFalecimento")
            with col6:
                st.selectbox("Município de falecimento", 
                             get_municipios(st.session_state.ufFalecimento),
                             index=None,
                             help="Município da federação onde o verbetado faleceu.  \n:gray-background[(selecione a UF de falecimento para habilitar este campo)]",
                            key="munFalecimento")
                
        if st.session_state.causaMorteConhecida:
            st.text_input(
                "Causa da morte",
                help="Causa da morte conhecida. Exemplo: Causa natural, suicídio...  \n(Esta informação não integra o corpo do verbete, sendo armazenada apenas como um metadado)",
                key="causaMorte"
            )
            
        else:
            if "causaMorte" in st.session_state:
                del st.session_state["causaMorte"]
            
    else:
        for j in ['dataFalecimento',
                  'causaMorteConhecida',
                  'ufFalecimento',
                  'munFalecimento',
                  'causaMorte']:
            if j in st.session_state:
                del st.session_state[j]
            
    