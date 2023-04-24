import pygame
import math
import constroi_terreno
import transforma_terreno

def masmorras(area, valor_masmorra):
  AREIA = (244, 164, 96)
  MONTANHA = (139, 137, 137)

  variavel = {
    "AREIA": AREIA,
    "MONTANHA": MONTANHA,
  }

  CUSTO = {
    AREIA: 20,
    MONTANHA: 150,
  }


  pygame.init()

  LARGURA = 700
  ALTURA = 700
  TAMANHO = 25

  janela = pygame.display.set_mode((LARGURA, ALTURA))


  LINHAS = 28
  COLUNAS = 28

  transformado = transforma_terreno.transforma_terreno(area, variavel)


  if valor_masmorra == 1:
    partida = (26, 14)
    destino = (3, 13)
  elif valor_masmorra == 2:
    partida = (25, 13)
    destino = (2, 13)
  elif valor_masmorra == 3:
    partida = (25, 14)
    destino = (19, 15)

  def verifica_distancia(primeiro_ponto, segundo_ponto):
    x1, y1 = primeiro_ponto
    x2, y2 = segundo_ponto
    return math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
  

  class Celula:
    def __init__(self, posicao, custo):
      self.posicao = posicao
      self.custo = custo
      self.vizinhos = []
      self.g = 0
      self.h = 0
      self.f = 0
      self.pai = None
      self.visitada = False

    def reset(self):
      self.g = 0
      self.h = 0
      self.f = 0
      self.pai = None
      self.visitada = False
  

  def heuristica(lugar_atual, destino1):
    return verifica_distancia(lugar_atual.posicao, destino1)*10

  def custo(lugar_atual, vizinho):
    if vizinho in lugar_atual.vizinhos:
        return lugar_atual.custo + vizinho.custo
    else:
        return float('inf')

  def montar_caminho(caminho_recente, ponto_partida, ponto_chegada):

      #Monta o ponto de partida
    pygame.draw.rect(janela, (0,255,242), (ponto_partida[1] * TAMANHO, ponto_partida[0]*TAMANHO, TAMANHO - 1, TAMANHO - 1))

      #Monta o ponto de destino
    pygame.draw.rect(janela, (0,250,229), (ponto_chegada[1] * TAMANHO,  ponto_chegada[0]*TAMANHO, TAMANHO - 1, TAMANHO - 1)) 

    tempo = pygame.time.Clock()
    caminho = caminho_recente +  caminho_recente[::-1]
    
    for i, espaco in enumerate(caminho):
      x, y = espaco
      cor = (255, 0, 0)

      if i>= len(caminho)/2:
        cor = (255, 165, 0)

      rect = pygame.Rect(y * TAMANHO, x * TAMANHO, TAMANHO -1, TAMANHO - 1)
      janela.fill(cor, rect=rect)
      pygame.display.update()
      tempo.tick(7)
  

  def algoritmo_estrela(transformado, ponto_partida, ponto_chegada):
    espacos = [[Celula((linha, coluna), CUSTO[transformado[linha][coluna]])
                for coluna in range(COLUNAS)] for linha in range(LINHAS)]
    

    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            if linha > 0:
                espacos[linha][coluna].vizinhos.append(espacos[linha-1][coluna])
            if linha < LINHAS-1:
                espacos[linha][coluna].vizinhos.append(espacos[linha+1][coluna])
            if coluna > 0:
                espacos[linha][coluna].vizinhos.append(espacos[linha][coluna-1])
            if coluna < COLUNAS-1:
                espacos[linha][coluna].vizinhos.append(espacos[linha][coluna+1])


    aberta = []
    fechada = []

    lugar_atual = espacos[ponto_partida[0]][ponto_partida[1]]
    aberta.append(lugar_atual)

    while aberta:
        lugar_atual = min(aberta, key=lambda quadrado: quadrado.f + quadrado.h)

        if lugar_atual.posicao == ponto_chegada:
            caminho = []
            while lugar_atual:
                caminho.append(lugar_atual.posicao)
                lugar_atual = lugar_atual.pai
                
            return (caminho[::-1])

        aberta.remove(lugar_atual)
        fechada.append(lugar_atual)

        for vizinho in lugar_atual.vizinhos:
            if vizinho in fechada:
                continue

            novo_g = lugar_atual.g + custo(lugar_atual,vizinho)

            if vizinho not in aberta:
                aberta.append(vizinho)
            elif novo_g >= vizinho.g:
                continue


            vizinho.g = novo_g
            vizinho.h = heuristica(vizinho, ponto_chegada)
            vizinho.f = vizinho.g + vizinho.h
            vizinho.pai = lugar_atual
    
    return None
  

  for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        if transformado[linha][coluna] == AREIA:
            cor = (196, 188, 148)
        elif transformado[linha][coluna] == MONTANHA:
            cor = (82, 70, 44)



        pygame.draw.rect(janela, cor, (coluna * TAMANHO,
                            linha * TAMANHO, TAMANHO-1, TAMANHO-1))

  
  caminho = algoritmo_estrela(transformado, partida, destino)

  montar_caminho(caminho, partida, destino)

  janela = pygame.display.set_mode((LARGURA, ALTURA))

  pygame.display.update()

