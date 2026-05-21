# pyrefly: ignore [missing-import]
import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

# Tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Space Invaders - Estilo Atari")

# Relógio e Fonte
FPS = 60
relogio = pygame.time.Clock()
fonte = pygame.font.Font(None, 36)

# Jogador
jogador_largura = 40
jogador_altura = 20
jogador_x = LARGURA // 2 - jogador_largura // 2
jogador_y = ALTURA - 50
jogador_velocidade = 5

# Tiro do jogador
tiros = []
tiro_velocidade = -7

# Inimigos
inimigos = []
inimigo_largura = 30
inimigo_altura = 30
linhas_inimigos = 4
colunas_inimigos = 10

def criar_inimigos():
    for linha in range(linhas_inimigos):
        for coluna in range(colunas_inimigos):
            x = 50 + coluna * (inimigo_largura + 20)
            y = 50 + linha * (inimigo_altura + 20)
            inimigos.append(pygame.Rect(x, y, inimigo_largura, inimigo_altura))

criar_inimigos()

direcao_inimigos = 1
velocidade_inimigos_x = 2
velocidade_inimigos_y = 10

pontuacao = 0
estado = "jogando"

# Loop Principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            # Atirar com espaço
            if evento.key == pygame.K_SPACE and estado == "jogando":
                # Limita a 3 tiros na tela para dar sensação retro
                if len(tiros) < 3:
                    tiros.append(pygame.Rect(jogador_x + jogador_largura // 2 - 2, jogador_y, 4, 10))
            # Reiniciar com Enter
            if evento.key == pygame.K_RETURN and estado != "jogando":
                estado = "jogando"
                inimigos.clear()
                criar_inimigos()
                pontuacao = 0
                tiros.clear()
                jogador_x = LARGURA // 2 - jogador_largura // 2

    if estado == "jogando":
        # Controles
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and jogador_x > 0:
            jogador_x -= jogador_velocidade
        if teclas[pygame.K_RIGHT] and jogador_x < LARGURA - jogador_largura:
            jogador_x += jogador_velocidade

        # Move tiros
        for tiro in tiros[:]:
            tiro.y += tiro_velocidade
            if tiro.y < 0:
                tiros.remove(tiro)

        # Move inimigos
        mover_baixo = False
        for inimigo in inimigos:
            inimigo.x += velocidade_inimigos_x * direcao_inimigos
            if inimigo.right >= LARGURA or inimigo.left <= 0:
                mover_baixo = True

        if mover_baixo:
            direcao_inimigos *= -1
            for inimigo in inimigos:
                inimigo.y += velocidade_inimigos_y

        # Colisões
        for tiro in tiros[:]:
            acertou = False
            for inimigo in inimigos[:]:
                if tiro.colliderect(inimigo):
                    inimigos.remove(inimigo)
                    pontuacao += 10
                    acertou = True
                    break
            if acertou:
                tiros.remove(tiro)

        # Verifica game over ou vitória
        if not inimigos:
            estado = "vitoria"
            
        for inimigo in inimigos:
            if inimigo.bottom >= jogador_y:
                estado = "gameover"

    # Desenho na tela
    tela.fill(PRETO)
    
    if estado == "jogando":
        # Desenha jogador
        pygame.draw.rect(tela, VERDE, (jogador_x, jogador_y, jogador_largura, jogador_altura))
        # Desenha tiros
        for tiro in tiros:
            pygame.draw.rect(tela, BRANCO, tiro)
        # Desenha inimigos
        for inimigo in inimigos:
            pygame.draw.rect(tela, BRANCO, inimigo)
            
        # Placar
        texto_pontos = fonte.render(f"Pontos: {pontuacao}", True, BRANCO)
        tela.blit(texto_pontos, (10, 10))
    else:
        # Telas de fim de jogo
        msg = "GAME OVER" if estado == "gameover" else "VITÓRIA!"
        cor = VERMELHO if estado == "gameover" else VERDE
        texto = fonte.render(msg, True, cor)
        texto2 = fonte.render("Pressione ENTER para reiniciar", True, BRANCO)
        tela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, ALTURA // 2 - 30))
        tela.blit(texto2, (LARGURA // 2 - texto2.get_width() // 2, ALTURA // 2 + 20))

    pygame.display.flip()
    relogio.tick(FPS)

pygame.quit()
sys.exit()
