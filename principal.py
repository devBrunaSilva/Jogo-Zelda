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

terreno = constroi_terreno.terreno()
dungeon1 = constroi_terreno.dungeon1()
dungeon2 = constroi_terreno.dungeon2()
dungeon3 = constroi_terreno.dungeon3()
transformado = transforma_terreno.converte(terreno, variavel)
