import pygame
import math
import constroi_terreno
import transforma_terreno


AGUA = (30, 144, 255)
AREIA = (244, 164, 96)
FLORESTA  = (34, 139, 34)
GRAMA = (124, 252, 0)
MONTANHA = (139, 137, 137)

variavel = {
    "AGUA": AGUA,
    "AREIA": AREIA,
    "FLORESTA": FLORESTA,
    "GRAMA": GRAMA,
    "MONTANHA": MONTANHA
}

CUSTO = {
    AGUA: 180,
    AREIA: 20,
    FLORESTA: 100,
    GRAMA: 10,
    MONTANHA: 150
}

pygame.init()

LARGURA = 800
ALTURA = 800
TAMANHO = 19

tela = pygame.display.set_mode((LARGURA, ALTURA))

LINHA = 42
COLUNA = 42

terreno = constroi_terreno.retorna_terreno()
masmorra1 = constroi_terreno.retorna_masmorra1()
masmorra2 = constroi_terreno.retorna_masmorra2()
masmorra3 = constroi_terreno.retorna_masmorra3()
transformado = transforma_terreno.transforma_terreno(terreno, variavel)


inicio = (27,24)
destino1 = (32,5)
destino2 = (17,39)
destino3 = (2,25)
espada = (2,3)


def verifica_distancia(primeiro_ponto, segundo_ponto):
    x1,y1 = primeiro_ponto
    x2,y2 = segundo_ponto
    return math.sqrt(((x2-x1)**2) + ((y2 - y1)**2))


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
    pygame.draw.rect(tela, (0,255,242), (ponto_partida[1] * TAMANHO, ponto_partida[0]*TAMANHO, TAMANHO, TAMANHO))

    pygame.draw.rect(tela, (79,79,79), (ponto_chegada[1] * TAMANHO, ponto_chegada[0]*TAMANHO, TAMANHO, TAMANHO))

    pygame.display.update()
    pygame.time.wait(100)
        
    for quadrado in caminho_recente:
        x, y = quadrado
        rect = pygame.Rect(y * TAMANHO, x * TAMANHO, TAMANHO, TAMANHO)
        pygame.draw.rect(tela, (255,0,0), rect)
        pygame.display.update()
        pygame.time.wait(100)


def algoritmo_estrela(transformado, ponto_partida, ponto_chegada):
    espacos = [[Celula((linha, coluna), CUSTO[transformado[linha][coluna]])
                for coluna in range(COLUNA)] for linha in range(LINHA)]
    
    for linha in range(LINHA):
        for coluna in range(COLUNA):
            if linha > 0:
                espacos[linha][coluna].vizinhos.append(espacos[linha-1][coluna])
            if linha < LINHA-1:
                espacos[linha][coluna].vizinhos.append(espacos[linha+1][coluna])
            if coluna > 0:
                espacos[linha][coluna].vizinhos.append(espacos[linha][coluna-1])
            if coluna < COLUNA-1:
                espacos[linha][coluna].vizinhos.append(espacos[linha][coluna+1])


    aberta = []
    fechada = []

    lugar_atual = espacos[ponto_partida[0]][ponto_partida[1]]
    aberta.append(lugar_atual)

    while aberta:
        lugar_atual = min(aberta, key=lambda quadrado: quadrado.f + quadrado.h)

        if lugar_atual.posicao == ponto_chegada:
            caminho = []
            custo_total = 0
            while lugar_atual:
                caminho.append(lugar_atual.posicao)
                lugar_atual = lugar_atual.pai
                if lugar_atual:
                    custo_total =+ lugar_atual.custo
            return (caminho[::-1], custo_total)

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


for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()

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



        pygame.draw.rect(tela, cor, (coluna * TAMANHO,
                            linha * TAMANHO, TAMANHO-1, TAMANHO-1))
        

destinos =  [destino1, destino2, destino3]
menor = 100000000000
indice_destino = 0
partida = inicio
caminho_atual = []

while destinos:
    for i, melhor_caminho in enumerate(destinos):
        caminho, custo_total = algoritmo_estrela(transformado, partida, melhor_caminho)
        if(menor > custo_total):
            menor = custo_total
            indice_destino = i
            caminho_atual = caminho
    
    montar_caminho(caminho_atual, partida, destinos[indice_destino])
    partida = destinos[indice_destino]
    destinos.remove(destinos[indice_destino])
    menor = 100000000000

pygame.display.update()