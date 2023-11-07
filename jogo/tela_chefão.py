import pygame
import tela_final
from random import randint
import funcoes as jogo

TILE_FRAME = 50

def inicializa():
    pygame.init()
    widht = 1200
    height = 800
    QUANT_COELHOS = 5

    window = pygame.display.set_mode((widht,height))
    pygame.display.set_caption('RETRO SNAKE')

    clock = pygame.time.Clock()

    estado = {
        'pos_cobra': [(widht/2),(height/2)],
        'pos_rabo' : [(widht/2) + 12,(height/2) - 59],
        'velocidade' : [50,50],
        'pontuacao' : 0,
        'xp' : 0,
        'direcao': 'baixo',
        'cobra' : [{
            'pos' : [(widht/2),(height/2)],
            'imag' : '',
        }],
        'clock' : clock,
        'status': True
    }


    #posicao aleatoria da maçã
    x = randint(100,1100)
    y = randint(100,700)
    pos_maca = pygame.Rect((x, y), (30, 40))

    #posicao aleatoria da maca especial
    x = randint(100,1100)
    y = randint(100,700)
    pos_maca_especial = pygame.Rect((x, y), (30, 40))
            
    #parede    
    parede = pygame.Rect((0,0), (TILE_FRAME, TILE_FRAME))   
    estado['pos_parede'] = [parede]
    
    for y1 in range(0,height,TILE_FRAME):
        parede = pygame.Rect((0, y1), (TILE_FRAME, TILE_FRAME))
        estado['pos_parede'].append(parede)
    
    for x1 in range(0,widht,TILE_FRAME):
        parede = pygame.Rect((x1, 0), (TILE_FRAME, TILE_FRAME))
        estado['pos_parede'].append(parede)

    for y2 in range(0,height,TILE_FRAME):
        parede = pygame.Rect((widht-TILE_FRAME, y2), (TILE_FRAME,TILE_FRAME))
        estado['pos_parede'].append(parede)
    
    for x2 in range(0,widht,TILE_FRAME):
        parede = pygame.Rect((x2, height-TILE_FRAME), (TILE_FRAME, TILE_FRAME))
        estado['pos_parede'].append(parede)

    dicionario = {}

    #fontes
    dicionario['fonte'] = pygame.font.Font('fonte/perfect_dos_vga_437/Perfect DOS VGA 437 Win.ttf',20)

    #posicao
    dicionario['pos_maca'] = pos_maca
    dicionario['pos_maca_especial'] = pos_maca_especial

    #imagem da parede
    dicionario['parede'] = pygame.image.load('imagens/parede2.png')

    #imagens dos coelhos
    img_coelho = pygame.image.load('imagens/coelho.png')
    dicionario['coelho_bom'] = pygame.transform.scale(img_coelho,(40,50))

    img_coelho_mal = pygame.image.load('imagens/coelho_malvado.png')
    dicionario['coelho_mal'] = pygame.transform.scale(img_coelho_mal,(40,50))

    #posicao aleatoria do coelho
    dicionario['coelhos'] = []
    for _ in range(QUANT_COELHOS):
        x = randint(100,1100)
        y = randint(100,700)        
        coelho = {
            'pos': pygame.Rect((x,y), (40, 50)),
            'img': dicionario['coelho_bom'],
            'malvado': False
            }
        dicionario['coelhos'].append(coelho)

    #imagens da cobra
    img_cabeca = pygame.image.load('imagens/cobra_cabeca.png')
    dicionario['img_cabeca'] = pygame.transform.scale(img_cabeca,(50,50))

    dicionario['cobra_direita']= pygame.transform.rotate(dicionario['img_cabeca'],90)
    dicionario['cobra_cima']= pygame.transform.rotate(dicionario['img_cabeca'],180)
    dicionario['cobra_esquerda']= pygame.transform.rotate(dicionario['img_cabeca'],270)
    dicionario['cobra_baixo'] = dicionario['img_cabeca']
    estado['cobra'][0]['imag'] = dicionario['img_cabeca'] 

    img_cobra_rabo = pygame.transform.scale(pygame.image.load('imagens/cobra_rabo.png'),(50,50))
    dicionario['cobra_rabo_direita'] = pygame.transform.rotate(img_cobra_rabo,90)
    dicionario['cobra_rabo_cima'] = pygame.transform.rotate(img_cobra_rabo,180)
    dicionario['cobra_rabo_esquerda'] = pygame.transform.rotate(img_cobra_rabo,270)
    dicionario['cobra_rabo_baixo'] = img_cobra_rabo
    
    img_cobra_corpo = pygame.image.load('imagens/cobra_corpo.png')
    dicionario['cobra_corpo'] = pygame.transform.scale(img_cobra_corpo,(50,50))
    dicionario['cobra_corpo_horizontal'] = pygame.transform.rotate(dicionario['cobra_corpo'],90)
    dicionario['cobra_corpo_vertical'] = dicionario['cobra_corpo']

    img_cobra_quina = pygame.transform.scale(pygame.image.load('imagens/cobra_mov1.png'), (50,50))
    dicionario['cobra_quina_direita_baixo'] = img_cobra_quina
    dicionario['cobra_quina_esquerda_baixo'] = pygame.transform.rotate(img_cobra_quina, -90)
    dicionario['cobra_quina_esquerda_cima'] = pygame.transform.rotate(img_cobra_quina, -180)
    dicionario['cobra_quina_direita_cima'] = pygame.transform.rotate(img_cobra_quina, -270)

    #imagens das maçãs
    img_maca = pygame.image.load('imagens/maca.png')
    dicionario['maca'] = pygame.transform.scale(img_maca,(30,40))

    img_maca_especial = pygame.image.load('imagens/maca_especial.png')
    dicionario['maca_especial'] = pygame.transform.scale(img_maca_especial,(30,40))

    #sons
    musica = 'sons/8bit-music-for-game-68698.mp3'
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()

    dicionario['game_over'] = pygame.mixer.Sound('sons/game-over-arcade-6435.mp3')

    dicionario['comida'] = pygame.mixer.Sound('sons/eating-sound-effect-36186.mp3')

    return window,dicionario,estado 

def recebe_eventos(estado,dicionario, window):
    estado, dicionario = jogo.muda_movimento(estado, dicionario)
    y = estado['cobra'][0]['pos'][1] 
    x = estado['cobra'][0]['pos'][0] 
    
    # movimentação da cobra
    estado, x, y = jogo.movimenta(estado, x, y)
    
    estado,dicionario = jogo.movimenta_coelho(estado,dicionario)

    estado, dicionario = jogo.atualiza_cobra(estado, dicionario, x, y)

    cabeca = estado['cobra'][0]
    retan_cobra = pygame.Rect((cabeca['pos'][0],cabeca['pos'][1]),(TILE_FRAME,TILE_FRAME))  

    #colisão da cobra c/ ela mesma
    estado, dicionario = jogo.colisao_cobra(estado, dicionario, retan_cobra)

    #colisão da cobra c/ parede
    estado, dicionario = jogo.colisao_parede(estado, dicionario, retan_cobra)
        
    #colisao da cobra com a maçã
    estado, dicionario = jogo.colisao_maca(estado, dicionario, retan_cobra)

    #colisao da cobra com a maçã especial
    estado, dicionario = jogo.colisao_maca_especial(estado, dicionario, retan_cobra)
    
    #colisao da cobra com o coelho
    estado, dicionario = jogo.colisao_coelho(estado, dicionario, retan_cobra)

    return estado['status']

def desenha(window,dicionario,estado):
    window.fill((0,149,0))

    for cobra in estado['cobra']:
        window.blit(cobra['imag'],(cobra['pos'][0], cobra['pos'][1]))

    for parede in estado['pos_parede']:
        window.blit(dicionario['parede'],parede)

    for coelho in dicionario['coelhos']:
        window.blit(coelho['img'],(coelho['pos'][0],coelho['pos'][1]))

    window.blit(dicionario['maca'],(dicionario['pos_maca'][0],dicionario['pos_maca'][1]))

    window.blit(dicionario['maca_especial'],(dicionario['pos_maca_especial'][0],dicionario['pos_maca_especial'][1]))

    texto = dicionario['fonte'].render(f'POINTS: {estado["pontuacao"]}',False,(0,0,0))
    window.blit(texto,(10,10))

    texto = dicionario['fonte'].render(f'XP: {estado["xp"]}',False,(0,0,0))
    window.blit(texto,(10,30))
    pygame.display.update()

def game_loop(window,dicionario,estado):
    # jogo começa
    while recebe_eventos(estado,dicionario,window):
        estado['clock'].tick(4)
        desenha(window,dicionario,estado)
    
    # jogo acaba e troca pra tela final
    w,d = tela_final.inicializa()
    d['morte'] = dicionario['morte']
    tela_final.game_loop(w,d)   