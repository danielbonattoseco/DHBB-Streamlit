import streamlit as st
import os
from streamlit_extras.stylable_container import stylable_container
import locale
from utils.redator_verbete import redator_verbete
from utils.filtro_metadados import filtro_metadados
import layout.identificacao_pessoal
import layout.parentela_politica
import layout.formacao_academica
import layout.trajetoria_politica
import layout.atuacao_legislativa
import layout.burocracia_estatal
import layout.atuacao_imprensa
import layout.obra_do_verbetado
import layout.obra_sobre_verbetado
import layout.processo_criminal
import layout.conjuge
import layout.fonte

### CONFIGURAÇÕES DE LAYOUT ###

locale.setlocale(locale.LC_ALL, 'pt_BR')

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
os.chdir(current_directory)

# WIDESCREEN
st.set_page_config(layout="wide",
                   page_title="Gerador de Verbetes DHBB/CPDOC",
                   page_icon="images/fgv-logo.ico")


st.markdown("""
        <style>
               .block-container {
                    padding-top: 4rem;
                    padding-bottom: 2rem;
                    padding-left: 2rem;
                    padding-right: 2rem;
                }
               .seletor_data {
                   padding-bottom: 0.3.rem;
                   font-size: 14px;
                   }
}
        </style>
        """, unsafe_allow_html=True)
        
# FORMATAÇÃO DE ESTILOS 
# st.markdown("""
#         <style>
#                .block-container {
#                     padding-top: 4rem;
#                     padding-bottom: 2rem;
#                     padding-left: 3rem;
#                     padding-right: 3rem;
#                 }
#                 [data-key="seletor_data"] {
#                     gap: 0.15rem;
#                 }
# }
#         </style>
#         """, unsafe_allow_html=True)

    
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
                 key='dicionarioVerbete')
    with col2:
        st.text_input("Autor do verbete", 
                        help="Nome civil do autor do verbete.",
                        key="nomeAutorVerbete")

#%% Identificação Pessoal
    with st.expander("**Identificação Pessoal**",
                     expanded=True):
        layout.identificacao_pessoal.add_conteiner_identificacao_pessoal()
        
#%% Parentela Política

    with st.expander("**Parentela Política**"):                

        # Inicializando a lista de subconteiners na primeira execução
        if 'parentelasPoliticas' not in st.session_state:
            st.session_state.parentelasPoliticas = []

        # Conteiner principal
        with st.container():
            
            if len(st.session_state.parentelasPoliticas) < 1:
                layout.parentela_politica.add_parentela_politica()
            
            # Exibindo todos os subconteiners
            for i, parentela_politica in enumerate(st.session_state.parentelasPoliticas):
                with st.container(border=1):
                    layout.parentela_politica.add_conteiner_parentela_politica(i, parentela_politica)

            # Botão para adicionar novos subconteiners
            st.button(":green[**+ Adicionar**]",
                      on_click=layout.parentela_politica.add_parentela_politica,
                      key=f"insertParentelaPolitica{i}")
                
#%% Formação Acadêmica  
    with st.expander("**Formação Acadêmica**"):
        # Inicializando a lista de subconteiners na primeira execução
        if 'formacoesAcademicas' not in st.session_state:
            st.session_state.formacoesAcademicas = []

        # Conteiner principal
        with st.container():
            
            if len(st.session_state.formacoesAcademicas) < 1:
                layout.formacao_academica.add_formacao_academica()
            
            # Exibindo todos os subconteiners
            for i, formacao_academica in enumerate(st.session_state.formacoesAcademicas):
                with st.container(border=1):
                    layout.formacao_academica.add_conteiner_formacao_academica(i, formacao_academica)

            # Botão para adicionar novos subconteiners
            st.button(":green[**+ Adicionar**]",
                      on_click=layout.formacao_academica.add_formacao_academica,
                      key=f"insertFormacaoAcademica{i}")

   
#%% Trajetória Política
    with st.expander("**Trajetória Política**"):
        if 'trajetoriasPoliticas' not in st.session_state:
            st.session_state.trajetoriasPoliticas = []

        # Conteiner principal
        with st.container():
            
            if len(st.session_state.trajetoriasPoliticas) < 1:
                layout.trajetoria_politica.add_trajetoria_politica()
                
            # Exibindo todos os subconteiners
            for i, trajetoria_politica in enumerate(st.session_state.trajetoriasPoliticas):
                with st.container(border=1):
                    layout.trajetoria_politica.add_conteiner_trajetoria_politica(i, trajetoria_politica)

            # Botão para adicionar novos subconteiners
            st.button(":green[**+ Adicionar**]",
                      on_click=layout.trajetoria_politica.add_trajetoria_politica,
                      key=f"insertTrajetoriaPolitica{i}")
    
#%% Atuação Legislativa
    with st.expander("**Atuação Legislativa**"):
        if 'atuacoesLegislativas' not in st.session_state:
            st.session_state.atuacoesLegislativas = []

        # Conteiner principal
        with st.container():
            
            if len(st.session_state.atuacoesLegislativas) < 1:
                layout.atuacao_legislativa.add_atuacao_legislativa()
            
            # Exibindo todos os subconteiners
            for i, atuacao_legislativa in enumerate(st.session_state.atuacoesLegislativas):
                with st.container(border=1):
                    layout.atuacao_legislativa.add_conteiner_atuacao_legislativa(i, atuacao_legislativa)

            # Botão para adicionar novos subconteiners
            st.button(":green[**+ Adicionar**]",
                      on_click=layout.atuacao_legislativa.add_atuacao_legislativa,
                      key=f"insertAtuacaoLegislativa{i}")
        
#%% Trajetória na Burocracia Estatal
    with st.expander("**Trajetória na Burocracia Estatal**"):
        if 'burocraciasEstatais' not in st.session_state:
            st.session_state.burocraciasEstatais = []

        # Conteiner principal
        with st.container():
            
            if len(st.session_state.burocraciasEstatais) < 1:
                layout.burocracia_estatal.add_burocracia_estatal()
            
            # Exibindo todos os subconteiners
            for i, burocracia_estatal in enumerate(st.session_state.burocraciasEstatais):
                with st.container(border=1):
                    layout.burocracia_estatal.add_conteiner_burocracia_estatal(i, burocracia_estatal)

            # Botão para adicionar novos subconteiners
            st.button(":green[**+ Adicionar**]",
                      on_click=layout.burocracia_estatal.add_burocracia_estatal,
                      key=f"insertBurocraciaEstatal{i}")
    
#%% Atuação na Imprensa
    with st.expander("**Atuação na Imprensa**"):
        if 'atuacoesImprensa' not in st.session_state:
            st.session_state.atuacoesImprensa = []

        # Conteiner principal
        with st.container():
            
            if len(st.session_state.atuacoesImprensa) < 1:
                layout.atuacao_imprensa.add_atuacao_imprensa()
            
            # Exibindo todos os subconteiners
            for i, atuacao_imprensa in enumerate(st.session_state.atuacoesImprensa):
                with st.container(border=1):
                    layout.atuacao_imprensa.add_conteiner_atuacao_imprensa(i, atuacao_imprensa)

            # Botão para adicionar novos subconteiners
            st.button(":green[**+ Adicionar**]",
                      on_click=layout.atuacao_imprensa.add_atuacao_imprensa,
                      key=f"insertAtuacaoImprensa{i}")

    
#%% Obras publicadas pelo verbetado
    with st.expander("**Obras publicadas pelo verbetado**"):
        if 'obrasDoVerbetado' not in st.session_state:
            st.session_state.obrasDoVerbetado = []

        # Conteiner principal
        with st.container():
            
            if len(st.session_state.obrasDoVerbetado) < 1:
                layout.obra_do_verbetado.add_obra_do_verbetado()
            
            # Exibindo todos os subconteiners
            for i, obra_do_verbetado in enumerate(st.session_state.obrasDoVerbetado):
                with st.container(border=1):
                    layout.obra_do_verbetado.add_conteiner_obra_do_verbetado(i, obra_do_verbetado)

            # Botão para adicionar novos subconteiners
            st.button(":green[**+ Adicionar**]",
                      on_click=layout.obra_do_verbetado.add_obra_do_verbetado,
                      key=f"insertObraDoVerbetado{i}")

       
#%% Obras publicadas sobre o verbetado
    with st.expander("**Obras publicadas sobre o verbetado**"):
        if 'obrasSobreVerbetado' not in st.session_state:
            st.session_state.obrasSobreVerbetado = []

        # Conteiner principal
        with st.container():
            
            if len(st.session_state.obrasSobreVerbetado) < 1:
                layout.obra_sobre_verbetado.add_obra_sobre_verbetado()
            
            # Exibindo todos os subconteiners
            for i, obra_sobre_verbetado in enumerate(st.session_state.obrasSobreVerbetado):
                with st.container(border=1):
                    layout.obra_sobre_verbetado.add_conteiner_obra_sobre_verbetado(i, obra_sobre_verbetado)

            # Botão para adicionar novos subconteiners
            st.button(":green[**+ Adicionar**]",
                      on_click=layout.obra_sobre_verbetado.add_obra_sobre_verbetado,
                      key=f"insertObraSobreVerbetado{i}")
    
#%% Processos Criminais Concluídos e Condenações
    with st.expander("**Processos Criminais Concluídos e Condenações**"):
        if 'processosCriminais' not in st.session_state:
            st.session_state.processosCriminais = []

        # Conteiner principal
        with st.container():
            
            if len(st.session_state.processosCriminais) < 1:
                layout.processo_criminal.add_processo_criminal()
            
            # Exibindo todos os subconteiners
            for i, processo_criminal in enumerate(st.session_state.processosCriminais):
                with st.container(border=1):
                    layout.processo_criminal.add_conteiner_processo_criminal(i, processo_criminal)

            # Botão para adicionar novos subconteiners
            st.button(":green[**+ Adicionar**]",
                      on_click=layout.processo_criminal.add_processo_criminal,
                      key=f"insertProcessoCriminal{i}")

    
#%% Cônjuges
    with st.expander("**Cônjuges**"):
        if 'conjuges' not in st.session_state:
            st.session_state.conjuges = []

        # Conteiner principal
        with st.container():
            
            if len(st.session_state.conjuges) < 1:
                layout.conjuge.add_conjuge()
            
            # Exibindo todos os subconteiners
            for i, conjuge in enumerate(st.session_state.conjuges):
                with st.container(border=1):
                    layout.conjuge.add_conteiner_conjuge(i, conjuge)

            # Botão para adicionar novos subconteiners
            st.button(":green[**+ Adicionar**]",
                      on_click=layout.conjuge.add_conjuge,
                      key=f"insertConjuge{i}")
        
#%% Fontes
    with st.expander("**Fontes**"):
        if 'fontes' not in st.session_state:
            st.session_state.fontes = []

        # Conteiner principal
        with st.container():
            
            if len(st.session_state.fontes) < 1:
                layout.fonte.add_fonte()
            
            # Exibindo todos os subconteiners
            for i, fonte in enumerate(st.session_state.fontes):
                with st.container(border=1):
                    layout.fonte.add_conteiner_fonte(i, fonte)

            # Botão para adicionar novos subconteiners
            st.button(":green[**+ Adicionar**]",
                      on_click=layout.fonte.add_fonte,
                      key=f"insertFonte{i}")
        

#%% TEXTO VERBETE

texto_verbete = redator_verbete()

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
    json_string = filtro_metadados(st.session_state)
    
    st.download_button(
    label="Download JSON",
    file_name="verbete_%s.json"%(st.session_state['nomeCivil'].replace(" ", "_")),
    mime="application/json",
    data=json_string,
    key="metadataDownloadButton",
)

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

    st.write(st.session_state)

    # st.header("Menu")
    # st.markdown("🖊 [Parte 1 - Informações Pessoais](#parte1)")
    # st.markdown("🖊 [Parte 2 - Parentela Política](#parte2)")
    # st.markdown("💬 [Preview do Verbete](#previewverbete)")
    