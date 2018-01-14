def menjanje():
    
    for i in odabrane:
        
        a=1
        while a==1:
            print ("Da li ce se prikazivati knjiga ?")
            unos=input ("da/ne:  ")
            vrednost = unos.lower()
            i[0]=vrednost
            #print (i)
            break
        print ()
        b=1
        while b==1:
            print ("prethodni autor je: ", i[1])
            unos=input("Unestite novu vrednost ili Enter za zadrzavanje prethodne: ")
            if unos == "":
                i[1]=i[1]
                #print (i)
                break
            else:
                naziv=unos
                i[1]=naziv
                #print (i)
                break
        print ()
        c=1
        while c==1:
            print ("prethodni naziv je: ", i[2])
            unos=input("Unestite novu vrednost ili Enter za zadrzavanje prethodne: ")
            if unos == "":
                i[2]=i[2]
                #print (i)
                break
            else:
                naziv=unos
                i[2]=naziv
                #print (i)
                break
        print ()
        c=1
        while c==1:
            print ("prethodna godina je: ", i[3])
            unos=input("Unestite novu vrednost ili Enter za zadrzavanje prethodne: ")
            if unos == "":
                i[3]=i[3]
                #print (i)
                break
            else:
                naziv=unos
                i[3]=naziv
                #print (i)
                break
        print ()
        c=1
        while c==1:
            print ("prethodna kolicina je: ", i[4])
            unos=input("Unestite novu vrednost ili Enter za zadrzavanje prethodne: ")
            if unos == "":
                i[4]=i[4]
               # print (i)
                break
            else:
                naziv=unos
                i[4]=naziv
                #print (i)
                break
        print ()    
        c=1
        while c==1:
            print ("prethodna cena je: ", i[5])
            unos=input("Unestite novu vrednost ili Enter za zadrzavanje prethodne: ")
            if unos == "":
                i[5]=i[5]
                #print (i)
                break
            else:
                naziv=unos
                i[5]=naziv
                #print (i)
                break
        print ()
        c=1
        while c==1:
            print ("prethodni ISBN je: ", i[6])
            unos=input("Unestite novu vrednost ili Enter za zadrzavanje prethodne: ")
            if unos == "":
                i[6]=i[6]
                #print (i)
                break
            else:
                naziv=unos
                i[6]=naziv
                #print (i)
                break
        print ()
        
        c=1
        while c==1:
            print ("prethodni žanr je: ", i[7])
            unos=input("Unestite novu vrednost ili Enter za zadrzavanje prethodne: ")
            if unos == "":
                i[7]=i[7]
                break
            else:
                naziv=unos
                i[7]=naziv
                break

        print ()
        print ("                                          |---IZMENJENE KNJIGE---|                                               ")
        print ("-----------------------------------------------------------------------------------------------------------------")
        zapis ="{:<22}{:<28}{:<10}{:>5}{:>7}{:>15}{:>21}".format("AUTOR", "NAZIV", "GODINA", "KOLICINA", "CENA", "ISBN", "ŽANR")
        print (zapis)
        print ("-----------------------------------------------------------------------------------------------------------------")
        for i in odabrane:
            zapis="{:<20}{:<30}{:<10}{:>5}{:>10}{:>21}{:>17}".format(i[1], i[2], i[3], i[4], i[5], i[6], i[7])
            print (zapis)

        lista = []
        for i in l:
            zapis = "{}|{}|{}|{}|{}|{}|{}|{}".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
            lista.append(zapis)

        f=open ('knjige.txt', 'w')
        for i in lista:
            f.write(i)
        f.close()
        #break



def izmena ():
    global l
    l = []

    file = open('knjige.txt')
    print ("-----------------------------------------------")
    print ()
    print ("----Pretrazite knjigu po nazivu radi izmene----")


    x=0
    while x==0:
        global odabrane
        odabrane = []
            
    

        print ()
        unos = input ("Unesite naziv Knjige ili 0 za povratak: ")

        if unos == '0':
            break
        
        for line in file:
            s = line.split('|')
            l.append(s)
        #print (l)

        for i in l:
            if unos.lower() in i[1].lower():
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

        a=0
        while a==0:
            print("----------------------------")
            print ()
            print ("1.) IZMENI KNJIGU")
            print ()
            print ("2.) PONOVI PRETRAGU")
            print ()
            print ("0.) IZLAZAK IZ PROGRAMA")
            print ()
            x=input("unesite vrednost: ")

            if x=='1':
                menjanje()
                break
            elif x=='2':
                break
            elif x=='3':
                exit()
                
                




        


            
            



#izmena ()
