
class Hero:
    # Конструктор класса
    def __init__(self, name, hp, lvl):
        # Атрибуты экземпляра класса
        self.name = name
        self.hp = hp
        self.lvl = lvl

    # Метод класса
    def base_action(self):
        return f'this base action {self.name}'

# Объект|Экземпляр класса
kirito = Hero("kirito", 1000, 100)
asuna = Hero("Asuna", 1200, 110)

print(kirito.base_action())
print(asuna.base_action())

# print(kirito.lvl)
# print(asuna.lvl)
