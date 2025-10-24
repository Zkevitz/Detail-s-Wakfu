from Hero.spell import Spell
from Hero.hero import Hero
class ZOBAL(Hero):
    color = "#999900"
    breed = 14
    def __init__(self):
        self.spells = [Spell("Coup de pied fouetté", "Feu"),
                        Spell("Félure", "Feu"),
                        Spell("Névrose", "Feu"),
                        Spell("Détraquage", "Feu"),
                        Spell("Cabriole", "Feu"),
                        Spell("Signe", "Eau"),
                        Spell("Armature", "Eau"),
                        Spell("Rescousse", "Eau"),
                        Spell("Acharnement", "Eau"),
                        Spell("Sarabande", "Eau"),
                        Spell("Culbute", "Air"),
                        Spell("Fugue", "Air"),
                        Spell("Poursuite", "Air"),
                        Spell("Cavalcade", "Air"),
                        Spell("Dislocation", "Air"),
                        #Spell("Épée de Iop", "Air"),
                        #Spell("Uppercut", "Neutre"),
                        #Spell("Éventrail", "Neutre"),
                        ]
        Hero.__init__(self, "ZOBAL")