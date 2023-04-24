import pygame


def monta_terreno(transformado, LINHA, COLUNA, AGUA, AREIA, FLORESTA, GRAMA, MONTANHA, AMARELO, BRANCO, PRETO, TAMANHO, janela):

  for linha in range(LINHA):
    for coluna in range(COLUNA):
        if transformado[linha][coluna] == AGUA:
          cor = (45,72,181)
        elif transformado[linha][coluna] == AREIA:
          cor = (196,188,148)
        elif transformado[linha][coluna] == FLORESTA:
          cor = (1,115,53)
        elif transformado[linha][coluna] == GRAMA:
          cor = (140,211,70)
        elif transformado[linha][coluna] == MONTANHA:
          cor = (82,70,44)
        elif transformado[linha][coluna] == AMARELO:
          cor = (201, 176, 10)
        elif transformado[linha][coluna] == BRANCO:
          cor = (255, 255, 255)
        elif transformado[linha][coluna] == PRETO:
          cor = (0, 0, 0)
        


        pygame.draw.rect(janela, cor, (coluna * TAMANHO, linha * TAMANHO, TAMANHO-1, TAMANHO-1))
