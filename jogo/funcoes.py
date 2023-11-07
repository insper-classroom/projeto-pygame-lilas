import pygame
from random import randint

TILE_FRAME = 50

def game_over(estado, dicionario):
    dicionario['game_over'].play()
    estado['status'] = False
    return estado, dicionario

def movimenta(estado, x, y):
    if estado['direcao'] == 'baixo':
        y += estado['velocidade'][1]
    if estado['direcao'] == 'cima':
        y-= estado['velocidade'][1]
    if estado['direcao'] == 'direita':
        x += estado['velocidade'][0]
    if estado['direcao'] == 'esquerda':
        x -= estado['velocidade'][0]
    
    return estado, x, y

def muda_movimento(estado, dicionario):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT:
                if estado['direcao'] != 'esquerda': 
                    dicionario['img_cabeca'] = dicionario['cobra_direita']
                    estado['direcao'] = 'direita'

            elif event.key == pygame.K_LEFT:
                if estado['direcao'] != 'direita':
                    dicionario['img_cabeca'] = dicionario['cobra_esquerda']
                    estado['direcao'] = 'esquerda'
                
            elif event.key == pygame.K_DOWN:
                if estado['direcao'] != 'cima':
                    dicionario['img_cabeca'] = dicionario['cobra_baixo']
                    estado['direcao'] = 'baixo'
            
            elif event.key == pygame.K_UP:
                if estado['direcao'] != 'baixo':
                    dicionario['img_cabeca'] = dicionario['cobra_cima']
                    estado['direcao'] = 'cima'
    return estado, dicionario

def atualiza_cobra(estado, dicionario, x, y):
    pedaco = {
        'pos' : [x,y],
        'imag' : dicionario['img_cabeca'],
    }
    
    estado['cobra'].insert(0, pedaco)
    del estado['cobra'][-1]

    if len(estado['cobra']) == 2:
        rabo = estado['cobra'][-1]
        if estado['direcao'] == 'baixo':
            rabo['imag'] = dicionario['cobra_rabo_baixo']
        if estado['direcao'] == 'cima':
            rabo['imag'] = dicionario['cobra_rabo_cima']
        if estado['direcao'] == 'esquerda':
            rabo['imag'] = dicionario['cobra_rabo_esquerda']
        if estado['direcao'] == 'direita':
            rabo['imag'] = dicionario['cobra_rabo_direita']

    if len(estado['cobra']) > 2:
        cabeca = estado['cobra'][0]
        pescoco = estado['cobra'][1]
        pescoco['imag']= dicionario['cobra_corpo']
        rabo = estado['cobra'][-1]
        corpo1 = estado['cobra'][2]
                    
        if estado['direcao'] == 'baixo':
            # acompanha onde tá indo
            rabo['imag'] = dicionario['cobra_rabo_baixo']
            if cabeca['pos'][1] > pescoco['pos'][1] and pescoco['pos'][1] > corpo1['pos'][1]:
                pescoco['imag']= dicionario['cobra_corpo_vertical']
            # estava vindo da direita
            if cabeca['pos'][1] > pescoco['pos'][1] and pescoco['pos'][0] < corpo1['pos'][0]:
                pescoco['imag']= dicionario['cobra_quina_direita_baixo']
            # estava vindo da esquerda
            if cabeca['pos'][1] > pescoco['pos'][1] and pescoco['pos'][0] > corpo1['pos'][0]: 
                pescoco['imag']= dicionario['cobra_quina_esquerda_baixo']

        if estado['direcao'] == 'cima':
            # acompanha onde tá indo
            rabo['imag'] = dicionario['cobra_rabo_cima']
            if cabeca['pos'][1] < pescoco['pos'][1] and pescoco['pos'][1] < corpo1['pos'][1]: #cenario 2
                pescoco['imag']= dicionario['cobra_corpo_vertical']
            # 
            if cabeca['pos'][1] < pescoco['pos'][1] and pescoco['pos'][0] > corpo1['pos'][0]: 
                pescoco['imag']= dicionario['cobra_quina_esquerda_cima']
            if cabeca['pos'][1] < pescoco['pos'][1] and pescoco['pos'][0] < corpo1['pos'][0]: 
                pescoco['imag']= dicionario['cobra_quina_direita_cima']

        if estado['direcao'] == 'esquerda':
            rabo['imag'] = dicionario['cobra_rabo_esquerda']
            
            if cabeca['pos'][0] < pescoco['pos'][0] and pescoco['pos'][0] < corpo1['pos'][0]:
                pescoco['imag'] = dicionario['cobra_corpo_horizontal']
            if cabeca['pos'][0] < pescoco['pos'][0] and pescoco['pos'][1] > corpo1['pos'][1]: # cenario 3
                pescoco['imag'] = dicionario['cobra_quina_esquerda_cima']
            if cabeca['pos'][0] < pescoco['pos'][0] and pescoco['pos'][1] < corpo1['pos'][1]: # cenario 4
                pescoco['imag'] = dicionario['cobra_quina_esquerda_baixo']

        if estado['direcao'] == 'direita':
            rabo['imag'] = dicionario['cobra_rabo_direita']
            
            if cabeca['pos'][0] > pescoco['pos'][0] and pescoco['pos'][0] > corpo1['pos'][0]:
                pescoco['imag']= dicionario['cobra_corpo_horizontal']
            if cabeca['pos'][0] > pescoco['pos'][0] and pescoco['pos'][1] < corpo1['pos'][1]: 
                pescoco['imag']= dicionario['cobra_quina_direita_baixo']
            if cabeca['pos'][0] > pescoco['pos'][0] and pescoco['pos'][1] > corpo1['pos'][1]: 
                pescoco['imag']= dicionario['cobra_quina_direita_cima']
    return estado, dicionario

def colisao_parede(estado, dicionario, retan_cobra):
    for parede in estado['pos_parede']:
        if retan_cobra.colliderect(parede):
            estado, dicionario = game_over(estado, dicionario)
            dicionario['morte'] = "ter batido na parede"
    return estado, dicionario

def colisao_cobra(estado, dicionario, retan_cobra):
    for i, pedaco in enumerate(estado['cobra']):
        if i == 0:
            pass
        else:
            retan_pedaco = pygame.Rect((pedaco['pos'][0], pedaco['pos'][1]), (TILE_FRAME, TILE_FRAME))
            if retan_cobra.colliderect(retan_pedaco):
                estado, dicionario = game_over(estado, dicionario)
                dicionario['morte'] = "comer o próprio corpo"
    return estado, dicionario

def colisao_maca(estado, dicionario, retan_cobra):
    retan_maca = pygame.Rect((dicionario['pos_maca'][0], dicionario['pos_maca'][1]),(30,40))
    if retan_cobra.colliderect(retan_maca):
        y = estado['cobra'][0]['pos'][1] 
        x = estado['cobra'][0]['pos'][0] 
        estado, x, y = movimenta(estado, x, y)  

        nova_cabeca = {
            'pos' : [x,y],
            'imag' : dicionario['img_cabeca']
        }

        estado['cobra'].insert(0,nova_cabeca)

        estado['cobra'][1]['imag'] = dicionario['cobra_corpo']

        dicionario['comida'].play()
        estado["pontuacao"] += 1
        x = randint(100,1100)
        y = randint(100,700)
        nova_maca = pygame.Rect((x, y), (30, 40))
        dicionario['pos_maca'] = nova_maca
    return estado, dicionario
        
def colisao_maca_especial(estado, dicionario, retan_cobra):
    retan_maca_especial = pygame.Rect((dicionario['pos_maca_especial'][0], dicionario['pos_maca_especial'][1]),(30,40))
    if retan_cobra.colliderect(retan_maca_especial):
        dicionario['comida'].play()
        estado['xp'] += 5
        
        x = randint(50,500)
        y = randint(50,100)
        nova_maca_especial = pygame.Rect((x, y), (30, 40))
        dicionario['pos_maca_especial'] = nova_maca_especial
    return estado, dicionario

def colisao_coelho_parede(estado, coelho):
    for parede in estado['pos_parede']:
        if coelho['pos'].colliderect(parede):
            return True, parede
    return False, parede

def movimenta_coelho(estado, dicionario):
    for coelho in dicionario['coelhos']:
        colisao, parede = colisao_coelho_parede(estado, coelho)
        x, y = coelho['pos'][0], coelho['pos'][1]
        if colisao:
            if parede[0] > 0 and parede[1] == 0:
                coelho['pos'] = pygame.Rect((x,y+50), (40,50))
            elif parede[0] > 0 and parede[1] == 750:
                coelho['pos'] = pygame.Rect((x, y-50), (40, 50))
            elif parede[0] == 0 and parede[1] > 0:
                coelho['pos'] = pygame.Rect((x+50, y), (40, 50))
            else:
                coelho['pos'] = pygame.Rect((x-50, y),(40, 50))
        elif coelho['malvado']:
            x += randint(-50, 50)
            y += randint(-50, 50)
            coelho['pos'] = pygame.Rect((x, y), (40, 50))
    return estado, dicionario

def colisao_coelho(estado, dicionario,retan_cobra):
    for i, coelho in enumerate(dicionario['coelhos']):
        if retan_cobra.colliderect(coelho['pos']):
            if estado['xp'] < 20 and coelho['malvado'] == False:
                coelho['img'] = dicionario['coelho_mal']
                coelho['malvado'] = True
            elif estado['xp'] < 20 and coelho['malvado'] == True:
                for i in range(0, 3):
                    try:
                        del estado['cobra'][-1]
                    except IndexError:
                        estado, dicionario = game_over(estado, dicionario)
                        dicionario['morte'] = "deixar o coelho bravo"
                        return estado, dicionario
                coelho['img'] = dicionario['coelho_bom']
                coelho['malvado'] = False
            else:
                del dicionario['coelhos'][i]
                estado['xp'] -= 20
    return estado, dicionario

