from random import*
print("Tahad mängida? (1 - jah/0 - ei)")
while 1:
    try:
        vastus=int(input("=> "))
        if vastus == 1: 
            break
        elif vastus == 0:
            print("Kahju :( ")
            exit()
    except ValueError:
        print("Vale andmetüüp!")
while 1:
    try:
        slovo=str(input("Palun siseta sõna minimaalselt viiest tähest => "))
        if len(slovo)==5: break
    except ValueError:
        print("Siseta rohkem tähti!")
slovo_list=list(slovo)
print(slovo)
if slovo_list.istitle()==True:
    print("Sinu sõna algab suure algustähega")
    slovo_list.lower()
    print("Aga me natukene töötasime, ning praegu sinu sõna algab väikse algustähega")
    print(slovo_list)
else:
    print("Sinu sõna algab väikse algustähega")
    slovo_list.upper()
    print("Aga me natukene töötasime, ning praegu sinu sõna algab suure algustähega")
    print(slovo_list)
slovo_list.shuffle()
print("Nüüd ma tegin niimodi, et kõik tähed läksid segamini")
print(slovo_list)
slovo_list.reverse()
print("Aga nüüd kõik tähed vahetasid oma kohta. Wow, mis siin toimub??")
print(slovo_list)
slovo_list.copy()
slovo_list.clear()
print("Oi, kui pahasti, kõik läks katki. Sinu sõna on kustutatud")
print(slovo_list)
print("Hah, see oli lihtsalt nali. Kõik on korras :) ")
print(slovo_list)
print("Aitäh, et võttis minu projekti jaoks aega")