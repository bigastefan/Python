##def ispisivanje ():
##    
##    f = open ('knjige.txt')
##    L=[]
##    #unos = input ("Unesite naziv knjige: ")
##
##    
##
##    a=1
##    while a==1:
##        citanje = f.readline()
##        d = citanje.split('|')
##        l = []
##        
####        print (l)
##
##        for x in d:
##            l.append (x)
##            
##            #a=0
##            L.append(l)
##            a=0
##        print (l)
##        
##            
##        
#### ----pretraga po autoru----------
##
##            
####        for i in l:
####            if unos.lower() not in i.lower():
####                print("Nema zadate knjige !")
####            else:
####                if unos.lower() in i.lower():
####                    print ()
####                    print ("izabrana knjiga od autora: " + i.upper())
####                    print (l)          
####                    a=1
######                elif unos.lower() not in i.lower():
######                    continue
####                else:
####                    print("Nema zadate knjige !")
##
##            
####        a=1
##
##
##    f.close()
##
##
##
##
##ispisivanje ()
##
####a = "1. ivo andric"
####b = "2. Ivo Andric"
####c = "3. Marko BIGa"
####d = "4. VELJKO BIGA"
####l = [a, b, c, d]
####
####unos = input ("Unesite: ")
####
####for i in l:
####    if unos.lower() in i.lower():
####        print ("izabrana knjiga: " + i.lower())
####                
####    
####print ("uneta vrednost: " + unos.lower())


##lista = []
##
##l = [["ivo", "knjiga", "123", "234"], ["andric", "naziv", "2344", "34534"]]
##
##print ()

#zapis = "{}|{}|{}|{} \n".format(l[0][0], l[0][1], l[0][2], l[0][3]) 

##print (zapis)
##for i in l:
##    zapis = "{}|{}|{}|{} \n".format(i[0], i[1], i[2], i[3])
##    print (zapis)
##    lista.append(zapis)
##
##print (lista)

##l = [2, 5, 6, 7, 9]
####
####a=0
####for i in lista:
####    c=i+a
####    a=c
####    #print (a)
####print (a)
####
##
##zapis="{:<3}|{:<3}|{:<3}|{:<3}|{:<3}".format(l[0], l[1], l[2], l[3], l[4])
##
##print (zapis)
##my_time ()



knjiga = {'kolicina': '456', 'cena': '3456', 'zanr': 'roman', 'naslov': 'sdgth', 'godina': '3456', 'isbn': '3456345634566', 'autor': 'sufhg', 'vrednost': 'da'}

print (knjiga['kolicina'])

for i in knjiga:
    print (i[kolicina])


























