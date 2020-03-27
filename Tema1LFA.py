f = open ("input.in", "r")
sir = f.readline()
sir = sir[:-1]

lst_finale = []
nr = int(f.readline())

lst_liste = [[[] for i in range(30)] for i in range(nr)]
finale = int(f.readline())
lst_finale = f.readline().split()
for x in f:
    l = x.split()
    lst_liste [int(l[0])][int(l[1])].append(l[2])

print (lst_liste)

def ParcurgereSir(ch):
        global curent
        gasit = 0
        for i in range(nr):
            for x in lst_liste[curent][i]:
                if x == ch:
                    curent = i
                    gasit = 1
                    break
            if gasit == 1:
                return 1
        if gasit == 0:
            return 0

curent = 0
ok = 1
for ch in sir:
    if ParcurgereSir(ch) == 0:
        print ("Nu este acceptat")
        ok = 0
        break

if ok == 1:
    if str(curent) in lst_finale:
        print("Este acceptat")
    else:
        print("Nu este acceptat")
