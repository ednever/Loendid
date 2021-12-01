#Kmd=[] #tühi järjend
#Km=10 #esimene päev
#print("1. päeval pikkus oli ",Km)
#Kmd.append(Km)
#for i in range(2,8):
#    Km*=1.1 # > 10%
#    Kmd.append(round(Km,2))
#print(Kmd)
#print(Kmd[2])
#print(Kmd.index(16.11)+1)
#Kmd.remove(10) #pop(0)
#print(Kmd,"liistis on kokku ",Kmd.count(16.11)," elementi mis võrduvad 16.11")
#print(len(Kmd)," on jäänud listis")


                            # Задание 1 Сделано

#Maakonnad=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
#while 1:
#    try:
#        indeks=int(input("Indeks - "))
#        if len(str(indeks))==5: break
#    except ValueError:
#        print("Valesti sisetatud indeks!")
#i_list=list(str(indeks))
#s1=int(i_list[0]) #1->0, 2->1...
#print(Maakonnad[s1-1])
#if s1 in [1,2,3]:
#    print("Jätke koju!")
#else:
#    print("Kanna maski!")

                            # Задание 2 Сделано

#from random import*
#spisok=[]
#while 1:
#    try:
#        N=int(input("N - "))
#        if len(str(N))==2: break
#    except ValueError:
#        print("Rohkem kui")
#for i in range(N):
#    spisok.append(randint(1,100))
#print(spisok)
#esimene=spisok[0]
#viimane=spisok[N-1]
#spisok.pop(0)
#spisok.insert(0,viimane)
#spisok.pop()
#spisok.append(esimene)
#print(spisok)
#print()
#vastus=""
#while type(vastus)!=int or vastus not in [0,1]:
#    try:
#        vastus=int(input("Kas tahad jätkata? (Jah-1/Ei-0) - "))
#    except ValueError:
#        print("Vale andmetüüp!")
#if vastus==1:
#    teine=spisok[1]
#    eelviimane=spisok[N-2]
#    spisok.pop(1)
#    spisok.insert(1,eelviimane)
#    spisok.pop(N-2)
#    spisok.insert(N-2,teine)
#    print(spisok)
#    print()
#    vastus2=""
#    while type(vastus2)!=int or vastus2 not in [0,1]:
#        try:
#            vastus2=int(input("Kas tahad jätkata veel? (Jah-1/Ei-0) - "))
#        except ValueError:
#            print("Vale andmetüüp!")
#    if vastus2==1:
#        kolmas=spisok[2]
#        eeleelviimane=spisok[N-3]
#        spisok.pop(2)
#        spisok.insert(2,eeleelviimane)
#        spisok.pop(N-3)
#        spisok.insert(N-3,kolmas)
#        print(spisok)
#        print("Tubli, tõõ on tehtud!")
#    else:
#        print("Kahju :(")
#else:
#    print("Kahju :(")

#print(spisok)
#spisok.copy()
#spisok.reverse()
#print(spisok)

                         # Задание 3 Сделано

#from random import*
#spisok=[]
#while 1:
#    try:
#        N=int(input("N - "))
#        if len(str(N))==2: break
#    except ValueError:
#        print("Rohkem kui")
#for i in range(N):
#    spisok.append(randint(1,100))
#print(spisok)
#spisok.copy()
#viimane=max(spisok)
#print(viimane)
#vastus=viimane/N
#print(vastus)
#ind=spisok.index(viimane)
#spisok.pop(ind)
#spisok.insert(ind,vastus)
#print(spisok)

                       # Задание 4 Сделано

#from random import*
#spisok=[]
#spisok_=[]
#while 1:
#    try:
#        N=int(input("N - "))
#        if len(str(N))==2: break
#    except:
#        ValueError
#for i in range(N):
#    spisok.append(randint(-100,100))
#print(spisok)
#for n in spisok:
#    spisok_.append(abs(n))
#spisok_.sort()
#print("По возрастанию - ",spisok_)
#spisok_.sort(reverse=True)
#print("По убыванию - ",spisok_)

                     # Задание 5 Сделано

#from random import*
#spisok1=["крот","белка","выхухоль"]
#spisok2=["a","aa","aaa","aaaa","aaaaa"]
#spisok3=["qweasdqweas","q","rteww","ewqqqqq"]
#spisok1_=[]
#spisok2_=[]
#spisok3_=[]
#pikkem=0
#for spisok in spisok1:
#    pikkus=len(spisok)
#    if pikkus>pikkem: pikkem=pikkus
#for spisok in spisok1:
#    spisok1_.append(spisok.ljust(pikkem,"_"))
#print(spisok1_)

#for spisok in spisok2:
#    pikkus=len(spisok)
#    if pikkus>pikkem: pikkem=pikkus
#for spisok in spisok2:
#    spisok2_.append(spisok.ljust(pikkem,"_"))
#print(spisok2_)

#for spisok in spisok3:
#    pikkus=len(spisok)
#    if pikkus>pikkem: pikkem=pikkus
#for spisok in spisok3:
#    spisok3_.append(spisok.ljust(pikkem,"_"))
#print(spisok3_)

#from random import*
#s1=["крот","белка","выхухоль"]
#s2=["a","aa","aaa","aaaa","aaaaa"]
#s3=["qweasdqweas","q","rteww","ewqqqqq"]
#ss=[s1,s2,s3]
#N=0
#while N<3:
#    print(ss[N])
#    pikkem=0
#    sN_=[]
#    for s in ss[N]:
#        pikkus=len(s)
#        if pikkus>pikkem: pikkem=pikkus
#    for s in ss[N]:
#        sN_.append(s.ljust(pikkem,"_"))
#    print(sN_)
#    N+=1
