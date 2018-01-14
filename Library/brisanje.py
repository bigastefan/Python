def brisanje ():
    
    def meni_brisanje ():
        x=1
        while x==1:
            print ()
            print("--------------------------")
            print("(        KNJIZARA        )")
            print("--------------------------")
            print()
            print ("Ulogovani ste kao menadzer")
            print("----------------------------")
            print ("1.) PRETRAGA POO NAZIVU")
            print ()
            print ("2.) GLAVNI MENI")
            print ()
            print ("0.) IZLAZAK IZ PROGRAMA")
            print ()
            x=input ("unesite opciju: ").strip()
            
            if x=='1':
                pretraga_naziv ()
                x=0
            elif x=='2':
                break
            elif x=='0':
                #break
                
                exit ()
            x=1
        

    
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

            for i in l:
                if unos.lower() in i[1].lower() and i[0]=="da":
                    odabrane.append(i)

            print ()
            print ()
            print ("                                           |---ODABRANE KNJIGE---|                                               ")
            print ("-----------------------------------------------------------------------------------------------------------------")
            zapis ="{:<22}{:<28}{:<10}{:>5}{:>7}{:>15}{:>21}".format("AUTOR", "NAZIV", "GODINA", "KOLICINA", "CENA", "ISBN", "ŽANR")
            print (zapis)
            print ("-----------------------------------------------------------------------------------------------------------------")
            for i in odabrane:
                zapis="{:<20}{:<30}{:<10}{:>5}{:>10}{:>21}{:>17}".format(i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                print (zapis)
            print ()

            a=0
            while a==0:
                print("----------------------------")
                print ("Odaberite opciju: ")
                print ("1.) za brisanje knjige")
                print ("2.) ponovna pretraga")

                p=-1
                while p==-1:
                    x=input ("unesite opciju: ").strip()
                    
                    if x=='1':
                        if len (odabrane)== 0:
                            print ("------------------------------")
                            print ("nemoguće obaviti radnju !...")
                            print ("------------------------------")
                            break
                        else:
                            for i in odabrane:
                                i[0]="ne"

                            print ("Obrisane knjige: ")
                            for i in odabrane:
                                print (i)

                                
                        lista = []
                        for i in l:
                            zapis = "{}|{}|{}|{}|{}|{}|{}|{}".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                            lista.append(zapis)

                        f = open ('knjige.txt', 'w')
                        for i in lista:
                            f.write(i)
                        f.close
                        p=0
                    elif x=='2':
                        break
                a=1
    meni_brisanje ()
#brisanje ()


