# # Родительский класс
# class User:
#     def __init__(self, name, login, password):
#         self.name = name
#         self.age = login
#         self.password = password
#
#     def user_login(self, password):
#         if password == self.password:
#             return "Ok"
#         return "fail"
#
# # Дочерний класс
# class UserVIP(User):
#     def __init__(self, name, login, password, last_name):
#         super().__init__(name, login, password)
#         self.last_name= last_name
#
#     def vip_login(self, name):
#         if name == self.name:
#             return "ok"
#         return "fail"
#
#     def user_login(self, login):
#         if login == self.login:
#             return "Correct"
#         return "fail"
#
# arda = User("Arda", "arda123@gmail.com", "arda123")
# john = UserVIP("John", "john123@gmail.com", "john123")
#
# print(arda.user_login("arda123"))
# print(john.user_login("john123@gmail.com"))
#

class Swim:
    pass
    # def action(self):
    #     print("swim")
class Fly:
    def action(self):
        print("fly")
class Animal(Fly, Swim):
    pass
d = Animal()
d.action()


class A:
    def action(self):
        print("A")
class B(A):
    def action(self):
        super().action()
        print("B")
class C(A):
    def action(self):
        super().action()
        print("C")
class D(B, C):
    def action(self):
        super().action()
        print("D")
test_obj = D()
test_obj.action()

