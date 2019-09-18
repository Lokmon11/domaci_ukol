
import time
import random

#kostky...

#Část 1. Rozhovory a texty:

#mezera
def mez(smycka=1):
    for i in range(smycka):
        print('.')
        time.sleep(0.5)

#Úvodní text
def text_1():
    print('Vítej u mého úkolu :P')
    mez(smycka=2)
    print('KOSTKY! KOSTKY! KOSTKY!')
    print('By Lokmon')
    mez(smycka=5)

    print('Je teplý podzimní večer a ty ses vydal na procházku po tvém oblíbeném parku při poslechu všemožných vypalovaček.')
    time.sleep(2)
    print('Přestal jsi vnímat všechen ruch okolo a dřív než sis to uvědomil skončil si v nejtemnějším zákoutí parku.')
    time.sleep(2)
    print('Otočil jsi se a chceš odejít když v tom ti zastoupí cestu 3 individua...')
    time.sleep(2)
    print('Dva velcí hromotluci s naštvaným výrazem ve tváří v pomačkaných mikinách a sepraných džínách stáli se skříženýma rukama za, o poznání drobnějším, mladíkem v modré sportovní soupravě.')
    time.sleep(2)

#první rozhovor s volbou
def rozhovor_1():
    while True:
        print('Mladík promluvil mírně pískavým hlasem: "Copak? Ztratil ses?" \n  \n  ')
        print('Odpovědět: 1. Ne, vím přesně kde jsem!')
        print('	   2. Promiň Já nerozuměla Cecky... Kde nád-raczí?')
        print('	   3. Trochu jsem se zamyslel ale cestu pryč najdu. Hlavně nechci žádné problémy...')
        print('	   4. "Utéct" (Ukončí hru)')
        print(' ')
        roz1 = input('Odpovědět:')

        if roz1 == '1':
            print(' \nJá: Ne, vím přesně kde jsem!')
            time.sleep(2)
            print(' \nMladík: Tak jistě víš že jsi v průšvihu...')
            time.sleep(2)
            break

        elif roz1 == '2':
            print(' \nJá: Promiň Já nerozuměla Cecky... Kde nád-raczí?')
            time.sleep(2)
            print(' \nMladík: :D Ten byl dobrej. Koukám že jsi veselá kopa. My dva si budeme rozumět.')
            time.sleep(2)
            break

        elif roz1 == '3':
            print(' \nJá: Trochu jsem se zamyslel ale cestu pryč najdu. Hlavně nechci žádné problémy...')
            time.sleep(2)
            print(' \nMladík: Smůla, problémy si tě našly...')
            time.sleep(2)
            break

        elif roz1 == '4':
            print(' \n"Dáváš se na útěk..."')
            time.sleep(1)

            print(' \nMladík: Dostaňte ho hoši a vymlaťte z něj duši...')
            time.sleep(1)
            print('"I když jsi se snažil, ty dvě gorily tě bez problému dohnaly a udělali z tebe hranatou kouli..."')
            time.sleep(2)
            print('Mladík: Špatná volba, mohli jsme se domluvit...')
            time.sleep(1)
            print('"přicházíš o vědomí, tahle hra pro tebe končí."')
            time.sleep(1)

            print(' \nUkončuji hru...')
            time.sleep(3)
            print(" \nEror 702, the game don't respond")
            time.sleep(3)
            print(' \nSystem response: Restore system to factory settings')
            time.sleep(5)
            quit()

        else:
            print(' \nPřestaň blábolit a odpověz! (odpovíš napsáním čísla odpovědi například "1") \n  ')

#Mezi text
def text_2():
    print('Mladík: Dostal jsi se do špatného kouta parku...')
    time.sleep(2)
    print('Mladík: Sem se bojí chodit i poldové.')
    time.sleep(2)
    print('Mladík: A protože nechceme kazit pověst tohoto místa nemůžeme tě nechat jen tak odejít...')
    time.sleep(2)
    print('Mladík: Na štěstí pro tebe mám dneska dobrou náladu. Co bys řekl na trochu hazardu?')
    time.sleep(2)
    print('Mladík: Zahrajeme si kostky.')
    time.sleep(0.5)
    print('Mladík: Pokud vyhraješ, budeš moct odejít. Ale pokud prohraješ, tak tě trochu pomuchláme...')
    time.sleep(1)

#Druhý rozhovor s volbou
def rozhovor_2():
    while True:
        print('Mladík: Tak co? Hraješ? \n  \n  ')
        print('Odpovědět: 1. Asi nemám na výběr. Jak se to hraje?')
        print('	   2. Ano hraju, tak ať to máme z krku...')
        print('	   3. Trhni si... (ukončit hru) \n  ')
        roz2 = input('Odpovědět:')

        if roz2 == '1':
            print(' \nJá: Asi nemám na výběr. Jak se to hraje?')
            time.sleep(1)

            print(' \nMladík: Správné rozhodnutí.')
            time.sleep(1)
            print('Mladík: Pravidla jsou velmi jednoduchá. Každý hodí 6x kostkou. Když hodíš víc než já vyhraješ, když hodíš méně prohraješ. Pokud hodíš 21 automaticky vyhraješ. Jestliže to bude nerozhodně hází se znovu.')
            time.sleep(2)
            break

        elif roz2 == '2':
            print(' \nJá: Ano hraju, tak ať to máme z krku...')
            time.sleep(1)

            print(' \nMladík: Rovnou k věci. Tomu říkám správný přístup.')
            time.sleep(2)
            break

        elif roz2 == '3':
            print(' \nJá: Trhni si...')
            time.sleep(1)

            print(' \nMladík: Špatné rozhodnutí...')
            time.sleep(1)
            print('Mladík: Na něj hoši. Ukažte mu co děláme těm kteří se zatoulají do našeho kouta parku...')
            time.sleep(3)
            print('"Rozhodl jsi se špatně a tvá cesta zde končí."')
            time.sleep(1)

            print(' \nUkončuji hru...')
            time.sleep(2)
            print(" \nEror 702, the game don't respond")
            time.sleep(2)
            print(' \nSystem response: Restore system to factory settings')
            time.sleep(3)
            quit()

        else:
            print(' \nPřestaň blábolit a odpověz! (odpovíš napsáním čísla odpovědi například "1") \n  ')


#Výhra
def výhra():
    print(' \nBlahopřeji vyhrál jsi hru v kostky.')
    time.sleep(0.5)

#Prohra
def prohra():
    print(' \nJe mi líto ale prohrál jsi.')
    time.sleep(0.5)
    
#Opakování/Ukončení hry
def text3():
    while True:
        print(' \nPřeješ si hrát znovu?')
        print('Odpovědět: 1. Ano! Rozjeď to!')
        print('    2. Ne, dneska mám dost.')
        time.sleep(0.5)
        roz3 = input('Odpovědět:')

        if roz3 == '1':
            print(' \nVýborně. Hrajeme znovu.')
            time.sleep(0.5)
            Kostky()

        elif roz3 == '2':
            print(' \nDíky za hru, doufám že sis jí užil a snad příště')
            time.sleep(2)
            print('Ukončuji hru bez vedlejších účinků...')
            time.sleep(2)
            quit()

#Část 2. Samotná hra:

#Pro Player1
def hod_kostkou_p1(hod_p1):
    time.sleep(0.5)
    vysledek_p1 = random.randint(1,6)
    text_p1 = f'Protihráč při hodu {hod_p1} hodil {vysledek_p1} na kostce.'
    print(text_p1)
    return vysledek_p1

#Pro Player2
def hod_kostkou_p2(hod_p2):
    time.sleep(0.5)
    vysledek_p2 = random.randint(1,6)
    text_p2 = f'Hráč při hodu {hod_p2} hodil {vysledek_p2} na kostce.'
    print(text_p2)
    return vysledek_p2

#Definice hry
def Kostky():
    
    while True:
        print(' \nZačíná hra Kostky!')
        time.sleep(1)
        
        #Player1
        print(' \nHází protihráč...')
        time.sleep(0.5)
        
        celkem_p1 = 0
        
        for hod_p1 in range(1,7):
            vysledek_p1 = hod_kostkou_p1(hod_p1)
            celkem_p1 += vysledek_p1

        print(f'Protihráč dohromady hodil {celkem_p1}')
        time.sleep(1)

        #Player2
        print(' \nHází hráč...')
        time.sleep(0.5)
        
        celkem_p2 = 0
        
        for hod_p2 in range(1,7):
            vysledek_p2 = hod_kostkou_p2(hod_p2)
            celkem_p2 += vysledek_p2

        print(f'Dohromady jsi hodil {celkem_p2}')
        time.sleep(1)

        #Porovnání
        if celkem_p2 == celkem_p1:
            print('Mladík: REMÍZA?! Jak je tohle možné? No to je fuk, házej znovu... \n  ')
            time.sleep(1)

        elif celkem_p2 == 21:
            print(' \nMladík: Cože? Jak je tohle možné? Zpropadená smůla tys vyhrál! Fajn... Gratuluji a můžeš jít.')
            time.sleep(2)
            Výhra()
            break

        elif celkem_p1 == 21:
            print(' \nMladík: WoHooo tomu se říká štígro... Teda aspoň pro mě, pro tebe to moc šťastné nebude. Na něj hoši...')
            time.sleep(2)
            Prohra()
            break

        elif celkem_p2 > celkem_p1:
            print(' \nMladík: Pche, nějakou záhadou jsi vyhrál. Gratuluji, jsi volný a můžeš jít...')
            time.sleep(2)
            Výhra()
            break

        elif celkem_p2 < celkem_p1:
            print(" \nMladík: Smůla hošánku. Prohrál's a teď jsi náš! Na něj hoši!")
            time.sleep(2)
            Prohra()
            break

#Část 3. Seskupení Celku:

def __main__():
    text_1()
    rozhovor_1()
    text_2()
    rozhovor_2()
    Kostky()
    text_3()

__main__()