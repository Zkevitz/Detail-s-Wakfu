from Hero.spell import Spell
from Hero.hero import Hero
class ENIRIPSA(Hero):
    color = "#FF99FF"
    breed = 7
    def __init__(self):
        self.spells = [Spell("Vivification", "Eau"),
                        Spell("Mot soignant", "Eau"),
                        Spell("Revitalisation", "Eau"),
                        Spell("Infusion", "Eau"),
                        Spell("Reconstitution", "Eau"),
                        Spell("Cure alternative", "Feu"),
                        Spell("Flamme purificatrice", "Feu"),
                        Spell("Explo-soin", "Feu"),
                        Spell("Corro-soin", "Feu"),
                        Spell("Anatomie", "Air"),
                        Spell("Psychose", "Air"),
                        Spell("Colli-mateur", "Air"),
                        Spell("Fiole infectée", "Air"),
                        Spell("Torpeur", "Air"),
                        #Spell("Épée de Iop", "Air"),
                        #Spell("Uppercut", "Neutre"),
                        #Spell("Éventrail", "Neutre"),
                        ]
        Hero.__init__(self, "ENIRIPSA")
