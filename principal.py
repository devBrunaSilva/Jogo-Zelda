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

custo = {
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
    return verifica_distancia(lugar_atual.posica, destino1)*10

def custo(lugar_atual, vizinho):
    if vizinho in lugar_atual.vizinhos:
        return lugar_atual.custo + vizinho.custo
    else:
        return float('inf')
    

def montar_caminho(caminho_recente, ponto_partida, ponto_chegada):
    pygame.draw.rect(tela, (0,255,242), (ponto_partida[1] * TAMANHO, ponto_partida[0]*TAMANHO, TAMANHO, TAMANHO))
        

pygame.display.update()