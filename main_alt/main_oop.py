from abc import ABC, abstractmethod
import time
import random

class Pykemon(ABC):
    def __init__(self, name, dexNum, baseHP, baseAtk, baseDef, baseSpd):
        self.dexNum = dexNum
        self.name = name
        self._baseHP = baseHP
        self.currentHP = baseHP
        self.baseAtk = baseAtk
        self.baseDef = baseDef
        self.baseSpd = baseSpd

    @abstractmethod
    def descripcion_juego(self, name):
        pass

    # ESTA CLASE LA HAGO ABSTRACTA TAMBIEN, POR SI HAY QUE AÑADIR EL TIPO Y CAMBIAR SEGUN CADA UNO  (PODEMOS HACERLA NORMAL)
    @abstractmethod
    def attack(self):
        pass

    def harm(self, damage):
        self.currentHP -= damage
        if self.currentHP < 0:
            self.currentHP = 0
        return round(self.currentHP)

class Electric(Pykemon):
    def descripcion_juego(self, name):
        return f'Soy {name}, un Pykemon eléctrico!'

    def attack(self):
        return round(random.uniform(0.8, 1) * (4 * (self.baseAtk * (self.baseAtk / self.baseDef)) / 50))

class Fire(Pykemon):
    def descripcion_juego(self, name):
        return f'Soy {name}, un Pykemon de fuego!'

    def attack(self):
        return round(random.uniform(0.8, 1) * (4 * (self.baseAtk * (self.baseAtk / self.baseDef)) / 50))

class Battle:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def descripcion_juego(self):
        return 'Bienvenido a Pykemon\n'

    def battle(self):
        life = self.pokemon1.currentHP
        life2 = self.pokemon2.currentHP

        while life > 0 and life2 > 0:
            damage = self.pokemon1.attack()
            damage2 = self.pokemon2.attack()

            print(f'{self.pokemon1.name} hace un ataque de {damage}')
            life2 = self.pokemon2.harm(damage)

            if life2 <= 0:
                print(f'La vida de {self.pokemon1.name} es {life} y del {self.pokemon2.name} es {life2}')
                print(f'{self.pokemon2.name} ha sido derrotado. {self.pokemon1.name} ha ganado!')
                break

            print(f'{self.pokemon2.name} hace un ataque de {damage2}')
            life = self.pokemon1.harm(damage2)

            if life <= 0:
                print(f'La vida de {self.pokemon1.name} es {life} y del {self.pokemon2.name} es {life2}')
                print(f'{self.pokemon1.name} ha sido derrotado. {self.pokemon2.name} ha ganado!')
                break

            print(f'La vida de {self.pokemon1.name} es {life} y del {self.pokemon2.name} es {life2}')
            time.sleep(2)


pokemon1 = Electric('Pikachu', 1, 20, 20, 5, 4)
pokemon2 = Fire('Charmander', 4, 20, 20, 4, 4)

battle = Battle(pokemon1, pokemon2)
print(battle.descripcion_juego())
print(pokemon1.descripcion_juego(pokemon1.name))
print(pokemon2.descripcion_juego(pokemon2.name))
battle.battle()
