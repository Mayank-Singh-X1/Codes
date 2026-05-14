# class Stack:
#     def __init__(self):
#         self.stack=[]

#     def isempty(self):
#         return len(self.stack)==0
    
#     def push(self,value):
#         self.stack.append(value)
#         print(f"Pushed {value}")

#     def pop(self):
#         if self.isempty():
#             print("Stack is empty")
#             return None
#         value=self.stack.pop()
#         print(f"value popped {value}")
    
#     def peek(self):
#         if self.isempty():
#             print("Stack is empty")
#             return None
#         print(f"top element is {self.stack[-1]}")

#     def traverse(self):
#         if self.isempty():
#            print("Stack is empty")
#            return None
#         for i in reversed(self.stack):
#             print(i)

#     def search(self,target):
#         if self.isempty():
#            print("Stack is empty")
#            return None
#         for i in range(len(self.stack)):
#             if self.stack[i]==target:
#                 pos=len(self.stack)-i
#                 print(f"Match found at {pos}") 
#                 return         
#         print("no match found")

# s=Stack()
# s.push(130)
# s.push(20)
# s.push(50)
# s.pop()
# s.search(130)
# s.traverse()
        
#2
# def precedence(op):
#     if op == '+' or op == '-':
#         return 1
#     elif op == '*' or op == '/':
#         return 2
#     return 0

# def infix_to_postfix(expression):
#     result = ""
#     stack = []

#     for char in expression:
#         if char.isalnum():  # operand
#             result += char
#         elif char == '(':
#             stack.append(char)
#         elif char == ')':
#             while stack and stack[-1] != '(':
#                 result += stack.pop()
#             stack.pop()  # Remove '('
#         else:  # operator
#             while stack and precedence(stack[-1]) >= precedence(char):
#                 result += stack.pop()
#             stack.append(char)

#     while stack:
#         result += stack.pop()

#     return result

# # 🔍 Test
# expr = "A+B*"
# print("Infix  :", expr)
# print("Postfix:", infix_to_postfix(expr))



#3
# def evaluate_postfix(expression):
#     stack = []

#     for char in expression:
#         if char.isdigit():
#             stack.append(int(char))
#         else:
#             b = stack.pop()
#             a = stack.pop()
#             if char == '+':
#                 stack.append(a + b)
#             elif char == '-':
#                 stack.append(a - b)
#             elif char == '*':
#                 stack.append(a * b)
#             elif char == '/':
#                 stack.append(a // b)  # Use // for integer division

#     return stack.pop()

# expr = "53+62/*"  # ((5+3)*(6/2)) = 8*3 = 24
# print("Postfix Expression:", expr)
# print("Evaluated Result:", evaluate_postfix(expr))






        


