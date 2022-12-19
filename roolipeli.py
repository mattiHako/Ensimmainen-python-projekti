from luokatRoolipeli import Hahmo
import random
hahmosi = Hahmo  

# ainut Globaali muuttuja.
skillpoints = 0


#Hahmon luonnin funktio
def hahmoLuonti():
    hahmoLista = []
    etuNimi = input("Etunimesi: ")
    sukuNimi = input("Sukunimesi: ")
    ika = int(input("Ikäsi: "))
    sukupuoli = input("Sukupuolesi: ")
    hahmoTiedot = Hahmo(etuNimi, sukuNimi, ika, sukupuoli)
    hahmoLista.append(hahmoTiedot)
    
    # Pieni humoristinen lisä iän syöttämiseen.
    if ika < 50:
            vanhuus = "Hienoa, Sinullahan on vielä elämä edessä!"
    else:
        vanhuus = "Olet jo ikäloppu vanha pieru, kiesus sentään."
    return print(f"Tervetuloa {hahmoTiedot.etunimi} {hahmoTiedot.sukunimi}, Olet siis {hahmoTiedot.ika}-vuotta vanha {hahmoTiedot.sukupuoli}. {vanhuus}")
    
   
   


def visailu():
    print("Seuraavaksi katsotaan, paljonko ansaitset skillpointteja. Seuraa 4 kysymystä, vastaa harkiten. Äläkä katso googlesta prkl.")
    print("Jokaisessa kysymyksessä vastausvaihtoehtoja on KOLME: A, B ja C.")
    input("Jos olet valmis, paina 'enter'")
    # Tuple lista tietovisa osiolle. Etsin pitkin nettiä parasta vaihtoehtoa, ja tämä tuntui kaikista järkevimmältä, jossa voi vain näppärästi syöttää kysymyksiä, ja poimia ne for loopin avulla.
    # random.shuffle siis sekoittaa kysymykset random järjestykseen, joten jokaisella hahmonluonti kerraalla saat erilaisen listauksen kysymyksiä.
    kysymykset = [("Minä vuonna suomi itsenäistyi? | A.1918 B.1914 C.1917: ", "c"),
        ("Minä vuonna Facebook perustettiin? | A.2003 B.2004 C.2013: ", "b"),
        ("Mikä valtiomuoto oli antiikin roomassa ennen keisarivaltaa n.500-31eaa.? | A.Tasavalta B.Kuningaskunta C.Diktatuuri: ", "a"),
        ("Missä maassa sijaitsee Eiffelin torni? | A.Saksa B.Ranska C.Suomi: ", "b"),
        ("Minkä maalainen oli Kleopatra? | A.Sumerilainen B.Egyptiläinen C.Kreikkalainen: ", "c"),
        ("Kukaa on suomen presidentti? | A.Sauli Niinistö B.Keke Rosberg C.Vilma Lusenius: ", "a"),
        ("Milloin käytiin American sisällissota? | A.1850 B.1861 C.1982: ", "b"),
        ("Milloin Michael Jackson kuoli? | A.2006 B.2001 C.2009: ", "c"),
        ("Monta tuotantokautta on sarjassa The Sopranos? | A.6 B.8 C.2: ", "a"),
        ("Monta F1 mestaruutta Ayrton Senna voitti? | A.6 B.3 C.8: ", "b")]
    random.shuffle(kysymykset)
    maara = 0
    oikein = 0
    for kysymys, oikeaVastaus in kysymykset:
        if maara == 4:
            break
        vastaus = input(f"{kysymys}").lower()
        if vastaus == oikeaVastaus:
            print("Oikein!")
            oikein += 1
        else:
            print("Väärin!")
        maara += 1
    print(f"Sait {oikein} kysymystä oikein.")
    skillpoints = oikein*25
    return skillpoints


    
# Viimeisimpänä tehty ja varmasti pystyisi karsimaan vähintään puolet lyhyemmäksi. Pitää palata jatkossa modaamaan.
def taidot():
    global skillpoints
    taitoLista = [["Älykkyys:",0], ("Charmikkuus:",0), ("Nopeus:",0), ("Voima:",0), ("Kestävyys:",0)]
    
    print(f"Sinulla on {skillpoints} skillpointtia, käytä ne viisaasti.")
    print("Skillit ovat seuraavia:\n1. Älykkyys\n2. Charmikkuus\n3. Nopeus\n4. Voima\n5. Kestävyys")
    print("Käytä skillpisteet mielesi mukaan. Voit listan loputtua syöttää pisteet uudestaan, jos et ole tyytyväinen.")
    print("-"*100)
    kerrat = 5
    
    # Hahmolle syötetään skillpointit. Meinasi olla ongelmia loopin katkasemisessa jostain syystä, koska iski aivopieru..
    while kerrat > 0:
        lista = []
        kerrat = 5
        taitoPisteet = skillpoints
        for ominaisuus, pisteet in taitoLista:
            if kerrat == 0:
                break
            print(f"{taitoPisteet} skillpointtia jäljellä.")
            skill = int(input(f"{ominaisuus}"))
            if skill > taitoPisteet:
                skill = taitoPisteet
            statti = f"{ominaisuus} {skill}"
            taitoPisteet -= skill
            print(kerrat)
            lista.append(statti)
            print(lista)
            print("-"*70)
            if kerrat == 1:
                kysy = input("Jos haluat syöttää pisteet uudestaan, vastaa 'kyllä'. muuten paina 'enter'?")
                if kysy == "kyllä":
                    taitoPisteet = skillpoints
                    lista = []
                    continue
            kerrat -= 1
    print("-"*100)        
    return print(f"Hahmosi taidot:\n{lista}")
    # Eli syötät hahmolle skillpointteja järjestyksessä ja jokaisella loopin kierroksella tiedot lisätään listaan. Lopussa voit vielä päättää, haluatko syöttää tiedot alusta vai jatkaa eteenpäin.
        
#-----------------------------------------------------------------------------------------------------------------------------

# VIRALLINEN OHJELMA WHILE LOOPIN SISÄLLÄ.           

while True:
    print("Tervetuloa roolipelihahmon luonti generaattoriin. Täytä ensimmäiseksi hahmosi perus tiedot.")
    hahmo = hahmoLuonti()
    print("-"*100)
    skillpoints = visailu()
    print("-"*100)
    print(f"Ansaitsit itsellesi {skillpoints}/100 taitopistettä. Hahmosi on siis Level {skillpoints//25}")
    if skillpoints == 0:
        print("Tämä hahmo ei pääse edes omasta ovesta pihalle... Yritäs uudestaan!")
        print("*"*100)
        print("*"*100)
        continue
    input("Paina 'enter' jatkaaksesi")
    Skillit = taidot()
    print()
    print("Koita seuraavaksi uudestaan, millaisen hahmon saat luotua!")
    print("-"*100)
