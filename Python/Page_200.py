# class dog:
#     def __init__(self,name,age):
#         self.Name=name
#         self.Age=age

#     def sit(self):
#         print(f"{self.Name} is sitting")

#     def rollover(self):
#         print(f"{self.Age} is jutst a nmber")

# mydog=dog('madharchod', 45)
# mydog=dog('piyush',3)
# print(f"{mydog.Name} is name and age is {mydog.Age}")
# mydog.sit()
# mydog.rollover()
# print(mydog.Name)

# class restaurants:
#     def __init__(self,restaurant_name, cuisine ):
#         self.name=restaurant_name
#         self.Cuisine=cuisine

#     def descibe_restaurant(self):
#         print("Best restaurant in world")

#     def open_restaurant(self):
#         print("Resaturant is open")

# a=restaurants("reyansh","Italinan")
# print(f"name is {a.name} and cuisine is {a.Cuisine}")

# a.descibe_restaurant()
# a.open_restaurant()

# class CAR:
#     def __init__(self, brand, year, color):
#         self.Brand=brand
#         self.Year=year
#         self.Color=color

#     def description(self):
#         print(f"{self.Brand} is manufactured in {self.Year} and coloor is {self.Color}")
#     def mileage(self,run):
#         self.Run=run
#         print(f"Total run is {self.Run}")

# class electric(CAR):
#     def __init__(self,brand,year,color):
#         super().__init__( brand, year, color)

#     def __str__(self):
#         return  f"{self.Brand} is manufactured in {self.Year} and coloor is {self.Color}" 

# c1=CAR("honda",2024,"biluuu")
# # c1.Brand="hefhje"
# c1.mileage(30)
# c1.description()


    
# a3=electric("bomm",343,"neon")
# print(a3)


# class user:
#     def __init__(self,firstname,lastname):
#         self.fname=firstname
#         self.lname=lastname
#         self.attemp_login=0
#         self.max=3

#     def greet(self):
#         print(f"Hello {self.fname} {self.lname}")

#     def increment_attempt(self):
#         if self.attemp_login<3:
#             self.attemp_login+=1
#             print(f"attempts left {self.max-self.attemp_login}")
#         else:
#             print("you ran out of attempts")

#     def dis_attempt(self):
#         print(self.attemp_login)

# a=user('madhar','chod')
# a.greet()
# a.increment_attempt()
# a.increment_attempt()
# a.increment_attempt()
# a.increment_attempt()
# a.dis_attempt()

# from random import choice as raand
# l1=[1,"boom",34,"dnjcd","3445"]
# a=raand(l1)
# print(a)

#files and exceptions

# from pathlib import Path 

# a=Path('pi_digits.txt')
# content=a.read_text()
# content=content.strip()
# # print(content)

# lines=content.splitlines()
# for line in lines:
#     print(line)

# pi_string=''
# for line in lines:
#     pi_string+=line

# print(pi_string)
# print(len(pi_string))
# print(pi_string[:4])

# bb=input("enter your birthday")
# if bb in pi_string:
#     print("your birthday exists")
# else:
#     print("it doesn't")

# msg='i like dog'
# msg=msg.replace('dog','cat')
# print(msg)

# from pathlib import Path
# a=Path('pi_digits.txt')
# a.write_text("kyu re madharchod!!")
# b=a.read_text()

# contents='hello\n'
# contents+='world\n'
# contents+='qwerty\n'
# a.write_text(contents)
# b=a.read_text()

# print(b)

# print("enter the number you want to divide")
# print("enter q to quit")

# while True:
#     a=input("enter 1st number: ")
#     if a=='q':
#         break
#     b=input("enter 2nd number: ")
#     if b=='q':
#         break

    
#     try:
#         result=int(a)/int(b)
#     except ZeroDivisionError:
#         print("you cant divide numbre by 0")
#     else:
#         print(result)

# from pathlib import Path
# def count_words(path):
   
#     try:
#         content=path.read_text()
#     except FileNotFoundError:
#        print("file not found")
#     else:       
#         words=content.split()
#         wordlen=len(words)
#         print(wordlen)

# l1=['pivalue.txt','dfbdj','pi_digits.txt']
# for i in l1:
#     path=Path(i)
#     count_words(path)



# numbers=[1,2,3,4,5,6,7]
# path=Path('username.json')
# content=json.dumps(numbers)
# path.write_text(content)
# contents=path.read_text()
# num=json.loads(contents)
# print(num)
# username=input("Enter your name: ")
# content=json.dumps(username)
# path.write_text(content)
# print(f"we will remember you {username}")
# name=path.read_text()
# wer=json.loads(name)
# print(f"we rememberred you {wer}")

# from pathlib import Path
# import json
# path = Path('username.json')
# if path.exists():
#     contents = path.read_text()
#     username = json.loads(contents)
#     print(f"Welcome back, {username}!")
# else:
#     username = input("What is your name? ")
#     contents = json.dumps(username)
#     path.write_text(contents)
#     print(f"We'll remember you when you come back, {username}!")


