from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def rest(self):
        self.__health += 1
        print(f"{self.name} отдыхает")
        print(f"Здоровье увеличилось: {self.__health}")

    @abstractmethod
    def attack(self):
        pass


class Warrior(Hero):
    def attack(self):
        print("Воин атакует мечом")


class Mage(Hero):
    def attack(self):
        print("Маг использует магию")


class Assassin(Hero):
    def attack(self):
        print("Ассасин атакует из-под тишка")

warrior = Warrior("Байаман", 10, 100, 50)
mage = Mage("Римуру", 15, 80, 70)
assassin = Assassin("Саске", 12, 90, 60)

warrior.greet()
warrior.attack()
warrior.rest()

print()

mage.greet()
mage.attack()
mage.rest()

print()

assassin.greet()
assassin.attack()
assassin.rest()