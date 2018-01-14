def parsiraj (line):

    knjiga = {}

    podaci = line.split('|')

    if len (podaci) != 8:
        print ("Greska u formatu")
    else:
        knjiga["vrednost"]=podaci[0]
        knjiga["autor"]=podaci[1]
        knjiga["naslov"]=podaci[2]
        knjiga["godina"]=podaci[3]
        knjiga["kolicina"]=podaci[4]
        knjiga["cena"]=podaci[5]
        knjiga["isbn"]=podaci[6]
        knjiga["zanr"]=podaci[7]
        

    return knjiga

def ucitavanje_knjiga(file_name):

    lista_knjiga=[]

    file = open('knjige.txt', 'r')

    for line in file:
        l=line.strip()
        knjiga=parsiraj(l)
        lista_knjiga.append(knjiga)

    file.close()
    return lista_knjiga

lista_knjiga= ucitavanje_knjiga('knjige.txt')




def unos():
    global lista_knjiga
    zanrovi=["autobiografija", "fantazija", "drama", "roman", "dnevnik"]

    knjiga={}
    print("-----Podaci za unos knjige-----")

    knjiga["vrednost"] = "da"
    
    w=1
    while w==1:
        unos_podataka=input("Autor: ")
        if provera_polja(unos_podataka):
            podaci=unos_podataka
            knjiga["autor"]=podaci
            break


    e=1
    while e==1:    
        unos_podataka=input("Naslov: ")
        if provera_polja(unos_podataka):
            naslov=unos_podataka
            knjiga["naslov"]=naslov
            break
        

    g=1
    while g==1:
        unos_godina=input("Godina izdanja: ")
        if provera_godina(unos_godina):
            if provera_Godina(unos_godina):
                godina=unos_godina
                knjiga["godina"]=godina
                break


    
    k=1
    while k==1:
        unos_kolicina=input("Kolicina: ")
        if provera_kolicina(unos_kolicina):
            kolicina=unos_kolicina
            knjiga["kolicina"]=kolicina
            break




    e=1
    while e==1:
        unos_cena=input("Cena: ")
        if unos_cena.isnumeric():
            cena=unos_cena
            knjiga["cena"]=cena
            break
        else:
            print("Cena mora da bude broj! Pokusajte ponovo...")


    

    isbn = None
    while isbn is None:
        unos_isbn = input("ISNB: ")
        if provera_isbn(unos_isbn):
            if proveraIsbn(unos_isbn):
                if provera_Isbn(unos_isbn):
                    isbn = unos_isbn
                    knjiga["isbn"] = isbn
        else:
            print("Uneti isbn vec postoji. Pokusajte ponovo.")
    zanr = None
     
    while zanr is None:
        print ("Ponudjeni zanrovi: ")
        for i in range (len (zanrovi)):
            print (str(i+1)+".)"+zanrovi[i])

        zanr_indeks = input ("Unesite redni broj zanra: ")
        if zanr_indeks.isdigit():
            if 0<int(zanr_indeks)<=len(zanrovi):
                zanr = zanrovi[int(zanr_indeks)-1]
                knjiga["zanr"]=zanr
            else:
                print("Vrednost zanra mora biti broj!")

    #knjiga["vrednost"] = "da"
        

    lista_knjiga.append(knjiga)
    #zapis= "{}|{}|{}|{}|{}|{}|{}|{}\n".format(knjiga["vrednost"], knjiga["autor"], knjiga["naslov"], knjiga["godina"], knjiga["kolicina"], knjiga["cena"], knjiga["isbn"], knjiga["zanr"])

    print ()
    print ("Unesena Knjiga: ")
    print ("--------------------------------")
    print ()
    print ("                                             |---UNEŠENA KNJIGA---|                                              ")
    print ("-----------------------------------------------------------------------------------------------------------------")
    zapis ="{:<22}{:<28}{:<10}{:>5}{:>7}{:>15}{:>21}".format("AUTOR", "NAZIV", "GODINA", "KOLICINA", "CENA", "ISBN", "ŽANR")
    print (zapis)
    print ("-----------------------------------------------------------------------------------------------------------------")
    zapis="{:<20}{:<30}{:<10}{:>5}{:>10}{:>21}{:>17}".format(knjiga["autor"], knjiga["naslov"], knjiga["godina"], knjiga["kolicina"], knjiga["cena"], knjiga["isbn"], knjiga["zanr"])
    print (zapis)
    print ()

    f = open('knjige.txt', 'a')
    zapiss= "{}|{}|{}|{}|{}|{}|{}|{}\n".format(knjiga["vrednost"], knjiga["autor"], knjiga["naslov"], knjiga["godina"], knjiga["kolicina"], knjiga["cena"], knjiga["isbn"], knjiga["zanr"])
    f.write(zapiss)
    f.close

##    print ("Sve knjige: ")
##    print ("--------------------------------")
##    print ()
##    print ("                                               |---SVE KNJIGE---|                                                ")
##    print ("-----------------------------------------------------------------------------------------------------------------")
##    zapis ="{:<22}{:<28}{:<10}{:>5}{:>7}{:>15}{:>21}".format("AUTOR", "NAZIV", "GODINA", "KOLICINA", "CENA", "ISBN", "ŽANR")
##    print (zapis)
##    print ("-----------------------------------------------------------------------------------------------------------------")
##    for i in lista_knjiga:
##        zapis="{:<20}{:<30}{:<10}{:>5}{:>10}{:>21}{:>17}".format(knjiga["autor"], knjiga["naslov"], knjiga["godina"], knjiga["kolicina"], knjiga["cena"], knjiga["isbn"], knjiga["zanr"])
##        print (zapis)
##    print ()




## -----ISBN--------
def provera_isbn(unos_isbn):
    global lista_knjiga
    for knjiga in lista_knjiga:
        if knjiga["isbn"] == unos_isbn:
            print("Vec Postoji !")
            return False
    return True

def proveraIsbn(unos_isbn):
    if unos_isbn.isnumeric():
        #print()
        return True
    else:
        print ("ISBN neispravan, ponovo uneti BROJEVE !")
        return False

def provera_Isbn(unos_isbn):
    if len(unos_isbn)!=13:
        print("Ponovo unesite cifre tako da ih bude 13 !")
        return False
    else:
        return True



## -----GODINA------------
def provera_godina(unos_godina):
    if unos_godina.isnumeric():
        return True
    else:
        print ("GODINA neispravna, ponovo uneti brojeve !")
        return False

def provera_Godina(unos_godina):
    if len(unos_godina)!=4:
        print("Ponovo unesite cifre tako da ih bude 4 !")
        return False
    else:
        return True
        

        

## -------KOLICINA-------
def provera_kolicina(unos_kolicina):
    if unos_kolicina.isnumeric():
        return True
    else:
        print ("KOLICINA neispravna, ponovo uneti brojeve !")
        return False


##-------PRAZNO POLJE------
def provera_polja(unos_podataka):
    if len(unos_podataka)==0:
        print ("Morate uneti neke podatke")
        return False
    else:
        return True
        

##-------DRUGA OPCIJA--------------





#unos()


