from knjige import *
from pretragaKnjiga import *
from prodaja import *
from brisanje import *
from izmena import *


def glavni_meni (uloga):
    x=1
    while x==1:
        print()
        print("--------------------------")
        print("(        KNJIZARA        )")
        print("--------------------------")
        if uloga=='menadzer':
            print()
            print ("Ulogovani ste kao menadzer")
            print("----------------------------")
            print ()
            print ("1.) PRETRAGA KNJIGA")
            print ()
            print ("2.) UNOS NOVE KNJIGE")
            print ()
            print ("3.) BRISANJE KNJIGE")
            print ()
            print ("4.) IZMENA KNJIGA")
            print ()
            print ("5.) IZLOGUJTE SE")
            print ()
            print ("0.) IZLAZAK IZ PROGRAMA")
            print ()
            x=0
        elif uloga == 'prodavac':
            print ("Ulogovali ste se kao prodavac")
            print("------------------------------")
            print ()
            print ("1.) PRETRAGA KNJIGA")
            print ()
            print ("2.) PRODAJA KNJIGA")
            print ()
            print ("5.) IZLOGUJTE SE")
            print ()
            print ("0.) IZLAZAK IZ PROGRAMA")
            print ()
            x=0
        else:
            print ("Niste se uspesno prijavili, ponovo se prijavite pokretanjem programa")
            x=1
            exit(0)


    x=-1
    
    while x==-1:
        x=input ("unesite opciju: ").strip()
        
        if uloga=='menadzer' and x=='1':
            meni ()
            glavni_meni ('menadzer')
            x=0
        elif uloga=='prodavac' and x=='1':
            meni ()
            glavni_meni('prodavac')
            x=0
        elif uloga =='menadzer' and x=='2':
            unos()
            glavni_meni ('menadzer')
            x=0
        elif uloga =='prodavac' and x=='2':
            prodaja()
            glavni_meni('prodavac')
            x=0
        elif uloga =='menadzer' and x=='3':
            brisanje ()
            glavni_meni ('menadzer')
            x=0
        elif uloga=='menadzer' and x=='4':
            izmena()
            glavni_meni ('menadzer')
            x=0
        elif uloga=='menadzer' and x=='5':
            x=0
            break
        elif uloga=='prodavac' and x=='5':
            x=0
            break
        elif x=='0':
            exit(0)
        x=-1

#glavni_meni('menadzer')
















