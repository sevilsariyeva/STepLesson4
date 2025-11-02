# class Computer:
#
#     def __init__(self,model,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         self.model=model
#         self.memory=128
#
# class Display:
#
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         self.resolution="4K"
#
# class SmartPhone(Display,Computer):
#     def print_info(self):
#         print(self.model)
#         print(self.resolution)
#         print(self.memory)
#
# iphone=SmartPhone(model="Last")
# iphone.print_info()



# class Grandparent:
#     def about(self):
#         print("I am Grandparent")
#     def about_myself(self):
#         print("I am Grandparent")
#
# class Parent(Grandparent):
#     def about_myself(self):
#         print("I am Parent")
#
# class Child(Parent):
#     def __init__(self):
#         super().about()
#         super().about_myself()
#
# nick=Child()



# class Class1:
#     var=20
#     def __init__(self):
#         self.var=10
#
# class Class2(Class1):
#     def __init__(self):
#         print(self.var)
#         super().__init__()
#         print(self.var)
#         print(super().var)adsasdadasdasdsd
#
#asdjasdgjmsbdjmasdjb
# hello_world=Class2()



# class Hello:
#     def __init__(self):
#         print("Hello")
#
# class Hello_World(Hello):
#     def __init__(self):
#         super().__init__()
#         print("World!")
#
#
# hello_world=Hello_World()

# class Grandparent:
#
#     height=170
#     progress=100
#     age=60
# class Parent(Grandparent):
#     age=40
#
# class Child(Parent):
#     height=50
#     def __init__(self):
#         print(self.height)
#         print(self.progress)
#         print(self.age)
#
# nick=Child()


# class Human:


#     height=170
#     progress=40
# class Student(Human):
#     progress=100
# class Worker(Human):
#     progress=50
#
# nick=Student()
# ann=Worker()
#
# print(nick.progress)
# print(ann.progress)
#
#
#
# # class Human:
# #     def __init__(self,name,age):
# #         self.name=name
# #         self.age=age
# #     def talk(self):
# #         print(f" {self.name} is talking")
# #
# # class Student(Human):
# #     def study(self):
# #         print(f"{self.name} is studying")
# # class Teacher(Human):
# #     def teach(self):
# #         print(f"{self.name} is teaching")
# #
# # student1=Student("Nigar",29)
# # teacher1=Teacher("Aysel teacher",35)
# #
# # student1.talk()
# # teacher1.talk()
# #
# # student1.study()
# # teacher1.teach()
#
#
