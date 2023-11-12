# -*- coding: utf-8 -*-
"""
Created on Mon May  2 17:05:44 2022

@author: sidvs
"""

class Animal():
    
    # Constructor Method
    def __init__(self):
        self.name = None # Default value is None
        self.food_habit = None
        self.weight = 63
    
    # Getters
    def get_name(self):
        return self.name
    
    # Setters
    def set_name(self, newname = ""):
       self.name = newname
    
    # String method
    def __str__(self):
        return self.name

class Person(Animal):
    
    def __init__(self,hair = "black",nickname = None):
        super().__init__()  # Calling the init function of the parent class. Other functions are inherited automatically
        self.hair = hair
        self.nickname = nickname
        
    
class Student(Person):
    
    def __init__(self,regd = None,course = None):
        super().__init__()
        self.regd = regd
        self.course = course
    
    def intro(self):
        print("Hello, my name is ",self.name+"!")
        print("My weight is ",self.weight,"kgs")
        print("My hair color is",self.hair)
        print("My nickname is",self.nickname)
        print("My registration number is",self.regd)
        print("I am pursuing",self.course)
        



s1 = Student(193246,"B.Sc(Hons.) in Physics")
s1.hair = "Black"
s1.nickname = "Sid"
s1.set_name("Siddharth")
s1.intro()