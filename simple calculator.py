# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 20:19:50 2024

@author: harsh
"""

a = int(input("Enter any number on which you want to perform operation:"))
b = int(input("Enter another number on which you want to perform operation:"))

print("Choose any operation:")
print("1. Addition")
print("2. Subtraction")
print("4. Division")
oper = int(input("Enter operation:"))

def case_one():
    print("Addition of numbers is:", a+b)

def case_two():
    print("Subtraction of numbers is:", a-b)

def case_three():
    print("Multiplication of numbers is:", a*b)

def case_four():
    print("Division of numbers is:", a/b)

def default_case():
    print("Invalid value")

def switch_demo(oper):
    switcher = {
        1: case_one,
        2: case_two,
        3: case_three,
        4: case_four
        }
    func = switcher.get(oper,default_case)
    return func()

switch_demo(oper)