tipo=input()
ipo=input()
po=input()

if tipo=="vertebrado":
    if ipo=="ave":
        if po=="carnivoro":
            print('aguia')
        elif po=="onivoro":
            print('pomba')
    elif ipo=="mamifero":
        if po=="onivoro":
            print('homem')
        elif po=="herbivoro":
            print('vaca')
elif tipo=="invertebrado":
    if ipo=="inseto":
        if po=="hematofago":
            print('pulga')
        elif po=="herbivoro":
            print('lagarta')
    elif ipo=="anelideo":
        if po=="hematofago":
            print('sanguessuga')
        elif po=="onivoro":
            print('minhoca')
