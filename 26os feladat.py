
#fájl vizsgálata
try:
    fajl = open('data.txt','r',encoding='utf-8')
except:
    fajl = open('data.txt', 'w', encoding='utf-8')
    fajl.writelines('angol-magyar\n')


def bővítés(angol,magyar):
    string=angol+'-'+magyar+'\n'  #az adott szó
    szotar=open('data.txt','r',encoding='utf-8')
    tmp=szotar.readlines()
    tmp.append(string)  #hozzá adja a többihez
    szotar=open('data.txt', 'w', encoding='utf-8')
    for i in range(len(tmp)):
        szotar.writelines(tmp[i]) #beírja a szótárba

def fordítás(irany,szo):
    if 'a' ==irany:
        adat=open('data.txt','r',encoding='utf-8')
        tmp=adat.readlines()
        for i in range(len(tmp)):
            if tmp[i].strip().split('-')[0] in szo:
                return tmp[i].strip().split('-')[0]+' '+tmp[i].strip().split('-')[1]
        print('Nincs ilyen szó az adatbázisban!')
    elif 'm' == irany:
        adat=open('data.txt','r',encoding='utf-8')
        tmp=adat.readlines()
        for i in range(len(tmp)):
            if tmp[i].strip().split('-')[1] in szo:
                return tmp[i].strip().split('-')[0]+' '+tmp[i].strip().split('-')[1]
        print('Nincs ilyen szó az adatbázisban!')

def kezdo():
    tmp = input('Bővítés vagy fordítás? (b/f) ')
    if 'b' == tmp:
            szavak=input('Add meg a szavakat szóközzel elválasztva!\n\n angol magyar\n ').split(' ')
            bővítés(szavak[0], szavak[1])
    elif 'f' == tmp:
        tmp = input('Add meg, hogy melyik nyelvről akarsz fordítani? (a/m) ')
        if tmp == 'a' or tmp=='m':
            szo=input('Add meg a szót:')
            print('angol magyar\n{}'.format(fordítás(tmp,szo)))


print(kezdo())