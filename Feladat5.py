def rendezes(szavak):
    szavak.sort()
    ujlista = []
    for i in szavak:
        if i not in ujlista:
            ujlista.append(i)
    return ujlista

szavak = ['red', 'white', 'black', 'red', 'green', 'black']
print(rendezes(szavak))