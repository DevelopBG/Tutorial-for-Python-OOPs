list = [1,3,5]
string = "mlops playlist"
myint = 123

print(type(list))
print(type(string))
print(type(myint))
from oops_proj import Chatbook

# user1 = Chatbook()
# print(user1._Chatbook__name)


# """below we are checking using getter and setter 
# we can change the encapsulated var values"""
# print(user1.get_name())
# user1.set_name("ulto")
# print(user1.get_name())

user1 = Chatbook()
print(user1.id)
user2= Chatbook()
print(user2.id)
user3= Chatbook()
print(user3.id)