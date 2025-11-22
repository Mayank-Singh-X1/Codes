# data structure
 # list 
# create a list 
list1 = [1,2,3,True,"str",2,2,3]
print(list1)
# changing the value
list1[2]= False
# append = to add a element in the list 
print(list1)
list1.append("New element")
print(list1)
# insert = to add any element in any position 
list1.insert(4,"Hello")
print(list1)
# extend = add a new list with the old list 
list1.extend(["Not Hello",3])
print(list1)
# remove = remove the first 2 from the list 
list1.remove(2)
print(list1)
# pop with value = remove the element present in that position
list1.pop(2)
print(list1)
# pop with no value = remove the element from the last
list1.pop()
print(list1)
# len = give the lenght of the list 
print(len(list1))
# slice = it will make the list to get a porsiton of the list
# print(list[start:end]) start is counted by not the end 
print(list1[2:7])
# count = number of times the element is print
print(list1.count(2))
# index = will tell the index to the element
print(list1.index("str"))
# clear = will clear the list 
list1.clear()

# create a new list 
fruits = ["apple","banana","ornage","grapes"]
num = [1,5,0,-9]
#sort it will sort and arrange the list 
fruits.sort()
print(fruits)
# it will only work on one type of same data type 
num.sort()
print(num)
# reverse = it give reverse order of the list or decending order
fruits.reverse()
print(fruits)
fruits.clear()
num.clear()
 # tuple is a collection of element that are ordered imutable can be duplicate and is declared  using parentisis 
# tuple does not allow to duplicate the data 
number = (1,2,3,4)
# number[2]= 5
print(number)
flower  = ("rose","lily")
# to add any tupe of list
print(number+flower)
# to multiply the list many type
print(flower*4)
print(flower.index("lily"))

# tuple unpacking = allow to open the list with out breaking
# and help them to assine them to a new var 
# without creating a new variable and use it 
person =("Jhon",34,"develop")
name,age,profession=person
print(name)
# we use tuple for two resion they are fast and they do not chage .
# 
# # set is a collcetion of item that are unoreded unimutable.
set1={1,3,4,5,5,6,}
set2= set([1,2,3,4])
# it doesn't allow duplecate item
print(set1)
print(set2)
# add to add an item 
set1.add(19)
print(set1)
# remove to remove but if the element is not there it will show error
set1.remove(3)
print(set1)
# discard is use in case of remove if the element it will not show the error even the element is not present
set1.discard(5)
print(set1)
# membership operator 
print(19 in set1)
print(1 not in set1)
# update = modify the list with a new set of element
set1.update([2,4,5,6,])
print(set1) 
 # update method add elemnet form another iterable truple,string in the exlisting set
set1.pop()
print(set1)
set1.pop()
print(set1)
# pop remove the first element in the set and last in the list.
set1.clear()
# del will delete whole set not just the element of the set.
del set1

# let use union and other thing of set in python
A = {1,2,3,4}
B = {3,4,5,6}
print(A|B)# for union
print(A-B)# for inetersetion 
print(A^B) # the element not present in B and A and not even in both
# to square the number with for loop.
square = {x**2 for x in range(1,11)}
print(square)
square_list = list(square)
# set does't support sort but list support .
square_list.sort()
print(square_list)
# forzen  help to forze mean no changes can be done after this function
frozen = frozenset([1,2,3])
# Dictionary = is a collection of item that are unorded mutable and are stored as key pair where each key is unique.
# key vlaue pair must be unique 
# value of the key can be same 
student = {
    "name":"Alice",
    "age":20,
    "city":"surat"
}
print(student)
person = dict(name="Jhon",collage="PU")
print(person)
# there are two way to write  dictionary in python 
print(student["name"])
print(student.get("name"))

student["course"]="python"
print(student.get("course"))

student["city"]="vadodara"
print(student.get("city"))

del student["city"]
print(student)

student.clear()
 
 # nested dictionary = a dictinary inside a dictionary 
students= {
  "101" : {"name":"tom","age":45},
  "102":{"name":"jerry","age":63}
 }
print(students["101"].get("name"))

# string is the collection of characters 
# string are immutable in python 
# mean you can't change string after declaration 

s1 = "hello "
s2  = 'bob'
s3 = """ 
This is 
multi line 
strng
"""
print(s1)
print(s3)
print(s2)
print(s1[5])
# concatination it will add the string in a sequence 
print(s1+s2)
print(s1)
print(s2)
# repetation operatino it will repeate the string multinple time 
print(s1*3)
print(len(s3))