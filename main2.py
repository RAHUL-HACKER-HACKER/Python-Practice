#factorial
# n=int(input("Enter Value:"))
# fac=1
# for i in range(n):
#     fac*=i+1
# print(fac)

#new program
# def sum(value1,value2):
#     add=value1+value2
#     return add


# def fibb(n):
#     if(n==1):
#         return 0
#     if(n==2):
#         return 1
#     return fibb(n-1)+fibb(n-2)
# n=int(input())
# print("fibb series:")
# for i in range(1,n+1):
#     print("values:",fibb(i),1003)

#dictonary
#dic={"one":1,"two":2,"three":3}
#print(dic)
# for i in dic:
#     print(i)

# dic={"one":1,"two":2,"three":3}
# dic["One"]=dic["one"]
# dic.pop("one")

# print(dic)

# class Fruit:
#     id=100  
#     def get(self):
#         print(self.id)

# obj=Fruit()

# print(obj.get()) 

# class Circle:
#     def get_radius(self):
#         return self._radius

#     def set_radius(self, radius):
#         if radius > 0:
#             self._radius = radius
#         else:
#             print("Radius must be a positive value.")

# circle1 = Circle()
# circle1.set_radius(5)
# print("Circle Radius:", circle1.get_radius())
# circle1.set_radius(-2)

class Animal:
    def intro(self):
        print("I am from Animal")

class Dog(Animal):
    def name(self):
        print("My name is Dog")
 
obj=Dog()
obj.intro()
obj.name()

def display():
    print("My name is rahul kumar")
    
display()