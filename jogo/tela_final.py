import pygame

widht = 1200
height = 800
def inicializa():
    pygame.init()
    window = pygame.display.set_mode((widht,height))
    pygame.display.set_caption('RETRO SNAKE')

    dicionario = {}
    dicionario['game over'] = pygame.image.load('imagens/game over.png')

    dicionario['img_cobra_morta'] = pygame.image.load('imagens/cobra_morta.png')
    dicionario['cobra_morta'] = pygame.transform.scale(dicionario['img_cobra_morta'],(300,300))

    dicionario['fonte'] = pygame.font.Font('fonte/perfect_dos_vga_437/Perfect DOS VGA 437 Win.ttf',25)

    dicionario['som_game_over'] = 'sons/game-over-arcade-6435.mp3'
    pygame.mixer.music.load(dicionario['som_game_over'])
    pygame.mixer.music.play()

    return window,dicionario

def recebe_eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return False
        
    return True

def desenha(window,dicionario):
    window.fill((0,149,0))
    
    window.blit(dicionario['game over'],(widht - 850,height - 750))

    window.blit(dicionario['cobra_morta'],(450,220))

    texto = dicionario['fonte'].render('Pressione ENTER para recomeçar', False, (0,0,0))
    window.blit(texto,(390,530))
    
    morte = dicionario['fonte'].render(f"Você morreu por: {dicionario['morte']}", False, (0,0,0))
    window.blit(morte, (390,555))

    pygame.display.update()

def game_loop(window,dicionario):
    while recebe_eventos():
        desenha(window,dicionario)
