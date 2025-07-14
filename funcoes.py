import random 
def transforma_base(lista_titulos):
    dic = {}
    for dicio in lista_titulos:
        nivel = dicio['nivel']
        if nivel in dic.keys():
            dic[nivel] += [dicio]
        else:
            dic[nivel] = [dicio]
    return dic 

def valida_questao(dicio):
    dic = {}
    
    if 'titulo' not in dicio.keys():
        dic['titulo'] = 'nao_encontrado'
    else: 
        if dicio['titulo'].strip() == '':
            dic['titulo'] =  'vazio'
    
    
    if len(dicio) != 4:
        dic['outro'] = 'numero_chaves_invalido'

    if 'nivel' not in dicio.keys():
        dic['nivel'] = 'nao_encontrado'
    else:
        if dicio['nivel'] != 'facil' and dicio['nivel'] != 'medio' and dicio['nivel'] != 'dificil':
            dic['nivel'] = 'valor_errado'
    
    if 'opcoes' not in dicio.keys():
        dic['opcoes'] = 'nao_encontrado'
    else:
        if len(dicio['opcoes']) != 4:
            dic['opcoes'] = 'tamanho_invalido'
        if len(dicio['opcoes']) == 4:
            if 'A' not in dicio['opcoes'].keys() or 'B' not in dicio['opcoes'].keys() or 'C' not in dicio['opcoes'].keys() or 'D' not in dicio['opcoes'].keys():
                dic['opcoes'] = 'chave_invalida_ou_nao_encontrada'
            else:
                dic_op = {}
                dic_opcoes = dicio['opcoes']
                for opcoes, valores in dic_opcoes.items():
                    if valores.strip() == '':
                        dic_op[opcoes] = 'vazia'
                if len(dic_op) > 0:
                    dic['opcoes'] = dic_op

    if 'correta' not in dicio.keys():
        dic['correta'] = 'nao_encontrado'
    else:
        if 'correta' in dicio.keys() and dicio['correta'] not in ['A', 'B', 'C', 'D']:
            dic['correta'] = 'valor_errado'
    
    return dic 



def valida_questoes(lista_questoes):
    lista_r = []
    for dicio in lista_questoes:
        res = valida_questao(dicio)
        lista_r.append(res)
    return lista_r
 

def sorteia_questao(dicio_organizado, nivel):
    lista_questoes = dicio_organizado[nivel]
    indice = len(lista_questoes) - 1
    r_num = random.randint(0, indice)
    return lista_questoes[r_num]

def sorteia_questao_inedita(dicio_organizado, nivel, lista):
    lista_questoes = dicio_organizado[nivel]
    lista_nova = []
    for questoes in lista_questoes:
        if questoes not in lista:
            lista_nova.append(questoes)
    indice = len(lista_nova) - 1
    r_num = random.randint(0, indice)
    return lista_nova[r_num]

def questao_para_texto(questao, ide):
    titulo = questao['titulo']
    A = questao['opcoes']['A']
    B = questao['opcoes']['B']
    C = questao['opcoes']['C']
    D = questao['opcoes']['D']
    resposta = f"""----------------------------------------
QUESTAO {ide}

{titulo}

RESPOSTAS:
A: {A}
B: {B}
C: {C}
D: {D}"""
    return resposta


def gera_ajuda(dicio_questoes):
    letra_correta = dicio_questoes['correta']
    questao_correta = dicio_questoes['opcoes'][letra_correta]
    lista_questoes = [dicio_questoes['opcoes']['A'], dicio_questoes['opcoes']['B'], dicio_questoes['opcoes']['C'], dicio_questoes['opcoes']['D']]

    lista_questoes.remove(questao_correta)

    tamanho = len(lista_questoes) - 1

    numero_questo = random.randint(1, 2)

    if numero_questo == 1:
        num_r = random.randint(0, tamanho)
        questao_errada = lista_questoes[num_r]
        resposta = f'''DICA:
Opções certamente erradas: {questao_errada}'''
    elif numero_questo == 2:
        num_r = random.randint(0, tamanho)
        questao_errada1 = lista_questoes[num_r]
        lista_questoes.remove(questao_errada1)
        tamanho2 = len(lista_questoes) - 1
        num_r2 = random.randint(0, tamanho2)
        questao_errada2 = lista_questoes[num_r2]
        resposta = f'''DICA:\nOpções certamente erradas: {questao_errada1} | {questao_errada2}'''
    return resposta


