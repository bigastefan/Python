from glavniMeni import *

korisnik1={'korisnicko ime':'petar' , 'sifra':'petar', 'ime':'Petar', 'prezime':'Petrovic', 'uloga':'menadzer', 'jmbg':'13047722647733'}

korisnik2={'korisnicko ime':'marko' , 'sifra':'marko', 'ime':'Marko', 'prezime':'Markovic', 'uloga':'prodavac', 'jmbg':'13042345347733'}

korisnik3={'korisnicko ime':'jovan' , 'sifra':'jovan', 'ime':'Jovan', 'prezime':'Jovanovic', 'uloga':'prodavac', 'jmbg':'54647722647733'}

lista_korisnika=[korisnik1, korisnik2, korisnik3]

a=1
while a==1:
    def logovanje():
        p=1
        while p==1:
            print()
            print ("-----------------------------------------------------------------------------------------------------------------")
            print ()
            print("--------------------------")
            print("(        KNJIZARA        )")
            print("--------------------------")
            print()
            print("Ulogujte se: ")
            print("-----------")
            
            x=input("Korisnicko ime: ")
            y=input("Lozinka: ")

            print ("***************************")
            

            z= "Pogresno korisnicko ime i/ili lozinka, pokusajte ponovo !"
            for i in lista_korisnika:
                pronadjen = False
                if x == i['korisnicko ime'] and y == i['sifra']:
                    print ("Prijavljeni ste kao: "+ i['ime']+" " + i['prezime']+"... Vasa uloga je: "+i['uloga'])
                    print()           
                    glavni_meni(i['uloga'])
                elif x != i['korisnicko ime'] and y != i['sifra']:
                    #print ("Pogresno korisnicko ime i/ili lozinka, pokusajte ponovo !")
                    pronadjen = False
                    continue
                else:
                    #if pronadjen == False:
                    print (z)
                        #p=1
                
    logovanje()
