from Hero.hero import Hero
from Hero.spell import Spell
class SACRIEUR (Hero) :
    color = "#680C0C"
    breed = 11
    def __init__(self) :
        Hero.__init__(self, "SACRIEUR")
        self.spells = [Spell("Sang pour sang", "Feu"),
                        Spell("Furie sanguinaire", "Feu"),
                        Spell("Sang brûlant", "Feu"),
                        Spell("Punition", "Feu"),
                        Spell("Cage de sang", "Feu"),
                        Spell("Pied rocheux", "Terre"),
                        Spell("Colonnades", "Terre"),
                        Spell("Poing tatoué agrippant", "Terre"),
                        Spell("Démence", "Terre"),
                        Spell("Fracasse", "Terre"),
                        Spell("Aversion", "Air"),
                        Spell("Projection", "Air"),
                        Spell("Fulgurance", "Air"),
                        Spell("Tempête spirituelle", "Air"),
                        Spell("Assaut", "Air"),
                        #Spell("Flèche lumineuse", "Neutre"),
                        #Spell("Uppercut", "Neutre"),
                        #Spell("Éventrail", "Neutre"),
                        ]