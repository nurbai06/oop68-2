class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает...")
        self.health += 1


hero1 = Hero("Римуру", 120, 1000, 2000)
hero2 = Hero("Велдора", 100, 1200, 2050)

hero1.greet()
print(f"До атаки: Сила = {hero1.strength}")
hero1.attack()
print(f"После атаки: Сила = {hero1.strength}")

print(f"До отдыха: Здоровье = {hero1.health}")
hero1.rest()
print(f"После отдыха: Здоровье = {hero1.health}")

print("-" * 30)

hero2.greet()
print(f"До атаки: Сила = {hero2.strength}")
hero2.attack()
print(f"После атаки: Сила = {hero2.strength}")

print(f"До отдыха: Здоровье = {hero2.health}")
hero2.rest()
print(f"После отдыха: Здоровье = {hero2.health}")