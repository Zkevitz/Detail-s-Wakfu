from Hero.spell import Spell
from Hero.hero import Hero
class CRA(Hero):
    color = "#33FF33"
    breed = 9
    def __init__(self):
        self.spells = [Spell("Flèche fulminante", "Feu"),
                        Spell("Flèche d'immolation", "Feu"),
                        Spell("Flèche enflammée", "Feu"),
                        Spell("Flèche ardente", "Feu"),
                        Spell("Flèche explosive", "Feu"),
                        Spell("Flèche cinglante", "Terre"),
                        Spell("Pluie de flèches", "Terre"),
                        Spell("Flèche criblante", "Terre"),
                        Spell("Flèche perçante", "Terre"),
                        Spell("Flèche destructrice", "Terre"),
                        Spell("Flèche chercheuse", "Air"),
                        Spell("Flèche de recul", "Air"),
                        Spell("Flèche tempête", "Air"),
                        Spell("Flèche harcelante", "Air"),
                        Spell("Flèche statique", "Air"),
                        Spell("Flèche lumineuse", "Neutre"),
                        #Spell("Uppercut", "Neutre"),
                        #Spell("Éventrail", "Neutre"),
                        ]
        self.affutage = 0
        self.precision = 0
        Hero.__init__(self, "CRA")
