from Hero.spell import Spell
from Hero.hero import Hero
class ENUTROF(Hero):
    color = "#CCCC00"
    breed = 3
    def __init__(self):
        self.spells = [Spell("Filouterie", "Eau"),
                        Spell("Purge", "Eau"),
                        Spell("Taxe", "Eau"),
                        Spell("Epuration", "Eau"),
                        Spell("Coupures", "Eau"),
                        Spell("Pelle du jugement", "Terre"),
                        Spell("Pelle tueuse", "Terre"),
                        Spell("Roulage de pelle", "Terre"),
                        Spell("Pelle mêle", "Terre"),
                        Spell("Pelle sismique", "Terre"),
                        Spell("Braise", "Feu"),
                        Spell("Météore", "Feu"),
                        Spell("Fusion", "Feu"),
                        Spell("Coup de grisou", "Feu"),
                        Spell("Coulée de lave", "Feu"),
                        Spell("Assurance tous risques", "Neutre"),
                        #Spell("Uppercut", "Neutre"),
                        #Spell("Éventrail", "Neutre"),
                        ]
        self.Phorzerker = 0
        Hero.__init__(self, "ENUTROF")
