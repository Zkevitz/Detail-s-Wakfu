from Hero.spell import Spell
from Hero.hero import Hero
class IOP(Hero):
    color = "#FF0000"
    breed = 8
    def __init__(self):
        self.spells = [Spell("Épée céleste", "Feu"),
                        Spell("Fulgur", "Feu"),
                        Spell("Super Iop Punch", "Feu"),
                        Spell("Jugement", "Feu"),
                        Spell("Super Iop Punch", "Feu"),
                        Spell("Colère de Iop", "Feu"),
                        Spell("Ébranler", "Terre"),
                        Spell("Roknocerok", "Terre"),
                        Spell("Fendoir", "Terre"),
                        Spell("Charge", "Terre"),
                        Spell("Ravage", "Terre"),
                        Spell("Jabs", "Air"),
                        Spell("Rafale", "Air"),
                        Spell("Torgnole", "Air"),
                        Spell("Tannée", "Air"),
                        Spell("Épée de Iop", "Air"),
                        Spell("Uppercut", "Neutre"),
                        Spell("Éventrail", "Neutre"),
                        Spell("Vertu", "Neutre"),
                        ]
        self.concentrations = 0
        Hero.__init__(self, "IOP")
