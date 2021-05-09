import numpy as np
beolvas = open('input.txt', 'r', encoding='utf-8')
beolvas=beolvas.readlines()

melybetuk = ['a', 'á', 'o', 'ó', 'u', 'ú']
magasbetuk = ['e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű']
magasszavak = []
melyszavak = []
vegyesszavak = []

def vizsgal(beolvas, melybetuk, magasbetuk):
    vektor = np.zeros(len(beolvas)) #nullával teli vektor a beolvas sztring hosszával megegyezően
    for i in range(len(beolvas)):
        if beolvas[i] in melybetuk:
            vektor[i] = 1
        elif beolvas[i] in magasbetuk:
            vektor[i] = 2

    if 1 in vektor and 2 not in vektor:
        return melyszavak.append(beolvas + '\n')
    elif 1 not in vektor and 2 in vektor:
        return magasszavak.append(beolvas + '\n')
    else:
        return vegyesszavak.append(beolvas + '\n')

for i in range(len(beolvas)): #meghívja a függvényt a fájl összes szavára
    vizsgal(beolvas[i],melybetuk, magasbetuk)

melyfajl = open('mely.txt', 'w', encoding='utf-8')
for i in melyszavak:
    melyfajl.writelines(i)
magasfajl = open('magas.txt', 'w', encoding='utf-8')
for i in magasszavak:
    magasfajl.writelines(i)
vegyesfajl = open('vegyes.txt', 'w', encoding='utf-8')
for i in vegyesszavak:
    vegyesfajl.writelines(i)

