import streamlit as st
import utils.ontologia_parentela

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
                                                        utils.ontologia_parentela.feminina()
                                                        if st.session_state.genero == 'Feminino' 
                                                        else utils.ontologia_parentela.masculina(),
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
