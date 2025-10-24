class Hero :
    def __init__(self, className, name=None) :
        self.className = className
        self.name = name or ""
        self.PlayedTurn = 0
        self.UsedSpell = []
        self.DamageDone = []
        self.AirDamage = []
        self.FireDamage = []
        self.WaterDamage = []
        self.EarthDamage = []
        self.HealDone = []
        self.ShieldDone = []
        self.TotalAmountOfShield = 0
        self.TotalAmountOfDamage = 0
        self.TotalAmountOfHeal = 0
        self.ShieldRank = 1
        self.DamageRank = 1
        self.HealRank = 1
    def clear(self):
        self.__init__()