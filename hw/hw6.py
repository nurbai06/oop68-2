from faker import Faker

# Эта библиотека нужна для генерации случайных реалистичных данных.
# Она используется для создания тестовых имен, email и адресов.

fake = Faker()

print("Имя:", fake.name())
print("Email:", fake.email())
print("Адрес:", fake.address())