import streamlit as st

def add_atuacao_legislativa():
    st.session_state.atuacoes_legislativas.append({
        'nome' : '',
        'trajetoriaPoliticaRelacionada' : '',
        'tipo' : '',
        'casaLegislativa' : '',
        'funcao' : ''
    })

def add_conteiner_atuacao_legislativa(i, atuacao_legislativa):
    st.caption(f"Atuação Legislativa {i+1}")
            
    col1, col2 = st.columns(2)
    with col1:
        atuacao_legislativa['nome'] = st.text_input("Nome", 
                                                    value=atuacao_legislativa['nome'],
                                                    help='Nome da comissão em que o verbetado atuou.',
                                                    key=f'atuacaoLegislativa{i}Nome')
        
        options = ['Comissão Permanente',
        'Comissão Especial',
        'Comissão Externa',
        'Comissão Parlamentar de Inquérito (CPI)']
        atuacao_legislativa['tipo'] = st.selectbox("Tipo", 
                                                    options,
                                                    index=options.index(atuacao_legislativa['tipo'])
                                                    if atuacao_legislativa['tipo']
                                                    in options
                                                    else None,
                                                    help='Tipo de comissão em que o verbetado atuou.',
                                                    key=f'atuacaoLegislativa{i}Tipo'
                                                    )

        options = ['Presidente',
         'Membro titular']
        atuacao_legislativa['funcao'] = st.selectbox("Função", 
                                                        options,
                                                        index=options.index(atuacao_legislativa['funcao'])
                                                        if atuacao_legislativa['funcao']
                                                        in options
                                                        else None,
                                                        help='Função exercida pelo verbetado na comissão.',
                                                        key=f'atuacaoLegislativa{i}Funcao'
                                                        )

    with col2:
        options = [x['cargo'] + (
            f" ({x['mandato']})" 
            if x['mandato'] 
            is not None 
            else '')
        for x 
        in st.session_state.trajetorias_politicas
        if x['cargo'] != ''
        and x['eleito']]
        
        atuacao_legislativa['trajetoriaPoliticaRelacionada'] = st.selectbox("Trajetória Política Relacionada", 
                                                        options,
                                                        index=options.index(atuacao_legislativa['trajetoriaPoliticaRelacionada'])
                                                        if atuacao_legislativa['trajetoriaPoliticaRelacionada']
                                                        in options
                                                        else None,
                                                        help='Etapa da trajetória política do verbetado na qual exerceu a atuação legislativa.  \nA lista apresenta todas as experiências preenchidas na seção "Trajetória Política" onde o verbetado tenha sido identificado como **eleito**.',
                                                        key=f'atuacaoLegislativa{i}TrajetoriaPoliticaRelacionada'
                                                        )
        
        options = ['Câmara dos Deputados',
         'Senado Federal']
        atuacao_legislativa['casaLegislativa'] = st.selectbox("Casa Legislativa", 
                                                        options,
                                                        index=options.index(atuacao_legislativa['casaLegislativa'])
                                                        if atuacao_legislativa['casaLegislativa']
                                                        in options
                                                        else None,
                                                        help='Casa legislativa onde a comissão foi instaurada.',
                                                        key=f'atuacaoLegislativa{i}CasaLegislativa'
                                                        )

    st.button(":red[Deletar Atuação Legislativa]", 
              on_click=delete_atuacao_legislativa,
              args=(i,),
              key=f"deleteAtuacaoLegislativa{i}")


# Função para deletar um subconteiner específico
def delete_atuacao_legislativa(i):
    if 'atuacoes_legislativas' in st.session_state and 0 <= i < len(st.session_state.atuacoes_legislativas):
        st.session_state.atuacoes_legislativas.pop(i)
