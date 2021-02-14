def szoreszlet(szo, n):
    if len(szo) < 3:
        return szo
    else:
        tő = szo[:n]
        return tő


print(szoreszlet(input("Adjon meg egy szót: "), int(input("Adja meg hány betűt írjunk ki: "))))
