# def add(*args):
#     total=0
#     for arg in args:
#         total+=arg
#     return total

# print(add(1,2,3,4))

def address(*args,**kwargs):
    for a in args:
        print(a)

    print(f"{kwargs.get('street')}")
    for key, value in kwargs.items():
        print(f"hell yeah {key} : {value}")

address(123,"jfjds",
    street="hello",myname="maikiee" )
    