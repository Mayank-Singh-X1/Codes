# # car="audi"
# # print(car.title()=="Audi
# # div=[x for x in range (0,100) if x%5==0]
# # print(div)

# # print((5>3) and (4<5))

# # toppings=["sauce","onions","milk"]
# # print("milkw" not in toppings)

# a=50
# if (a<18):
#   print("hello")
# elif(a<10):
#   print("boom")
# else:('kaboom')

# available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']

# requested_toppings = ['mushrooms', 'olives', 'green peppeers']

# for requested_topping in requested_toppings:
#   if requested_topping in available_toppings:
#     print(f"adding {requested_topping} to your pizza")
#   else:
#     print(f"sorry we ran out of {requested_topping}")

# print("hello")

#DICTIONARIES

# if alien["speed"]=="medium":
#     alien["x_pos"] +=2

# del alien["points"]
# print(alien)


# for key in alien:
#     print(f"{key} \n")

# a=[1,2,3,44,55,6,6,6,7,7,8]
# print(set(a))
# river={"nile":"egypt","ganga":"india","yamuna":'bihar'}
# for x,y in river.items():
#     print(f"The {x} runs through {y}")

# alien=[]
# for i in range(30):
#     new_alien={"color":"green","points":5,"speed":"medium"}
#     alien.append(new_alien)

# for k in alien[:5:2]:
#     print(k)

# aliens = []
#  # Make 30 green aliens.
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
#  # Show the first 5 aliens.
# for alien in aliens[:5]:
#     print(alien)
# print("...")

# for i in range(0,100,2):
#     print(i)

# pizza={
#     "crust":"thick",
#     "toppings":["cheese","pepperoni"]
# }
# for i in pizza["toppings"]:
#     print(i)
# print(f"you ordered crust {pizza["crust"]} with toppings {i}")


# alien1={'color': 'green', 'points': 5}
# alien2={'color': 'hreen', 'points': 5}
# alien3={'color': 'preen', 'points': 5}

# aliens=[]

# for i in range(30):
#     alien={'no':i,'color': 'preen', 'points': 5}
#     aliens.append(alien)

# for alien in  aliens[0:3]:
#     if alien['no']==1:
#         alien['color']='blue'
# print(aliens)

# favorite_languages = {
# 'jen': ['python', 'rust'],
# 'sarah': ['c'],
# 'edward': ['rust', 'go'],
# 'phil': ['python', 'haskell'],
# }

# for name,lang in favorite_languages.items():
#     print(f"{name} favourite language is ")
#     for lan in lang:
#         print(f"{lan}")

# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#         },
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#         },
#     }
# for username, user_info in users.items():

#     print(f"\nUsername: {username}")

#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']
#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")

# while True:
#     topping=input("enter your toppings:")
#     if topping=='quit':break;


# rt=[1,2,3,3,5,6,2,1,7,3]
# while 3 in rt:
#     rt.remove(3)
# print(rt)

# resp={}
# while True:
#     value=input("enter ur name")
#     age=int(input ("enter ur age"))

#     resp[value]=age
#     qqw=input("continur")
#     if qqw=='no':break

# print (resp)
# def ani(jaan,naam="kutta"):
#     print(f"{jaan} mst hai {naam}")

# ani("boom","chutad")

# def bab(name,ahh):
#     cut={'naam':name,'aggh':ahh}
#     return cut

# q=bab('color','green')
# print (q)

# def short_message(message):
#     for mess in message:
#         print(f"Hello, {mess}")
# a=["nikita","sakshi","rupali"]
# short_message(a)


# def pizza(*toppings):
#     print(f"you selected {toppings}")
# pizza('burger','cheeses')
# pizza('choot')

import letscode as j
j.hello()
