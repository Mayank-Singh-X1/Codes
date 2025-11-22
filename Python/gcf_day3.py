# #object oriented programming is based on the concept of objects , which can contain attributes and methods


# #class is a blueprint for creating object, it defines attributes and methods
# # class person:
# #     def __init__(self,name,age):  #init is inilization of object,it is a special method in python classes
# #                                   # and it automatically runs when u create an object
# #         self.name = name  #attribute
# #         self.age=age
# #     def greet(self):    #self refers to the current objectadn it is used to store data inside the object
# #         print(f"hi, im {self.name} and i am {self.age} years old")



# # #creating an object
# # p1=person("alice",20)
# # p2=person("bob",19)
# # print(p1.name)
# # p2.greet()


# class cars:
#     def __init__(self,color,brand,model):
#             self.carcolor=color
#             self.carbrand=brand
#             self.carmodel=model


#     def greet(self):  #greet is method i.e, just a name of function
#           print(f"Car color is {self.carcolor} , model is {self.carmodel} and its model is {self.carmodel}")


# c1=cars("blue","Toyota","XYZ")
# c2=cars("red","lambo","2334")
# print(c2.carcolor)
# c2.greet()


# #encapsulation   inheritance  abstraction  polymorphism
# #inheritance

# #example of 1) single inheritance
# #inheritance allows one class (child) to inherit attribute and methods from another classs (parent)
# class father():
#       def generationalWealth(self):
#             print("papa ka paisa / Dads money")


# class mother():
#       def hobbies(self):
#             print("hobbies in herited")


# class child(father,mother):
#       def salary(self):
#             print("Haram ki kamai")
# n1=child()
# n1.generationalWealth()
# n1.salary()


# #2) multiple inheritance: A class inherits fro more than one parent class
# #3) multi level inheritance.  for eg, Grandparent->parent->child
# #4) heirarchical inheritance: multiple child class but only one parent class
# class animal():
#       def sound(self):
#             print("Aimals make sound")


# class dog(animal):
#       def bark(self):
#             print("dog barks")


# class cat(animal):
#       def meow(self):
#             print("cat meows")


# d=dog()
# d.sound()
     
# #5)hybrid inheritance: combination of any four types of inheritance




# #polymorphism: it allows different classes to define methods with the same name that behave differently


# class Bird:
#       def sound(self):
#             print("chirp")
# class cat:
#       def sound(self):
#             print("meow")
# def make_sound(animal):
#       animal.sound()


# b=Bird()
# c=cat()
# make_sound(b)
# make_sound(c)


# #types of poly:1)runtime poly.   2)compiletime poly.
# class parent:
#       def runtime(self):
#             print("parent method overwriting")


# class child(parent):
#       def runtime(self):
#             print("child method overwriting")


# c1=child() #method overwriting means redifining a method from a parent class in its child class so that the child clases version is usded insted of parent
# #operator overloading allows custom classes to define ow operators like +-* , etc behave when used with the class object it makes custom objects behave like data types


class point:
      def __init__(self,x,y):
          self.x=x
          self.y=y


      def __add__(self,other):
          return point(self.x+other.x,self.y+other.y)
     
p1=point(1,2)
p2=point(3,4)
p3=p1+p2
print(p3.x, p3.y)


class book:
     def __init__(self,title,pages):
          self.title=title
          self.pages=pages


     def __add__(self,num1):
          return self.pages+ num1.pages


b1=book("harry potter",500)
b2=book("pyhton programming",350)
print(b1+b2)


#encapsuluation means binding data and methods that operate on that data into a unit and restrict data access
# access specifier
      # public - member are accessible anywhere
      # protected - members canbe accessed only in the class and the sub class(_)
      # private - members cannot be accessed directly from outside the class,fro accessing a private attribute a public method is created in the same classs (__)   .trying to accesss the private attribute deirectly will result in attribute error


class BankAcc:
     def __init__(self,balance):
          self.__balance = balance #private
     def deposit(self, amount):
          self.__balance+=amount
     def get_balance(self):
          return self.__balance
     
acc= BankAcc(1000)
acc.deposit(500)
print(acc.get_balance())


#abstraction means hiding internal details and sharing what is necessary.
from abc import ABC, abstractmethod
class vehicle(ABC):
     @abstractmethod
     def start_engine(self):
          pass


class car(vehicle):
     def start_engine(self):
         print("start with a key")


c1=car()
c1.start_engine()        
#any abstract method in parent class should b implemented
#abstract class(vehicle) hides how start engine vehicle works which is later on implemented by child class(car)
