import random
class Pykemon:
    def __init__(self, name, dexNum, baseHP, baseAtk, baseDef, baseSpd):
        self.dexNum = dexNum
        self.name = name
        self._baseHP = baseHP
        self.currentHP = baseHP
        self.baseAtk = baseAtk
        self.baseDef = baseDef
        self.baseSpd = baseSpd

    def attack(self):
        # damage = random.uniform(0.8, 1) * (4 * (self.power * (self.baseAtk / self.baseDef)) / 50) # TORNA MOLT PETIT
        damage = (random.random() * 1.5) * self.baseAtk
        return round(damage)

    def harm(self, damage):
        self.currentHP -= damage
        return self.currentHP

    def heal(self, healing):
        if self.currentHP + healing <= self.maxHP:
            self.currentHP += healing
        else:
            self.currentHP = self.maxHP

    def move(move):
        # TO DO: CREAR Y PROBAR CLASE MOVE 
        pass
