import streamlit as st
import datetime
import json
import os
from streamlit_extras.stylable_container import stylable_container
import requests

### CONFIGURAÇÕES DE LAYOUT ###

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
os.chdir(current_directory)

# WIDESCREEN
st.set_page_config(layout="wide",
                   page_title="Gerador de Verbetes DHBB/CPDOC",
                   page_icon="images/fgv-logo.ico")

# FORMATAÇÃO DE ESTILOS 
st.markdown("""
        <style>
               .block-container {
                    padding-top: 2rem;
                    padding-bottom: 2rem;
                    padding-left: 3rem;
                    padding-right: 3rem;
                }
}
        </style>
        """, unsafe_allow_html=True)

#%% FUNÇÕES 
def create_anchor(anchor_id): #ÂNCORAS PARA O MENU LATERAL
    st.markdown(f'<a id="{anchor_id}"></a>', unsafe_allow_html=True)

def get_municipios(sigla_UF, *args):
    """Utiliza a API do IBGE para retornar a lista de municípios no campo correspondente
    do módulo a partir do estado selecionado na UI."""
    
    if sigla_UF is not None:
        sigla_estado = {v: k for k, v in estados_br.items()}[sigla_UF]
    
        response  = requests.get(
            'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{}/municipios'.format(
            sigla_estado
                )
            )
        
        municipios = response.json()
        return [municipio['nome'] for municipio in municipios]
    else:
        return ''

# Função para adicionar um novo subconteiner
def add_parentela_politica():
    if 'parentelas_politicas' not in st.session_state:
        st.session_state.parentelas_politicas = []
    index = len(st.session_state.parentelas_politicas)
    st.session_state.parentelas_politicas.append({
        'title': f"Parentela Política {index + 1}",
        'input1': '',
        'input2': ''
    })

# Função para deletar um subconteiner específico
def delete_parentela_politica(index):
    if 'parentelas_politicas' in st.session_state and 0 <= index < len(st.session_state.parentelas_politicas):
        st.session_state.parentelas_politicas.pop(index)

#%% CARREGAMENTO DE DADOS

with open("dicts/estados_br.json") as f:
    estados_br = json.load(f)



#%% CONSTRUÇÃO 

# IMAGEM CPDOC
st.image('.streamlit/thumbnails/cpdoc-logo.png', caption=None, width=200, clamp=False, channels="RGB", output_format="auto")

create_anchor("parte1") #ANCORA MENU LATERAL

# TITULO
st.subheader("Gerador de Verbetes 0.0.2")
    
tab_preenchimento,tab_preview,tab_metadados = st.tabs(["Preenchimento", 
                            "Preview do Verbete", 
                            "Metadados"])

# ÁREA DE PREENCHIMENTO
with tab_preenchimento:
    col1,col2 = st.columns([2,6])
    with col1:
        st.radio("Dicionário do Verbete",
                 ['DHBB','DHBPR'],
                 horizontal=True,
                 help="**DHBB** = Dicionário Histórico-Biográfico Brasileiro  \n**DHBPR** = Dicionário Histórico-Biográfico da Primeira República",
                 key='dicionario_verbete')
    with col2:
        st.text_input("Autor do verbete", 
                        help="Nome civil do autor do verbete.",
                        key="nome_autor_verbete")

#%% Identificação Pessoal
    with st.expander("**Identificação Pessoal**",
                     expanded=True):
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
                                max_value=datetime.date.today(),
                                min_value=datetime.datetime.strptime("01-01-1900", '%d-%m-%Y'),
                                help="Data de nascimento do verbetado.",
                                key="data_nascimento")                
            with col4:
                st.selectbox("UF de nascimento", 
                              list(estados_br.values()),
                              index=None,
                              help="Estado da federação onde o verbetado nasceu.",
                              key="uf_nascimento")
            
            with col5:
                st.selectbox("Município de nascimento", 
                              get_municipios(st.session_state.uf_nascimento),
                              index=None,
                              help="Município da federação onde o verbetado nasceu.  \nblue-background[selecione a UF de nascimento para habilitar o campo)]",
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
                                    max_value=datetime.date.today(),
                                    min_value=datetime.datetime.strptime("01-01-1900", '%d-%m-%Y'),
                                    help="Data de falecimento do verbetado.",
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
                                 help="Município da federação onde o verbetado faleceu.",
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

#%% Parentela Política
    with st.expander("**Parentela Política**"):
        st.write("Conteúdo de Parentela Política")   
   
#%% Formação Acadêmica  
    with st.expander("**Formação Acadêmica**"):
        st.write("Conteúdo de Dados do Verbete")
   
#%% Trajetória Política
    with st.expander("**Trajetória Política**"):
        st.write("Conteúdo de Identificação Pessoal")
    
#%% Atuação Legislativa
    with st.expander("**Atuação Legislativa**"):
        st.write("Conteúdo de Parentela Política")    
        
#%% Trajetória na Burocracia Estatal
    with st.expander("**Trajetória na Burocracia Estatal**"):
        st.write("Conteúdo de Dados do Verbete")
    
#%% Atuação na Imprensa
    with st.expander("**Atuação na Imprensa**"):
        st.write("Conteúdo de Identificação Pessoal")
    
#%% Obras publicadas pelo verbetado
    with st.expander("**Obras publicadas pelo verbetado**"):
        st.write("Conteúdo de Parentela Política")    
       
#%% Obras publicadas sobre o verbetado
    with st.expander("**Obras publicadas sobre o verbetado**"):
        st.write("Conteúdo de Dados do Verbete")
    
#%% Processos Criminais Concluídos e Condenações
    with st.expander("**Processos Criminais Concluídos e Condenações**"):
        st.write("Conteúdo de Identificação Pessoal")
    
#%% Cônjuges
    with st.expander("**Cônjuges**"):
        st.write("Conteúdo de Parentela Política")    
        
#%% Fontes
    with st.expander("**Fontes**"):
        st.write("Conteúdo de Parentela Política")    
        

create_anchor("parte2") #ANCORA MENU LATERAL
        

# Inicializando a lista de subconteiners na primeira execução
if 'parentelas_politicas' not in st.session_state:
    st.session_state.parentelas_politicas = []

# Conteiner principal
with st.container(border=1):
    st.caption("Parte 2 - Parentela Política")

    # Botão para adicionar novos subconteiners
    if st.button(":green[**+ Adicionar**]"):
        add_parentela_politica()

    # Exibindo todos os subconteiners
    for i, parentela_politica in enumerate(st.session_state.parentelas_politicas):
        with st.container(border=1):
            cols = st.columns([4, 0.4])
            with cols[0]:
                st.caption(parentela_politica['title'])
                parentela_politica['input1'] = st.text_input(f"Input 1 - {parentela_politica['title']}", value=parentela_politica['input1'])
                parentela_politica['input2'] = st.text_input(f"Input 2 - {parentela_politica['title']}", value=parentela_politica['input2'])
            with cols[1]:
                delete_button = st.button(":red[Deletar]", key=f"delete_{i}")
                if delete_button:
                    delete_parentela_politica(i)
                    st.rerun()  # Recarrega a página para refletir as mudanças

#%% TEXTO VERBETE

texto_verbete = ''

cabecalho = f"---\ntitle: {st.session_state['nome_civil'].split()[-1].upper() if st.session_state['nome_civil'] else ''}" \
            f"""{", " + ' '.join(word for word in st.session_state['nome_civil'].split()[:-1]) 
            if len(' '.join(word 
                            for word 
                            in st.session_state['nome_civil'].split()[:-1])) > 0 
            else ''}""" \
            f"\nnatureza: Biográfico" \
            f"""\nsexo: {st.session_state['genero'][0].lower() 
            if st.session_state['genero'] 
            in ['Feminino','Masculino'] 
            else ''}""" \
            f"\n---\n\n"

if cabecalho:
    texto_verbete += cabecalho

#%% ÁREA DE PREVIEW
with tab_preview:
    st.write("**Preview do Verbete:**")
    
    with stylable_container(
    "codeblock",
    """
    code {
        white-space: pre-wrap !important;
    }
    """,
    ):
        st.code(texto_verbete, 
            language="markdown", 
            line_numbers=True
        )

#%% ÁREA DE METADADOS

with tab_metadados:
    st.write(st.session_state)
    
#%% SIDEBAR

with st.sidebar:
    st.write("**Preview do Verbete:**")
    
    with stylable_container(
    "codeblock",
    """
    code {
        white-space: pre-wrap !important;
    }
    """,
    ):
        st.code(texto_verbete, 
            language="markdown", 
            line_numbers=True
        )

    # st.header("Menu")
    # st.markdown("🖊 [Parte 1 - Informações Pessoais](#parte1)")
    # st.markdown("🖊 [Parte 2 - Parentela Política](#parte2)")
    # st.markdown("💬 [Preview do Verbete](#previewverbete)")
    