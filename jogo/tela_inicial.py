import pygame
import tela_jogo
pygame.mixer.init()

vaijogo = False

def inicializa():
    #janela
    pygame.init()
    window = pygame.display.set_mode((1200,800))
    pygame.display.set_caption('RETRO SNAKE')

    dicionario = {}
    #INSTRUCOES FONTE
    dicionario['fonte'] = pygame.font.Font('fonte/perfect_dos_vga_437/Perfect DOS VGA 437 Win.ttf',25)

    #desenho da cobra
    dicionario['cobra'] = pygame.image.load('imagens/cobra_logo.png')
    dicionario['cobra'] = pygame.transform.scale(dicionario['cobra'],(300,300))

    #imagem bem vindos
    dicionario['bem vindo'] = pygame.image.load('imagens/bem vindos.png')

    dicionario['int'] = 'sons/8bit-music-for-game-68698.mp3'
    pygame.mixer.music.load(dicionario['int'])
    pygame.mixer.music.play(-1)
    dicionario_comida = {}

    return window,dicionario,dicionario_comida

def recebe_eventos():
    global vaijogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
            if event.key  == pygame.K_RETURN:
                vaijogo = True
        if event.type == pygame.KEYDOWN:        
            if event.key == pygame.K_y:
                vaijogo = True
                

    return True

def desenha(window,dicionario):
    window.fill((0,149,0))
#DESENHAR A COBRA
    window.blit(dicionario['cobra'],(420,220))

#desenha bem vindo
    window.blit(dicionario['bem vindo'],(360,100))

#DESENHAR AS INSTRUÇOES
    texto = dicionario['fonte'].render('COMO JOGAR:',False,(0,0,0))
    window.blit(texto,(100,490))

    texto = dicionario['fonte'].render('- você pode mover com as teclas W,S,A,D ou usar as setas ',False,(0,0,0))
    window.blit(texto,(100,525))

    texto = dicionario['fonte'].render('- para você aumentar o corpo é necessário comer a maça vermelha ',False,(0,0,0))
    window.blit(texto,(100,550))

    texto = dicionario['fonte'].render('- o objetivo do jogo é que você chegue na tela do chefão',False,(0,0,0))
    window.blit(texto,(100,575))

    texto = dicionario['fonte'].render('- para ir na tela do chefao precisa 20xp que ganha comendo a maça laranja',False,(0,0,0))
    window.blit(texto,(100,600))

    texto = dicionario['fonte'].render('- cuidado!! ao enfrentar o chefao você precisa ter 20xp para remover ele',False,(0,0,0))
    window.blit(texto,(100,625))

    texto = dicionario['fonte'].render('Clique ENTER para iniciar e bom jogo!',False,(0,0,0))
    window.blit(texto,(100, 675))
    pygame.display.update()

def game_loop_inicial(window,dicionario,estado):
    while recebe_eventos():
        if vaijogo:
            window,dicionario,estado = tela_jogo.inicializa()
            fecha_jogo = tela_jogo.game_loop(window,dicionario,estado)#IMPORTANTE PARA TROCAR DE TELAS
            if fecha_jogo == False:
                return False
        else:
            desenha(window,dicionario)
    
w,d,estado= inicializa()
game_loop_inicial(w,d,estado)





    
