def meni ():
    x=1
    while x==1:
        print("--------------------------")
        print("(        KNJIZARA        )")
        print("--------------------------")
        print()
        print ("Ulogovani ste kao menadzer")
        print("----------------------------")
        print ()
        print ("1.) PRETRAGA PO NAZIVU")
        print ()
        print ("2.) PRETRAGAA PO AUTORU")
        print ()
        print ("3.) PRETRAGA PO ISBN")
        print ()
        print ("4.) GLAVNI MENI")
        print ()
        print ("0.) IZLAZAK IZ PROGRAMA")
        print ()
        x=0

        x=input ("unesite opciju: ").strip()
        
        if x=='1':
            pretraga_naziv ()
            x=0
        elif x=='2':
            pretraga_autor ()
            x=0
        elif x=='3':
            pretraga_isbn()
            x=0
        elif x=='4':
            break
        elif x=='0':
            exit ()
        x=-1



def pretraga_naziv ():

    l = []

    file = open('knjige.txt')
    print ("-------------------------------------")
    print ("----Odabrali ste pretragu po nazivu knjige----")


    x=0
    while x==0:
        odabrane = []
            
    

        #print ("-------------------------------------")
        unos = input ("Unesite naziv Knjige ili 0 za povratak: ")

        if unos == '0':
            break
        
        for line in file:
            s = line.split('|')
            l.append(s)
        #print (l)

        for i in l:
            if unos.lower() in i[1].lower() and i[0]=="da":
                odabrane.append(i)

        print ("--------------------------------")
        print ()
        print ("                                         |---ODABRANE KNJIGE---|                                             ")
        print ("-----------------------------------------------------------------------------------------------------------------")
        zapis ="{:<22}{:<28}{:<10}{:>5}{:>7}{:>15}{:>21}".format("AUTOR", "NAZIV", "GODINA", "KOLICINA", "CENA", "ISBN", "ŽANR")
        print (zapis)
        print ("-----------------------------------------------------------------------------------------------------------------")
        for i in odabrane:
            zapis="{:<20}{:<30}{:<10}{:>5}{:>10}{:>21}{:>17}".format(i[1], i[2], i[3], i[4], i[5], i[6], i[7])
            print (zapis)
        print ()



def pretraga_autor ():

    l = []

    file = open('knjige.txt')
    print ("-------------------------------------")
    print ("----Odabrali ste pretragu po autorima----")


    x=0
    while x==0:
        odabrane = []
        #print ("-------------------------------------")
        unos = input ("Unesite ime autora ili 0 za izlazak: ")

        if unos=="0":
            break
        
        for line in file:
            s = line.split('|')
            l.append(s)
        
        for i in l:
            if unos.lower() in i[2].lower() and i[0]=="da":
                odabrane.append (i)
        print ("--------------------------------")
        print ()
        print ("                                            |---ODABRANE KNJIGE---|                                              ")
        print ("-----------------------------------------------------------------------------------------------------------------")
        zapis ="{:<22}{:<28}{:<10}{:>5}{:>7}{:>15}{:>21}".format("AUTOR", "NAZIV", "GODINA", "KOLICINA", "CENA", "ISBN", "ŽANR")
        print (zapis)
        print ("-----------------------------------------------------------------------------------------------------------------")
        for i in odabrane:
            zapis="{:<20}{:<30}{:<10}{:>5}{:>10}{:>21}{:>17}".format(i[1], i[2], i[3], i[4], i[5], i[6], i[7])
            print (zapis)
        print ()



def pretraga_isbn ():

    l = []

    file = open('knjige.txt')
    print ("-------------------------------------")
    print ("----Odabrali ste pretragu po ISBN----")


    x=0
    while x==0:
        odabrane = []
        #print ("-------------------------------------")
        unos = input ("Unesite ISBN ili 0 za izlazak: ")

        if unos=="0":
            break
        
        for line in file:
            s = line.split('|')
            l.append(s)
        
        for i in l:
            if unos.lower() in i[6].lower() and i[0]=="da":
                odabrane.append (i)
        print ("--------------------------------")
        print ()
        print ("                                            |---ODABRANE KNJIGE---|                                              ")
        print ("-----------------------------------------------------------------------------------------------------------------")
        zapis ="{:<22}{:<28}{:<10}{:>5}{:>7}{:>15}{:>21}".format("AUTOR", "NAZIV", "GODINA", "KOLICINA", "CENA", "ISBN", "ŽANR")
        print (zapis)
        print ("-----------------------------------------------------------------------------------------------------------------")
        for i in odabrane:
            zapis="{:<20}{:<30}{:<10}{:>5}{:>10}{:>21}{:>17}".format(i[1], i[2], i[3], i[4], i[5], i[6], i[7])
            print (zapis)
        print ()








#meni ()
