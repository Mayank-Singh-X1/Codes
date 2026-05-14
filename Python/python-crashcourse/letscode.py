# word=" pyhton "
# a=word.strip()
# print(a)

# url="https://war.compile"
# b=url.removeprefix("https://")
# print(b)
# print(4-5)

# c=10_234_344
# print(c)
# CAT_SOUND="meow"
# CAT_SOUND="bahw"
# print(CAT_SOUND)

#lists
a=["bicycles","choot","boom"]
# print(a)
# print(a[1])
# print(a[0].title())
# a[0]="ducati"
# print(a)

# #inserting element to a
# a.insert(1,"23")
# print(a)

# del a[1]
# print(a)

# b=a.pop(0)
# print(b)

# print(sorted (cars,reverse=True))
# print(cars)
# print(cars[-1])
# print(len(cars))
# print(cars[0:2])

# for car in cars:
#   print(f"{car.title()}, is a nice car.")

# for i in range(6):
#   print(i)

# list1=list(range(111, 1000, 2))
# print(list1)

#print even numbers
# even=list(range(0,11,2))
# print(even)

# squares=[]
# for i in range(1,11):
#   s=i**2
#   squares.append(s)

# print(squares)
# print(max(squares))
# print(min(squares))
# print(sum(squares))

# even_num=[i for i in range(0,10)]
# print(even_num)

#multiple of 3
# mulof3=[]
# for i in range(3,30):
#   if i%3==0:
#     mulof3.append(i)

# print(mulof3)

# mulof3=[i for i in range(3,30) if i%3==0]
# print(mulof3)
# cars=["toyota","audi","subaru","bmw"]
# cars.sort()
# car=cars[:]
# car.insert(2,"choot")
# print(car)
# print(f"The first three items in the list are {cars[:3]}")

#TUPLES
tup1=("ele1","ele2","ele3","ele4","ele5")
# tup1=("ele1","ele2","ele3","ele44","ele5")
# print(tup1)

def hello():
    print('hellp')


from Page_200 import user as us

ab=us("boom","hdi")
ab.greet()