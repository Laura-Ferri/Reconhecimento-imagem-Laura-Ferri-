import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Definindo cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Configurações da tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pong - Estilo Atari")

# Configurações do jogo
FPS = 60
relogio = pygame.time.Clock()

# Raquetes e Bola
raquete_largura = 15
raquete_altura = 100
bola_tamanho = 15

# Posições iniciais
jogador1_x = 50
jogador1_y = ALTURA // 2 - raquete_altura // 2
jogador2_x = LARGURA - 50 - raquete_largura
jogador2_y = ALTURA // 2 - raquete_altura // 2

bola_x = LARGURA // 2 - bola_tamanho // 2
bola_y = ALTURA // 2 - bola_tamanho // 2

# Velocidades
velocidade_raquete = 7
bola_velocidade_x = 5
bola_velocidade_y = 5

# Pontuação
pontos_jogador1 = 0
pontos_jogador2 = 0
fonte = pygame.font.Font(None, 74)

def desenhar_elementos():
    tela.fill(PRETO)
    # Linha central tracejada (estilo Atari)
    for y in range(0, ALTURA, 30):
        pygame.draw.rect(tela, BRANCO, (LARGURA // 2 - 2, y, 4, 15))
        
    # Raquetes
    pygame.draw.rect(tela, BRANCO, (jogador1_x, jogador1_y, raquete_largura, raquete_altura))
    pygame.draw.rect(tela, BRANCO, (jogador2_x, jogador2_y, raquete_largura, raquete_altura))
    
    # Bola
    pygame.draw.rect(tela, BRANCO, (bola_x, bola_y, bola_tamanho, bola_tamanho))
    
    # Placar
    texto_p1 = fonte.render(str(pontos_jogador1), True, BRANCO)
    tela.blit(texto_p1, (LARGURA // 4, 20))
    
    texto_p2 = fonte.render(str(pontos_jogador2), True, BRANCO)
    tela.blit(texto_p2, (LARGURA * 3 // 4, 20))
    
    pygame.display.flip()

# Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Controles
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and jogador1_y > 0:
        jogador1_y -= velocidade_raquete
    if teclas[pygame.K_s] and jogador1_y < ALTURA - raquete_altura:
        jogador1_y += velocidade_raquete
        
    if teclas[pygame.K_UP] and jogador2_y > 0:
        jogador2_y -= velocidade_raquete
    if teclas[pygame.K_DOWN] and jogador2_y < ALTURA - raquete_altura:
        jogador2_y += velocidade_raquete

    # Movimentação da bola
    bola_x += bola_velocidade_x
    bola_y += bola_velocidade_y

    # Colisão com o teto e chão
    if bola_y <= 0 or bola_y >= ALTURA - bola_tamanho:
        bola_velocidade_y *= -1

    # Colisão com as raquetes
    # Criando retângulos para colisão
    rect_bola = pygame.Rect(bola_x, bola_y, bola_tamanho, bola_tamanho)
    rect_jogador1 = pygame.Rect(jogador1_x, jogador1_y, raquete_largura, raquete_altura)
    rect_jogador2 = pygame.Rect(jogador2_x, jogador2_y, raquete_largura, raquete_altura)

    if rect_bola.colliderect(rect_jogador1) or rect_bola.colliderect(rect_jogador2):
        bola_velocidade_x *= -1
        # Para evitar que a bola fique presa dentro da raquete
        if bola_velocidade_x > 0:
            bola_x = jogador1_x + raquete_largura + 1
        else:
            bola_x = jogador2_x - bola_tamanho - 1

    # Pontuação (quando a bola sai pelas laterais)
    if bola_x <= 0:
        pontos_jogador2 += 1
        bola_x = LARGURA // 2 - bola_tamanho // 2
        bola_y = ALTURA // 2 - bola_tamanho // 2
        bola_velocidade_x *= -1
    elif bola_x >= LARGURA:
        pontos_jogador1 += 1
        bola_x = LARGURA // 2 - bola_tamanho // 2
        bola_y = ALTURA // 2 - bola_tamanho // 2
        bola_velocidade_x *= -1

    # Atualiza a tela
    desenhar_elementos()
    
    # Controla o FPS
    relogio.tick(FPS)

pygame.quit()
sys.exit()
