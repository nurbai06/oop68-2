import random


# Родительский класс
class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} атакует!")

    def rest(self):
        self.health += 1
        print(f"{self.name} отдыхает. Здоровье: {self.health}")


# Дочерний класс Warrior
class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name}: Воин атакует мечом!")


# Дочерний класс Mage
class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.name}: Маг кастует заклинание!")


# Дочерний класс Assassin
class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f"{self.name}: Ассасин атакует из-под тишка!")


warrior = Warrior("Байаман", 100, 100, 100, 50)
mage = Mage("Мерлин", 105, 80, 150, 100)
assassin = Assassin("Шэдоу", 95, 90, 130, 80)

heroes = {
    "warrior": warrior,
    "mage": mage,
    "assassin": assassin
}

print("Выберите героя:")
print("Warrior")
print("Mage")
print("Assassin")

choice = input("Введите героя: ").lower()

if choice not in heroes:
    print("Неверный выбор!")
else:
    player = heroes[choice]

    opponents = [hero for key, hero in heroes.items() if key != choice]
    enemy = random.choice(opponents)

    print(f"\nВы выбрали: {player.__class__.__name__}")
    print(f"Противник: {enemy.__class__.__name__}\n")

    player.attack()
    enemy.attack()

    wins = {
        "Warrior": "Assassin",
        "Assassin": "Mage",
        "Mage": "Warrior"
    }

    player_class = player.__class__.__name__
    enemy_class = enemy.__class__.__name__

    print()

    if wins[player_class] == enemy_class:
        print(f"{player_class} победил!")
    else:
        print(f"{enemy_class} победил!")