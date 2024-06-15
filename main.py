import streamlit as st
import datetime
import json
import os
from streamlit_extras.stylable_container import stylable_container
import locale
from utils.get_municipios import get_municipios

### CONFIGURAÇÕES DE LAYOUT ###

locale.setlocale(locale.LC_ALL, 'pt_BR')

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
                    padding-top: 4rem;
                    padding-bottom: 2rem;
                    padding-left: 3rem;
                    padding-right: 3rem;
                }
}
        </style>
        """, unsafe_allow_html=True)


#%% FUNÇÕES

### CONSTRUTOR LAYOUT - IDENTIFICACAO PESSOAL ###
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
                          list(estados_br.values()),
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

### CONSTRUTOR LAYOUT - PARENTELA POLITICA ###

def add_parentela_politica():
    # if 'parentelas_politicas' not in st.session_state:
    #     st.session_state.parentelas_politicas = []
    st.session_state.parentelas_politicas.append({
        'nome' : '',
        'parentesco' : '',
        'verbetado' : '',
        'cargos' : [""]
    })

def add_conteiner_parentela_politica(i, parentela_politica):
    def add_cargo_parentela_politica():
        st.session_state.qtdcargos+=1
        parentela_politica['cargos'].append("")
        
    st.caption(f"Parente Político {i+1}")
    
    if 'qtdcargos' not in st.session_state:
        st.session_state.qtdcargos = 1
        
    col1, col2 = st.columns([1, 1])
    with col1:
        parentela_politica['nome'] = st.text_input("Nome", 
                                                    value=parentela_politica['nome'],
                                                    help="Nome civil do parente político do verbetado.",
                                                    key=f'parente_politico_{i}_nome')
        
        parentela_politica['verbetado'] = st.checkbox("Verbetado(a) no DHBB?", 
                        help="Ative caso o parente do político verbetado mencionado possua um verbete ativo no DHBB.",
                        key=f'parente_politico_{i}_verbetado')


    with col2:
        parentela_politica['parentesco'] = st.selectbox("Parentesco", 
                                                        onto_parentela_fem 
                                                        if st.session_state.genero == 'Feminino' 
                                                        else onto_parentela_masc,
                                                        index=None,
                                                        help="Tipo de parentesco que o verbetado possui com o parente político.",
                                                        key=f'parente_politico_{i}_parentesco'
                                                        )
        
    st.warning('CARGOS BUGADO')
    for j in range(st.session_state.qtdcargos):
        parentela_politica['cargos'][j] = (st.text_input(f"Cargo {j+1}", 
                                                    value=parentela_politica['cargos'][j],
                                                    help="Cargo ocupado pelo parente político do verbetado.",
                                                    key=f'parente_politico_{i}_cargo_{j}'))
    

    st.button(":orange[Adicionar Cargo]", 
              on_click=add_cargo_parentela_politica,
              key=f"add_cargo_{i}")

    st.button(":red[Deletar Parente Político]", 
              on_click=delete_parentela_politica,
              args=(i,),
              key=f"delete_{i}")
    


# Função para deletar um subconteiner específico
def delete_parentela_politica(i):
    if 'parentelas_politicas' in st.session_state and 0 <= i < len(st.session_state.parentelas_politicas):
        st.session_state.parentelas_politicas.pop(i)

### CONSTRUTOR LAYOUT - X ###

def validate_dates():
    """Valida os campos de data para impedir que datas impossíveis sejam inseridas."""

    if "data_nascimento" not in st.session_state: 
        st.session_state['data_nascimento'] = None
    if "data_falecimento" not in st.session_state: 
        st.session_state['data_falecimento'] = None
    if isinstance(st.session_state.data_nascimento, datetime.date) and isinstance(st.session_state.data_falecimento, datetime.date):
        if st.session_state.data_nascimento >= st.session_state.data_falecimento:
            st.toast("A data de falecimento não pode ser menor que a data de nascimento.", icon="⚠️")
            st.session_state['data_falecimento'] = None
        
#%% CARREGAMENTO DE DADOS

with open("dicts/estados_br.json") as f:
    estados_br = json.load(f)

onto_parentela_masc = ['afilhado', 'avô', 'bisavô', 'bisneto', 'companheiro', 'cunhado', 'enteado', 'esposo', 'ex-esposo', 'filho', 'genro', 'herdeiro', 'irmão', 'meio-irmão', 'neto', 'noivo', 'padrasto', 'padrinho', 'pai', 'primo', 'sobrinho', 'sobrinho-neto', 'sogro', 'tataravô', 'tio', 'tio-avô', 'viúvo']
onto_parentela_fem = ['afilhada', 'avó', 'bisavó', 'bisneta', 'companheira', 'cunhada', 'enteada', 'esposa', 'ex-esposa', 'filha', 'nora', 'herdeira', 'irmã', 'meia-irmã', 'neta', 'noiva', 'madrasta', 'madrinha', 'mãe', 'prima', 'sobrinha', 'sobrinha-neta', 'sogra', 'tataravó', 'tia', 'tia-avó', 'viúva']

#%% CONSTRUÇÃO 

# IMAGEM CPDOC
st.image('.streamlit/thumbnails/cpdoc-logo.png', caption=None, width=200, clamp=False, channels="RGB", output_format="auto")

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
        add_conteiner_identificacao_pessoal()
        
#%% Parentela Política

    with st.expander("**Parentela Política**"):                

        # Inicializando a lista de subconteiners na primeira execução
        if 'parentelas_politicas' not in st.session_state:
            st.session_state.parentelas_politicas = []

        # Conteiner principal
        with st.container():
            
            if len(st.session_state.parentelas_politicas) < 1:
                add_parentela_politica()
            
            # Exibindo todos os subconteiners
            for i, parentela_politica in enumerate(st.session_state.parentelas_politicas):
                with st.container(border=1):
                    add_conteiner_parentela_politica(i, parentela_politica)

            # Botão para adicionar novos subconteiners
            st.button(":green[**+ Adicionar**]",
                      on_click=add_parentela_politica,
                      key=f"insert_{i}")
                

#%% Formação Acadêmica  
    with st.expander("**Formação Acadêmica**"):
        st.write("Em breve! :eyes:")
   
#%% Trajetória Política
    with st.expander("**Trajetória Política**"):
        st.write("Em breve! :eyes:")
    
#%% Atuação Legislativa
    with st.expander("**Atuação Legislativa**"):
        st.write("Em breve! :eyes:")
        
#%% Trajetória na Burocracia Estatal
    with st.expander("**Trajetória na Burocracia Estatal**"):
        st.write("Em breve! :eyes:")
    
#%% Atuação na Imprensa
    with st.expander("**Atuação na Imprensa**"):
        st.write("Em breve! :eyes:")
    
#%% Obras publicadas pelo verbetado
    with st.expander("**Obras publicadas pelo verbetado**"):
        st.write("Em breve! :eyes:")
       
#%% Obras publicadas sobre o verbetado
    with st.expander("**Obras publicadas sobre o verbetado**"):
        st.write("Em breve! :eyes:")
    
#%% Processos Criminais Concluídos e Condenações
    with st.expander("**Processos Criminais Concluídos e Condenações**"):
        st.write("Em breve! :eyes:")
    
#%% Cônjuges
    with st.expander("**Cônjuges**"):
        st.write("Em breve! :eyes:")
        
#%% Fontes
    with st.expander("**Fontes**"):
        st.write("Em breve! :eyes:")
        
#%% TEXTO VERBETE
#################
#################
#################
#################
#################
#################
#################


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

#%% Introdução
paragrafo_introducao = f"«{st.session_state['nome_civil'].title()}»" \
    + (' nasceu' 
           if st.session_state['data_nascimento']
           or st.session_state['mun_nascimento']
           else '') \
    + ((f' em {st.session_state["mun_nascimento"]}' 
      + ' (' 
      + list(estados_br.keys())[list(estados_br.values()).index(st.session_state['uf_nascimento'])] 
      + ')') 
         if st.session_state['uf_nascimento']
         and st.session_state['mun_nascimento']
         else '') \
    + (" em" + \
    (' %s de'%(st.session_state['data_nascimento'].day)) \
    + (' %s de'%(st.session_state['data_nascimento'].strftime("%B"))) \
    + (' %s'%(st.session_state['data_nascimento'].year)) 
        if st.session_state['data_nascimento']
        else '') \
    + ((f", filh{'a' if st.session_state['genero'] == 'Feminino' else 'o'} de " +
        (f"{st.session_state['nome_mae']}" if st.session_state['nome_mae'] else '')  +
        (', ' +
        st.session_state['profissao_mae'] 
        if st.session_state['profissao_mae']
        and st.session_state['nome_mae']
        else '') +
       (' e ' if st.session_state['nome_mae']
       and st.session_state['nome_pai']
       else '') + 
       (f"{st.session_state['nome_pai'] if st.session_state['nome_pai'] else ''}"))
       if st.session_state['nome_mae']
       or st.session_state['nome_pai']
       else '') + \
        (', ' +
        st.session_state['profissao_pai'] 
        if st.session_state['profissao_pai']
        and st.session_state['nome_pai']
        else '') \
    + '. '

if paragrafo_introducao:
    texto_verbete += paragrafo_introducao

#%% Falecimento    

if 'mun_falecimento' not in st.session_state:
    st.session_state['mun_falecimento'] = ''
if "data_falecimento" not in st.session_state:
    st.session_state['data_falecimento'] = ''
if st.session_state['data_falecimento'] or st.session_state['mun_falecimento']:            
    paragrafo_falecimento = " Faleceu em" \
    + (' %s de'%(st.session_state['data_falecimento'].day)) \
    + (' %s de'%(st.session_state['data_falecimento'].strftime("%B"))) \
    + (' %s'%(st.session_state['data_falecimento'].year)) \
    + ((f' em {st.session_state["mun_falecimento"]}' 
      + ' (' 
      + list(estados_br.keys())[list(estados_br.values()).index(st.session_state['uf_falecimento'])]
      + ')') 
     if st.session_state['uf_falecimento']
     and st.session_state['mun_falecimento']
     else '') \
    + '. '
else:
    paragrafo_falecimento = ''

if paragrafo_falecimento:
    texto_verbete += paragrafo_falecimento

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
    