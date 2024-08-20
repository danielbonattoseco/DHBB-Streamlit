import streamlit as st 
from utils.estados_br import estados_br

def construtor_paragrafo_parentela_politica(parentela_politica):
    """Converte os metadados da classe em um parágrafo formatado do verbete"""
    if parentela_politica['parentesco']: #CAMPO OBRIGATÓRIO
        paragrafo = parentela_politica['parentesco'].title() \
                    + " de " \
                    + parentela_politica['nome'] 
        
        if len(parentela_politica['cargos']) > 0 and parentela_politica['cargos'][0] != '':
            paragrafo = paragrafo + ', que atuou como '
            for i, cargo in enumerate(parentela_politica['cargos']):
                if len(parentela_politica['cargos']) > 1 and i == len(parentela_politica['cargos']) - 1:
                    paragrafo = paragrafo + " e "
                paragrafo = paragrafo \
                + cargo.lower()
                if i == len(parentela_politica['cargos']) - 1:
                    paragrafo = paragrafo + ". "
                elif i != len(parentela_politica['cargos']) - 2:
                        paragrafo = paragrafo + ", "
        else:
            paragrafo = paragrafo + '. '
        return paragrafo
    else:
        return ''

def construtor_paragrafo_formacao_academica(formacao_academica):
    """Converte os metadados da classe em um parágrafo formatado do verbete"""
    if formacao_academica['tipo']: #CAMPO OBRIGATÓRIO
        paragrafo = 'Cursou' \
        + (' o' if formacao_academica['tipo'] in ['Ensino Fundamental','Ensino Médio'] else '') \
        + (' %s'%formacao_academica['tipo'].lower() if formacao_academica['tipo'] else '') \
        + (' em %s'%formacao_academica['curso'].lower() if ((formacao_academica['tipo'] in ['Graduação','Pós-Graduação','Especialização']) and formacao_academica['curso']) else '') \
        + (' na instituição %s'%formacao_academica['instituicao'] if formacao_academica['instituicao'] else '') \
        + (' em %s (%s)'%(formacao_academica['municipio'],list(estados_br().keys())[list(estados_br().values()).index(formacao_academica['uf'])] ) if (formacao_academica['municipio'] and formacao_academica['uf']) else '') \
        + (' a partir de %s'%formacao_academica['anoInicio'] if formacao_academica['anoInicio'] else '') \
        + (' até %s'%formacao_academica['anoFim'] if formacao_academica['anoFim'] else '') \
        + '. '
        return paragrafo
    else:
        return ''

def construtor_paragrafo_trajetoria_politica(trajetoria_politica):\
    #ORDENAR TRAJETORIAS POLITICAS POR DATA 
    if st.session_state.trajetoriasPoliticas:
        # if all(not d.get("ano") for d in st.session_state.trajetoriasPoliticas):
        st.session_state.trajetoriasPoliticas.sort(key=lambda x: (x['dataPleito']['ano'] is None, x['dataPleito']['ano'])) #ORGANIZA AS ATUAÇÕES POR ANO.
            
        # FLAG DE PRIMEIRA TRAJETORIA POLITICA
        for i, dicionario in enumerate(st.session_state.trajetoriasPoliticas):
            if i == 0:
                dicionario["primeiraTrajetoriaPolitica"] = True
            else:
                dicionario["primeiraTrajetoriaPolitica"] = False

    if trajetoria_politica['cargo']:
        #CAPTURAR ATUAÇÕES POLÍTICAS RELACIONADAS
        atuacoes_politicas_relacionadas = [atuacao
                                      for atuacao
                                      in st.session_state.atuacoesLegislativas
                                      if 'mandato'
                                      in trajetoria_politica
                                      and atuacao['trajetoriaPoliticaRelacionada'] ==
                                      trajetoria_politica['cargo'] + " (" + str(trajetoria_politica['mandato']) + ")"]
        
        #INICIO REDAÇÃO        
        if trajetoria_politica['primeiraTrajetoriaPolitica']:
            paragrafo = '\nIniciou na vida política' \
            + (' em %s'%trajetoria_politica['dataPleito']['ano'] if trajetoria_politica['dataPleito']['ano'] else '') \
            + ' quando concorreu ao cargo de %s'%trajetoria_politica['cargo'] \
            + (' pelo %s'%trajetoria_politica['partido'] if trajetoria_politica['partido'] else '') \
            + ', no qual' \
            + (' recebeu %s votos e'%trajetoria_politica['votos'] if trajetoria_politica['votos'] else '') \
            + (' %sconseguiu eleger-se.'%('' if trajetoria_politica['eleito'] else 'não ')) \
            + ((' Renunciou ao cargo' \
            + (' em %s'%trajetoria_politica['renunciaData']['data'] if trajetoria_politica['renunciaData']['data'] else '') \
            + (' por motivo de %s'%trajetoria_politica['renunciaMotivo'].lower() if trajetoria_politica['renunciaMotivo'] else '') \
            + '. ') if 'renuncia' in trajetoria_politica and trajetoria_politica['renuncia'] else '')
            
            ###INSERIR ATUACOES LEGISLATIVAS
            if atuacoes_politicas_relacionadas:
                if len(atuacoes_politicas_relacionadas) > 1: #CASO HAJA MAIS DE UMA ATUAÇÃO LEGISLATIVA
                    
                    paragrafo += " Durante o exercício de seu mandato atuou nas seguintes funções legislativas: "
                    
                    for index, atuacao in enumerate(atuacoes_politicas_relacionadas):
                        
                        paragrafo += "%i) "%(index + 1) \
                        + "%s"%(atuacao['nome'].lower() if atuacao['nome'] else '') \
                        + (', %s'%atuacao['tipo'].lower() if atuacao['tipo'] else '') \
                        + ((' n%s'%('a ' if atuacao['casaLegislativa'] == 'Câmara dos Deputados' else 'o ') \
                        + atuacao['casaLegislativa'].lower()) if atuacao['casaLegislativa'] else '') \
                        + (', na função de %s'%atuacao['funcao'].lower() if atuacao['funcao'] else '')
                        
                        if index == len(atuacoes_politicas_relacionadas) - 1:
                            paragrafo += ".\n"
                        elif index == len(atuacoes_politicas_relacionadas) - 2:
                            paragrafo += " e "
                        else:
                            paragrafo += ", "
                        
                else: #CASO HAJA APENAS UMA ATUAÇÃO LEGISLATIVA
                    
                    for atuacao in atuacoes_politicas_relacionadas:
                        
                        paragrafo += " Durante o exercício de seu mandato atuou na %s"%(atuacao['nome'].lower() if atuacao['nome'] else '') \
                        + (', %s'%atuacao['tipo'].lower() if atuacao['tipo'] else '') \
                        + ((' n%s'%('a ' if atuacao['casaLegislativa'] == 'Câmara dos Deputados' else 'o ') \
                        + atuacao['casaLegislativa'].lower()) if atuacao['casaLegislativa'] else '') \
                        + (', na função de %s'%atuacao['funcao'].lower() if atuacao['funcao'] else '') \
                        + ".\n"
            else: #CASO NÃO HAJA ATUAÇÃO LEGISLATIVA
                paragrafo += "\n"
    
            return paragrafo
        
        else: #SEGUNDA TRAJETÓRIA POLÍTICA EM DIANTE
        
            paragrafo = 'Candidatou-se ao cargo de %s'%trajetoria_politica['cargo'] \
            + (' nas eleições de %s'%trajetoria_politica['dataPleito']['ano'] if trajetoria_politica['dataPleito']['ano'] else '') \
            + (' pelo %s'%trajetoria_politica['partido'] if trajetoria_politica['partido'] else '') \
            + ', no qual' \
            + (' recebeu %s votos e'%trajetoria_politica['votos'] if trajetoria_politica['votos'] else '') \
            + (' %sconseguiu eleger-se.'%('' if trajetoria_politica['eleito'] else 'não ')) \
            + ((' Renunciou ao cargo' \
            + (' em %s'%trajetoria_politica['renunciaData']['data'] if trajetoria_politica['renunciaData']['data'] else '') \
            + (' por motivo de %s'%trajetoria_politica['renunciaMotivo'].lower() if trajetoria_politica['renunciaMotivo'] else '') \
            + '. ') if 'renuncia' in trajetoria_politica and trajetoria_politica['renuncia'] else '')
                
            ###INSERIR ATUACOES LEGISLATIVAS
            if atuacoes_politicas_relacionadas:
                if len(atuacoes_politicas_relacionadas) > 1: #CASO HAJA MAIS DE UMA ATUAÇÃO LEGISLATIVA
                    
                    paragrafo += " Durante o exercício de seu mandato atuou nas seguintes funções legislativas: "
                    
                    for index, atuacao in enumerate(atuacoes_politicas_relacionadas):
                        
                        paragrafo += "%i) "%(index + 1) \
                        + "%s"%(atuacao['nome'].lower() if atuacao['nome'] else '') \
                        + (', %s'%atuacao['tipo'].lower() if atuacao['tipo'] else '') \
                        + ((' n%s'%('a ' if atuacao['casaLegislativa'] == 'Câmara dos Deputados' else 'o ') \
                        + atuacao['casaLegislativa'].lower()) if atuacao['casaLegislativa'] else '') \
                        + (', na função de %s'%atuacao['funcao'].lower() if atuacao['funcao'] else '')
                        
                        if index == len(atuacoes_politicas_relacionadas) - 1:
                            paragrafo += ".\n"
                        elif index == len(atuacoes_politicas_relacionadas) - 2:
                            paragrafo += " e "
                        else:
                            paragrafo += ", "
                        
                else: #CASO HAJA APENAS UMA ATUAÇÃO LEGISLATIVA
                    
                    for atuacao in atuacoes_politicas_relacionadas:
                        
                        paragrafo += " Durante o exercício de seu mandato atuou na %s"%(atuacao['nome'].lower() if atuacao['nome'] else '') \
                        + (', %s'%atuacao['tipo'].lower() if atuacao['tipo'] else '') \
                        + ((' n%s'%('a ' if atuacao['casaLegislativa'] == 'Câmara dos Deputados' else 'o ') \
                        + atuacao['casaLegislativa'].lower()) if atuacao['casaLegislativa'] else '') \
                        + (', na função de %s'%atuacao['funcao'].lower() if atuacao['funcao'] else '') \
                        + ".\n"
    
            else: #CASO NÃO HAJA ATUAÇÃO LEGISLATIVA
                paragrafo += "\n" 
            
            return paragrafo    
    else:
        return ''

def construtor_paragrafo_atuacao_burocracia_estatal(burocracia_estatal):
    if burocracia_estatal['cargoNomeado']:
        paragrafo = 'Foi nomead%s para o cargo de %s'%('a' if st.session_state['genero'] == 'Feminino' else 'o', burocracia_estatal['cargoNomeado']) \
        + (' no %s'%burocracia_estatal['orgao'] if burocracia_estatal['orgao'] else '') \
        + (' em %s'%burocracia_estatal['dataNomeacao']['data'] if burocracia_estatal['dataNomeacao']['data'] else '') \
        + '. ' \
        + (('Foi exonerad%s do cargo'%('a' if st.session_state['genero'] == 'Feminino' else 'o') \
        + (' em %s'%burocracia_estatal['exoneracaoData']['data'] if burocracia_estatal['exoneracaoData']['data'] else '') \
        + (' por motivo de %s'%burocracia_estatal['exoneracaoMotivo'] if burocracia_estatal['exoneracaoMotivo'] else '') \
        + '. ') if burocracia_estatal['exonerado'] else '')
        return paragrafo
    else:
        return ''

def construtor_paragrafo_atuacao_imprensa(atuacao_imprensa):
    """Converte os metadados da classe em um parágrafo formatado do verbete"""
    if atuacao_imprensa['nomeJornal']: #CAMPO OBRIGATÓRIO
        paragrafo = 'Atuou no jornal ' \
        + atuacao_imprensa['nomeJornal'] \
        + (' como %s'%atuacao_imprensa['funcaoExercida'].lower() if atuacao_imprensa['funcaoExercida'] else '') \
        + (' a partir de %s'%atuacao_imprensa['dataInicio']['data'] if atuacao_imprensa['dataInicio']['data'] else '') \
        + (' até %s'%atuacao_imprensa['dataFim']['data'] if atuacao_imprensa['dataFim']['data'] else '') \
        + '. '
        return paragrafo
    else:
        return ''

def construtor_paragrafo_obra_do_verbetado(obra_do_verbetado):
    if obra_do_verbetado['nomeObra']:
        paragrafo = 'Publicou a obra "' \
        + obra_do_verbetado['nomeObra'] \
        + ('" em %s'%obra_do_verbetado['dataPublicacao']['data'] if obra_do_verbetado['dataPublicacao']['data'] else '') \
        + '. '
        return paragrafo
    else:
        return ''
    
def construtor_paragrafo_obra_sobre_verbetado(obra_sobre_verbetado):
    if obra_sobre_verbetado['nomeObra']:
        paragrafo = ('Em %s'%obra_sobre_verbetado['dataPublicacao']['data'] if obra_sobre_verbetado['dataPublicacao']['data'] else '') \
        + (' teve' if obra_sobre_verbetado['dataPublicacao']['data'] else 'Teve') \
        + (' uma obra publicada em sua referência, intitulada "' \
        + obra_sobre_verbetado['nomeObra']) \
        + '". '
        return paragrafo
    else:
        return ''

def construtor_paragrafo_obra_processo_criminal(processo_criminal):
    if processo_criminal['condenado']:
        paragrafo = "Foi indiciad%s no processo"%('a' if st.session_state['genero'] == 'Feminino' else 'o') \
        + (' %s,'%processo_criminal['processo'] if processo_criminal['processo'] else '') \
        + (' número %s,'%processo_criminal['codigoProcesso'] if processo_criminal['codigoProcesso'] else '') \
        + (' movido por motivo de %s,'%processo_criminal['motivoProcesso'].lower() if processo_criminal['motivoProcesso'] else '') \
        + ' do qual foi condenad%s'%('a' if st.session_state['genero'] == 'Feminino' else 'o') \
        + (' em %s'%processo_criminal['dataCondenacao']['data'] if processo_criminal['dataCondenacao']['data'] else '') \
        + '. '
        return paragrafo
    else:
        return ''

def construtor_paragrafo_conjuge(conjuge):
    if conjuge['nome']:
        paragrafo = '\nCasou-se com ' \
        + conjuge['nome'] \
        + (', com quem teve %s filho%s'%(len(conjuge['nomesFilhos']),"s" if len(conjuge['nomesFilhos']) > 1 else '') \
        + ((": " + ", ".join([i for i in conjuge['nomesFilhos'][:-1]]) + " e " + conjuge['nomesFilhos'][-1]) 
           if len(conjuge['nomesFilhos']) > 1 and all(isinstance(item, str) and len(item) > 0 for item in conjuge['nomesFilhos'])
           else (" incluindo " + ", ".join([i for i in conjuge['nomesFilhos'] 
                                            if len(i) > 0][:-1]) + (" e " + [i for i in conjuge['nomesFilhos'] 
                                                                             if len(i) > 0][-1] if len([i for i in conjuge['nomesFilhos'] if len(i) > 0]) > 1 
                                                                             else [i for i in conjuge['nomesFilhos'] if len(i) > 0][0])) 
           if len(conjuge['nomesFilhos']) > 1 and any(isinstance(item, str) and len(item) > 0 for item in conjuge['nomesFilhos'])
           else (" chamado %s"%conjuge['nomesFilhos'][0] 
                 if len(conjuge['nomesFilhos']) == 1 and len(conjuge['nomesFilhos'][0]) > 0
                 else " incluindo %s"%conjuge['nomesFilhos'][0] if len(conjuge['nomesFilhos'][0]) > 0 else '')) if conjuge['filhos'] else '') \
        + '.'
        return paragrafo
    else:
        return ''
    
def construtor_paragrafo_fonte(fonte):
    if fonte['autor']:
        paragrafo = "\n"
        autor_split = fonte['autor'].split()
        if len(autor_split) > 1:
            autor_formatado = f"{autor_split[-1].upper()}, {' '.join(autor_split[:-1])}"
            paragrafo += (f'{autor_formatado}. ')
        else:
            paragrafo += (f"{fonte['autor'].upper()}. ")
        paragrafo += (f"{fonte['titulo']}. " if fonte['titulo'] else '')
        paragrafo += (f"{fonte['informacoesComplementares']}. " if fonte['informacoesComplementares'] else '')
        if fonte['origem'] == "Online":
            paragrafo += (f"Disponível em: {fonte['url']}. " if fonte['url'] else '')
            paragrafo += (f"Acesso em: {fonte['dataAcesso']}. " if fonte['dataAcesso'] else '')
        return paragrafo
    else:
        return ''


#%%
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
    
    # INTRODUÇÃO
    
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
    
    #INSERIR PARENTELAS POLÍTICAS
    paragrafo_parentelas_politicas = ''.join([construtor_paragrafo_parentela_politica(parentela_politica) 
                                              for parentela_politica 
                                              in st.session_state['parentelasPoliticas']])
    if paragrafo_parentelas_politicas:
        texto_verbete += paragrafo_parentelas_politicas

    #INSERIR ATUAÇÕES IMPRENSA
    paragrafo_atuacoes_imprensa = ''.join([construtor_paragrafo_atuacao_imprensa(atuacao_imprensa) 
                                           for atuacao_imprensa 
                                           in st.session_state['atuacoesImprensa']])
    if paragrafo_atuacoes_imprensa:
        texto_verbete += paragrafo_atuacoes_imprensa

    #INSERIR FORMAÇÕES ACADÊMICAS
    paragrafo_formacoes_academicas = ''.join([construtor_paragrafo_formacao_academica(formacao_academica) 
                                              for formacao_academica 
                                              in st.session_state['formacoesAcademicas']])
    if paragrafo_formacoes_academicas:
        texto_verbete += paragrafo_formacoes_academicas

    #INSERIR TRAJETÓRIAS POLÍTICAS
    paragrafo_trajetorias_politicas = ''.join([construtor_paragrafo_trajetoria_politica(trajetoria_politica) 
                                               for trajetoria_politica 
                                               in st.session_state['trajetoriasPoliticas']])
    if paragrafo_trajetorias_politicas:
        texto_verbete += paragrafo_trajetorias_politicas

    #INSERIR TRAJETÓRIAS NA BUROCRACIA ESTATAL
    paragrafo_trajetorias_burocracia_estatal = ''.join([construtor_paragrafo_atuacao_burocracia_estatal(burocracia_estatal) 
                                                        for burocracia_estatal 
                                                        in st.session_state['burocraciasEstatais']])
    if paragrafo_trajetorias_burocracia_estatal:
        texto_verbete += paragrafo_trajetorias_burocracia_estatal

    #INSERIR OBRAS PUBLICADAS PELO VERBETADO
    paragrafo_obras_do_verbetado = ''.join([construtor_paragrafo_obra_do_verbetado(obra_do_verbetado) 
                                            for obra_do_verbetado 
                                            in st.session_state['obrasDoVerbetado']])
    if paragrafo_obras_do_verbetado:
        texto_verbete += paragrafo_obras_do_verbetado

    #INSERIR OBRAS PUBLICADAS SOBRE O VERBETADO
    paragrafo_obras_sobre_verbetado = ''.join([construtor_paragrafo_obra_sobre_verbetado(obra_sobre_verbetado) 
                                            for obra_sobre_verbetado 
                                            in st.session_state['obrasSobreVerbetado']])
    if paragrafo_obras_sobre_verbetado:
        texto_verbete += paragrafo_obras_sobre_verbetado

    #INSERIR OBRAS PROCESSOS CRIMINAIS
    paragrafo_processos_criminais = ''.join([construtor_paragrafo_obra_processo_criminal(processo_criminal) 
                                            for processo_criminal 
                                            in st.session_state['processosCriminais']])
    if paragrafo_processos_criminais:
        texto_verbete += paragrafo_processos_criminais

    #INSERIR CONJUGES E FILHOS
    paragrafo_conjuges = ''.join([construtor_paragrafo_conjuge(conjuge) 
                                            for conjuge 
                                            in st.session_state['conjuges']])
    if paragrafo_conjuges:
        texto_verbete += paragrafo_conjuges

    #INSERIR FONTES
    paragrafo_fontes = ''.join([construtor_paragrafo_fonte(fonte) 
                                            for fonte 
                                            in st.session_state['fontes']])
    if paragrafo_fontes:
        texto_verbete += "\n\nFONTES:" + paragrafo_fontes

    # FALECIMENTO
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
          + list(estados_br().keys())[list(estados_br().values()).index(st.session_state['uf_falecimento'])]
          + ')') 
          if st.session_state['uf_falecimento']
          and st.session_state['mun_falecimento']
          else '') \
        + '. '
    else:
        paragrafo_falecimento = ''
    
    if paragrafo_falecimento:
        texto_verbete += paragrafo_falecimento
        
    return texto_verbete