from Hero.spell import Spell
from Hero.hero import Hero
class XELOR(Hero):
    color = "#0000CC"
    breed = 5
    def __init__(self):
        self.spells = [Spell("Ralentissement", "Eau"),
                        Spell("Martel'heure", "Eau"),
                        Spell("Horloge", "Eau"),
                        Spell("Sablier", "Eau"),
                        Spell("Désynchronisation", "Eau"),
                        Spell("Suspension", "Feu"),
                        Spell("Éclair obscur", "Feu"),
                        Spell("Aiguille", "Feu"),
                        Spell("Poussière", "Feu"),
                        Spell("Perturbation", "Feu"),
                        Spell("Tempus fugit", "Air"),
                        Spell("Pointe-heure", "Air"),
                        Spell("Paradoxe", "Air"),
                        Spell("Symétrie", "Air"),
                        Spell("Retour spontané", "Air"),
                        Spell("Distorsion", "Neutre"),
                        Spell("Flétrissement", "Neutre"),
                        Spell("Présages violents", "Neutre"),
                        Spell("Sinistro", "Neutre"),
                        Spell("Rouage", "Neutre"),
                        ]
        Hero.__init__(self, "XELOR")
