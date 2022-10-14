import random


class Hahmo:
    
    # Hahmolle syötettävät perus tiedot
    def __init__(self, firstname:str, lastname:str, age: int, sex: str):
        self.etunimi = firstname 
        self.sukunimi = lastname
        self.ika = age
        self.sukupuoli = sex
    
#-----------------------------------------------------------------------------------------

# En loppujen lopuksi käyttänyt luokkia visalle tai taidoille. En vaan yksinkertaisesti nähny pointtia, kun kaiken sai tehtyä funktioiden sisällä pääohjelmassa.
# Jätin ne kuitenkin tänne lojumaan vaikka jatkon kannalta, jos vaikka myöhemmin ymmärtäisi enemmän, miten niitä olisi järkevin käyttää.
    
class Taito:
    
    def __init__(self, skill1:int, skill2: int, skill3:int, skill4:int, skill5:int):
        self.taito1 = skill1
        self.taito2 = skill2
        self.taito3 = skill3
        self.taito4 = skill4
        self.taito5 = skill5
        
class Visa:
    # Tietovisan perustiedot.
    def __init__(self, kysymys, vaihtoehdot, oikein, pisteet):
        self.kysymys = kysymys
        self.vaihtoehdot = vaihtoehdot
        self.oikein = oikein
        self.pisteet = pisteet
    
    # Tulostaa tietovisakysymyksen ja vaihtoehdot.    
    def tuloste(self):
        print(self.kysymys)
        print(self.vaihtoehdot)
        
    # Määrittelee, mitä tapahtuu vastauksista.
    def vastauksesi(self):
        vastaus = input("Anna vastauksesi: ").lower()
        if vastaus == self.oikein:
            self.pisteet += 30
        else:
            self.pisteet += 0
    
        
        
        
        
            
        
#---------------------------------------------------------------------------------------------------------------------

#FUNKTIOT

