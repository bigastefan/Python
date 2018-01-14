korisnik1={'korisnicko ime':'biga.stefan' , 'sifra':'stefanmarko', 'ime':'Stefan', 'prezime':'Biga', 'uloga':'menadzer'}

korisnik2={'korisnicko ime':'gordana.biga' , 'sifra':'cipele', 'ime':'Gordana', 'prezime':'Biga', 'uloga':'prodavac'}

korisnik3={'korisnicko ime':'veljko.biga' , 'sifra':'kosulja', 'ime':'Veljko', 'prezime':'Biga', 'uloga':'prodavac'}

korisnik4={'korisnicko ime':'marko.biga' , 'sifra':'kosarka', 'ime':'Marko', 'prezime':'Biga', 'uloga':'menadzer'}

lista_korisnika=[korisnik1, korisnik2, korisnik3, korisnik4]



kor_ime='Stefan'

for i in korisnik1:
    if ['korisnicko_ime'] in korisnik1 == kor_ime:
        print ("radi")
    else:
        print ("NE radi...")

print ("Prijavljani ste kao " +kor_ime)
