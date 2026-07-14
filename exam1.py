class Hero:

    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        print(f"{self.name} готов к бою!")


class MageHero(Hero):

    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        print(f"Маг {self.name} кастует заклинание! MP: {self.mp}")


class WarriorHero(MageHero):

    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp, mp)

    def action(self):
        print(f"Воин {self.name} рубит мечом! Уровень: {self.lvl}")


class BankAccount:

    bank_name = "Simba"

    def __init__(self, hero, balance, password):
        self.hero = hero
        self._balance = balance
        self.__password = password

    def login(self, password):
        return password == self.__password

    @property
    def full_info(self):
        return (
            f"Герой: {self.hero.name}, "
            f"Уровень: {self.hero.lvl}, "
            f"Баланс: {self._balance} SOM"
        )

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name

    def bonus_for_level(self):
        return self.hero.lvl * 10

    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if isinstance(other, BankAccount):
            if type(self.hero) == type(other.hero):
                return self._balance + other._balance
            return "Ошибка: Нельзя сложить счета героев разных классов!"
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return (
                type(self.hero) == type(other.hero)
                and self.hero.lvl == other.hero.lvl
            )
        return False


mage1 = MageHero("Rimuru", 50, 1000, 150)
mage2 = MageHero("Veldora", 50, 1200, 200)
warrior = WarriorHero("Conan", 50, 1500, 0)

mage1.action()
warrior.action()

acc1 = BankAccount(mage1, 5000, "1234")
acc2 = BankAccount(mage2, 3000, "5678")
acc3 = BankAccount(warrior, 7000, "9999")

print(acc1)
print(acc2)

print("Банк:", acc1.get_bank_name())
print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

print(acc1.full_info)

print("Вход:", acc1.login("1234"))
print("Вход:", acc1.login("1111"))

print("\n=== Проверка __add__ ===")
print("Сумма счетов двух магов:", acc1 + acc2)
print("Сумма мага и воина:", acc1 + acc3)

print("\n=== Проверка __eq__ ===")
print("Mage1 == Mage2 ?", acc1 == acc2)
print("Mage1 == Warrior ?", acc1 == acc3)

