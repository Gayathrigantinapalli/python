# my_amount = 60000
# class city:
#     def __init__(self,amount):
#         self.amount=amount
#     def deposite(self):
#         global my_amount
#         my_amount+=self.amount
#         print(my_amount)
#     def withdraw(self):
#         global my_amount
#         my_amount-=self.amount
#         print(my_amount)
#     def house_loan(self):
#         if self.amount>=100000:
#             print('eligible for houseloan')
#         else:
#             print('sorry')
# class village(city):
#     def __init__(self, amount):
#         super().__init__(amount)
#     def crop_loan(self):
#         if self.amount>=20000:
#             print('eligible for croploan')
#         else:
#             print('sorry')
#     def cow_loan(self):
#         if self.amount>=10000:
#             print('eligible for cowloan')
#         else:
#             print('sorry')
# # my_amount = 60000
# data=village(200000)
# data.deposite()
# data.withdraw()
# data.house_loan()
# data.crop_loan()
# data.cow_loan()






# class Animal:
#     def speak(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# data = Dog()
# data.speak()  
# data.bark()  


# class house:
#     def __init__(self,money):
#         self.money=money
#     def name(self):
#         print('ENTER THE NAME')
#     def age(self):
#         print('ENTER THE AGE')
# class room(house):
#     def __init__(self,money):
#         super().__init__(money)
#     def study(self):
#         print('ENTER THE CLASS')
# data=room(8)
# data.name()
# data.study()
# data.age()



# class vehicle:
#     def __init__(self,start):
#         self.start=start
#     def seat(self):
#         print('correct')
#     def money(self):
#         print('paid')
# class bike(vehicle):
#     def __int__(self,start):
#         super().__init__(start)
#     def ride(self):
#         print('go to ride')
# data=bike(2)
# data.ride()
# data.money()
# data.seat()


# class teacher:
#     def __init__(self,book):
#         self.book=book
#     def records(self):
#         print("WRITE THE RECORDS")
#     def name(self):
#         print("MY NAME IS GAYATHRI")
#     def age(self):
#         print("ENTER YOUR AGE")
# class student(teacher):
#     def __init__(self,book):
#         super().__init__(book)
#     def money(self):
#         print("TAKE IT YOUR MONEY")
#     def reading(self):
#         print("READ THE NEWSPAPPER")
#     def fees(self):
#         print("YOU ALREADY PAY THE FEES")
# data=student(9)
# data.records()
# data.name()
# data.age()
# data.money()
# data.reading()
# data.fees()



# my_bakance =40000
# class bank:
#     def __init__(self,balance):
#         self.balance=balance
#     def agricultureloan(self):
#         if self.balance>=50000:
#          print("GANTED AGRICULTURELOAN")
#         else:
#          print("SORRY")
#     def shoploan(self):
#         if self.balance>=30000:
#          print("ELIGIBLE FOR SHOPLOAN")
#         else:
#          print("SORRY")
#     def withdraw(self):
#       global my_balance
#       my_balance-=self.balance
#       print("my_balance")
#     def deposite(self):
#       global my_balance
#       my_balance+=self.balance
#       print("my_balance")
# class maneger(bank):
#     def __init__(self, balance):
#       super().__init__(balance)
#     def landloan(self):
#         if self.balance>=20000:
#          print("YOUR LANDLOAN IS GRANTED")
#         else:
#          print("in sufficiante balance")
# my_balance = 80000
# data=maneger(10000)
# data.agricultureloan()
# data.shoploan()
# data.deposite()
# data.withdraw()
# data.landloan()     
   


# class property:
#     def __init__(self,house):
#         self.house=house
#     def rooms(self):
#         print("THERE ARE ROOMS")
# class owner(property):
#     def __init__(self, house):
#         super().__init__(house)
#     def car(self):
#         print("MY CAR")
#     def bike(self):
#         if self.bike:
#             print("TRUE")
#         else:
#             print("SORRY")
# data=owner(2)
# data.car()
# data.bike()
# data.rooms()



# class resturant:
#     def __init__(self,fruits,tiffin,meals,biriyani):
#         self.fruits=fruits
#         self.tiffin=tiffin
#         self.meals=meals
#         self.biriyani=biriyani
#     def veg(self):
#         print("SHE EAT THE AP MEALS")
#     def nonveg(self):
#         print("SHE EAT THE HYDERABAD BIRIYANI")
#     def patient(seLf):
#         print("SHE CAN NOT THE  BANANA ")
#     def tiffin(self):
#         print("I EAT THE DOSA")
# x=resturant('tiffin','meals','fruits','biriyani') 
# x.patient()
# x.nonveg()
# x.veg()  

        
        
        
        



        
        





