tipo_terreno = {
    "g": "GRAMA",
    "a": "AREIA",
    "f": "FLORESTA",
    "m": "MONTANHA",
    "w": "AGUA"
}

terreno = []
masmorra1 = []
masmorra2 = []
masmorra3 = []

with open("./terreno.txt", "r") as arquivo:
    mapa = arquivo.readlines()
    for linha in mapa:
        temp = []
        for caractere in linha:
            if caractere != '\n':
                temp.append(tipo_terreno[caractere])
        terreno.append(temp)

with open("./masmorra1.txt", "r") as arquivo:
    mapa = arquivo.readlines()
    for linha in mapa:
        temp = []
        for caractere in linha:
            if caractere != '\n':
                temp.append(tipo_terreno[caractere])
        masmorra1.append(temp)

with open("./masmorra2.txt", "r") as arquivo:
    mapa = arquivo.readlines()
    for linha in mapa:
        temp = []
        for caractere in linha:
            if caractere != '\n':
                temp.append(tipo_terreno[caractere])
        masmorra2.append(temp)

with open("./masmorra3.txt", "r") as arquivo:
    mapa = arquivo.readlines()
    for linha in mapa:
        temp = []
        for caractere in linha:
            if caractere != '\n':
                temp.append(tipo_terreno[caractere])
        masmorra3.append(temp)

def retorna_terreno():
    return terreno

def retorna_masmorra1():
    return masmorra1

def retorna_masmorra2():
    return masmorra2

def retorna_masmorra3():
    return masmorra3