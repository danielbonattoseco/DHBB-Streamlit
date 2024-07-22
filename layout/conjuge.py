import streamlit as st

def add_conjuge():
    st.session_state.conjuges.append({
        'nome' : '',
        'filhos' : False,
    })

def add_conteiner_conjuge(i, conjuge):
    
    def add_filho_conjuge():
        conjuge['nomesFilhos'].append("")

    st.caption(f"Cônjuge {i+1}")
            
    conjuge['nome'] = st.text_input("Nome", 
                                    value=conjuge['nome'],
                                    help='Nome do cônjuge do verbetado.',
                                    key=f'conjuge{i}nome')
    
    conjuge['filhos'] = st.checkbox("Filhos?", 
                                    value = True if conjuge['filhos'] else False,
                                    help="Marque esta opção caso o verbetado tenha tido filho(s) com o cônjuge mencionado.",
                                    key=f"conjuge{i}filhos")
    
    if conjuge['filhos']:
        if 'nomesFilhos' not in conjuge:
            st.session_state.conjuges[i].update({'nomesFilhos' : [""]
            })
        
        for j in range(len(conjuge['nomesFilhos'])):
            conjuge['nomesFilhos'][j] = (st.text_input(f"Filho(a) {j+1}", 
                                                        value=conjuge['nomesFilhos'][j],
                                                        help="Nome do(a) filho(a) que o verbetado possui com o cônjuge mencionado.",
                                                        key=f'conjuge{i}filho{j}'))
    
        st.button(":orange[Adicionar Filho]", 
                  on_click=add_filho_conjuge,
                  key=f"addFilho{i}")

    st.button(":red[Deletar Conjuge]", 
              on_click=delete_conjuge,
              args=(i,),
              key=f"deleteConjuge{i}")
    

# Função para deletar um subconteiner específico
def delete_conjuge(i):
    if 'conjuges' in st.session_state and 0 <= i < len(st.session_state.conjuges):
        st.session_state.conjuges.pop(i)
