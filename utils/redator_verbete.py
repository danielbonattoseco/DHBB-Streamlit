import streamlit as st 
from utils.estados_br import estados_br

def redator_verbete():
    texto_verbete = ''
        
    ### CABEÇALHO DE METADADOS
    
    cabecalho = "---\ntitle: " \
    + (st.session_state['nomeCivil'].split()[-1].upper()
    if st.session_state['nomeCivil'] 
    else '') \
    + (", " + ' '.join(word for word in st.session_state['nomeCivil'].split()[:-1]) 
    if len(' '.join(word 
                    for word 
                    in st.session_state['nomeCivil'].split()[:-1])) > 0 
    else '') \
    + "\nnatureza: Biográfico" \
    + "\nsexo: " \
    + (st.session_state['genero'][0].lower() 
    if st.session_state['genero'] 
    in ['Feminino','Masculino'] 
    else '') \
    + "\n---\n\n"
    
    if cabecalho:
        texto_verbete += cabecalho
    
    #%% INTRODUÇÃO
    
    paragrafo_introducao = ("«%s»"%(st.session_state['nomeCivil'].title()) \
        if st.session_state['nomeCivil']
        else "") \
    + (' nasceu' 
        if st.session_state['dataNascimento']
        or st.session_state['munNascimento']
        else '') \
    + ((' em ' \
    + st.session_state["munNascimento"] \
    + ' (' 
    + list(estados_br().keys())[list(estados_br().values()).index(st.session_state['ufNascimento'])] 
    + ')') 
        if st.session_state['ufNascimento']
        and st.session_state['munNascimento']
        else '') \
    + (" em" + \
    (' %s de'%(st.session_state['dataNascimento'].day)) \
    + (' %s de'%(st.session_state['dataNascimento'].strftime("%B"))) \
    + (' %s'%(st.session_state['dataNascimento'].year)) 
        if st.session_state['dataNascimento']
        else '') \
    + ((", filh%s"%('a' if st.session_state['genero'] == 'Feminino' else 'o') \
    + " de " +
        (st.session_state['nomeMae'].strip() if st.session_state['nomeMae'] else '')  +
        (', ' +
        st.session_state['profissaoMae'].lower() 
        if st.session_state['profissaoMae']
        and st.session_state['nomeMae']
        else '') +
        (' e ' if st.session_state['nomeMae'].strip()
        and st.session_state['nomePai'].strip()
        else '') + 
        (st.session_state['nomePai'].strip() if st.session_state['nomePai'] else ''))
        if st.session_state['nomeMae']
        or st.session_state['nomePai']
        else '') + \
        (', ' +
        st.session_state['profissaoPai'].lower().strip()
        if st.session_state['profissaoPai']
        and st.session_state['nomePai']
        else '') \
    + '. '
    
    if paragrafo_introducao:
        texto_verbete += paragrafo_introducao
    
    # #%% Falecimento    
    
    # if 'mun_falecimento' not in st.session_state:
    #     st.session_state['mun_falecimento'] = ''
    # if "data_falecimento" not in st.session_state:
    #     st.session_state['data_falecimento'] = ''
    # if st.session_state['data_falecimento'] or st.session_state['mun_falecimento']:            
    #     paragrafo_falecimento = " Faleceu em" \
    #     + (' %s de'%(st.session_state['data_falecimento'].day)) \
    #     + (' %s de'%(st.session_state['data_falecimento'].strftime("%B"))) \
    #     + (' %s'%(st.session_state['data_falecimento'].year)) \
    #     + ((f' em {st.session_state["mun_falecimento"]}' 
    #       + ' (' 
    #       + list(estados_br().keys())[list(estados_br().values()).index(st.session_state['uf_falecimento'])]
    #       + ')') 
    #      if st.session_state['uf_falecimento']
    #      and st.session_state['mun_falecimento']
    #      else '') \
    #     + '. '
    # else:
    #     paragrafo_falecimento = ''
    
    # if paragrafo_falecimento:
    #     texto_verbete += paragrafo_falecimento
        
    return texto_verbete