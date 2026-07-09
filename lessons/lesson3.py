# class BankAccount:
#     def __init__(self, fio, balance, login, password):
#         self.fio = fio
#         self._balance = balance
#         self.login = login
#         self.__password = password
#
#     def get_balance(self, password):
#         if password == self.__password:
#             return self._balance
#         return "wrong password!"
#
#
#
#
# arda = BankAccount('arda', 1000, 'ardager', 'arda123')
# print(arda._balance)
# print(arda.login)
# print(arda._BankAccount__password)


from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Gaf"
    def move(self):
        return "Step"



class SendOTP(ABC):
    @abstractmethod
    def send(self, otp, phone):
        pass
class KgOTP(SendOTP):
    def send(self, otp, phone):
        data = f'''
        <Text> Ваш временный пароль: {otp}</Text>
        <Phone>{phone}</Phone>
        '''


             



