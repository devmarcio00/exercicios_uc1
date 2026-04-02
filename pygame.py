import pygame
import random

# Inicializar
pygame.init()

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

# Tela
largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

clock = pygame.time.Clock()

tamanho_bloco = 10
velocidade = 15

font = pygame.font.SysFont(None, 35)

def mensagem(msg, cor):
    texto = font.render(msg, True, cor)
    tela.blit(texto, [largura / 6, altura / 3])

def jogo():
    fim = False
    game_over = False

    x = largura / 2
    y = altura / 2

    dx = 0
    dy = 0

    cobrinha = []
    tamanho = 1

    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 10.0) * 10.0

    while not fim:

        while game_over:
            tela.fill(preto)
            mensagem("Game Over! C = jogar de novo | Q = sair", vermelho)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        fim = True
                        game_over = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    dx = -tamanho_bloco
                    dy = 0
                elif evento.key == pygame.K_RIGHT:
                    dx = tamanho_bloco
                    dy = 0
                elif evento.key == pygame.K_UP:
                    dy = -tamanho_bloco
                    dx = 0
                elif evento.key == pygame.K_DOWN:
                    dy = tamanho_bloco
                    dx = 0

        # Bateu na parede
        if x >= largura or x < 0 or y >= altura or y < 0:
            game_over = True

        x += dx
        y += dy
        tela.fill(preto)

        pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        cabeca = []
        cabeca.append(x)
        cabeca.append(y)
        cobrinha.append(cabeca)

        if len(cobrinha) > tamanho:
            del cobrinha[0]

        for bloco in cobrinha[:-1]:
            if bloco == cabeca:
                game_over = True

        for bloco in cobrinha:
            pygame.draw.rect(tela, branco, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])

        pygame.display.update()

        # Comeu a comida
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 10.0) * 10.0
            tamanho += 1

        clock.tick(velocidade)

    pygame.quit()
    quit()

jogo()