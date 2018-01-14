def prodaja ():

    global korpa_knjiga
    korpa_knjiga = []

    global korpa_knjiga_zapis
    korpa_knjiga_zapis = []

    global racuni
    racuni = []
    
    def pretraga_naziv ():
        
        l = []

        file = open('knjige.txt')
        print ("-------------------------------------")
        
        main_loop=0
        while main_loop==0:

            odabrane = []
            
            print ("----Odabrali ste pretragu po nazivu knjige----")
            unos = input ("Unesite naziv Knjige ili 0 za povratak: ")

            if unos == '0':
                break
            
            for line in file:
                s = line.split('|')
                l.append(s)
            #print (l)

            print (l)
            for i in l:
                
                if unos.lower() in i[1].lower() and i[0]=="da":
                    odabrane.append(i)
            if len (odabrane)==0:
                print ("------------------------------------")
                print ("Knjiga ne postoji, odaberite opciju")
                    

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


            temp = True
            a=0
            while a==0:
                if temp == False:
                    break
                print("----------------------------")
                print ("Odaberite opciju: ")
                print ()
                print ("1.) DODAJ U KORPU")
                print ()
                print ("2.) PONOVI PRETRAGU")
                print ()
                print ("3.) ZAVRSI KUPOVINU")
                print ()
                print ("0.) IZLAZAK IZ PROGRAMA")
                print ()
                x=input ("unesite opciju: ").strip()
                
                
                if x=='1':
                    
                    
                    
                    global kolicina
                    kolicina=input("unesite kolicinu: ")

                    for i in odabrane:
                        knjiga = []
                        if int(kolicina) > int(i[4]):
                            print ()
                            print ("OVIH KNJIGA NEMA NA LAGERU: ")
                            print ("------------------------------------------------")
                            zapis= "|{} - {} - {} komada |".format(i[1], i[2], i[4])
                            print (zapis)
                            print ("------------------------------------------------")
                            print ()
                            print ()
                        else:
                            #for k in odabrane:
                            
                            if unos.lower() in i[1].lower() and i[0]=="da":
                                #print (i)
                                i[4]=int(i[4])-int(kolicina)
                                korpa_knjiga.append(i)
                            zapis = "{},{}|{}{}|{}{}{}".format(i[1], i[2], kolicina," komada", "Cena:", int(kolicina)*int(i[5]), " din")
                            korpa_knjiga_zapis.append(zapis)  
                            knjiga.append(i[1])
                            knjiga.append(i[2])
                            knjiga.append(kolicina)
                            knjiga.append(int(kolicina)*int(i[5]))
                            racuni.append(knjiga)
                            
                    print ("------------------------------------------------------------------------")
                    print ()
                    print ()
                    print ("                            |---KORPA---|                               ")
                    print ("------------------------------------------------------------------------")
                    naslov = "|{:<20}{:<24}{:<4}{:>18}|".format("AUTOR", "NAZIV", "KOLICINA", "CENA")
                    print (naslov)
                    print ("------------------------------------------------------------------------")
                    for i in racuni:
                        zapiss="|{:<18}{:<30}{:<6}{:>12} din|".format(i[0], i[1], i[2], i[3])
                        print(zapiss)










                        

                    global lista
                    lista = []
                    for i in l:
                        zapis = "{}|{}|{}|{}|{}|{}|{}|{}".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                        lista.append(zapis)
                       
                    c=0
                    while c==0:
                        print("----------------------------")
                        print ()
                        print ("1.) ZAVRSI KUPOVINU")
                        print ()
                        print ("2.) POVRATAK U MENI")
                        print ()
                        y=input ("unesite vrednost: ")
                        
                        if y=='1':
                            file=open('knjige.txt','w')
                            for n in lista:
                                file.write(n)
                            file.close()
                            racun()
                            return True
                        elif y=='2':
                            temp = False
                            break
                        
                elif x=='2':
                    #x=0
                    break
                elif x=='3':
                    file=open('knjige.txt','w')
                    for n in lista:
                        file.write(n)
                    file.close()
                    racun()
                    break
                elif x=='0':
                    exit()

    def racun ():
        print ()
        print ("                            |---RACUN---|                               ")
        print ("------------------------------------------------------------------------")
        naslov = "|{:<20}{:<24}{:<4}{:>18}|".format("AUTOR", "NAZIV", "KOLICINA", "CENA")
        print (naslov)
        print ("------------------------------------------------------------------------")
        zapis = "Vaš račun iznosi: "
        cena = []
        for i in racuni:
            cena.append(i[3])
        a=0
        for i in cena:
            c=i+a
            a=c
        for i in racuni:
            zapiss="|{:<18}{:<30}{:<6}{:>12} din|".format(i[0], i[1], i[2], i[3])
            print(zapiss)
        print ("------------------------------------------------------------------------")
        print("|", zapis, a, ".00 din |")
        print ("---------------------------------")


##-----zapisivanje racuna u TXT fajl------------
        
##        f=open ('racuni.txt', 'a')
##        f.write()
##        f.close()
        
##------------------------------------------------------

    

        
    
    pretraga_naziv ()
#prodaja ()
