# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Chjl6XUrCsElH3EfN75gxe2I4JpX5y1A
"""

#Lets Upgrade
#Assignment 1 :Python Program to do operations using two numbers(Addition,Subtraction,Multiplication and Division)

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
print(" Press 1 for Addittion \n Press 2 for Subtraction \n Press 3 for Multiplication \n Press 4 for Division")
option = int(input("Enter your option: "))
if option == 1:
  print("You have choosen Addition operation")
  result = num1+num2
  print("Sum : ", result)
elif option == 2:
  print("You have choosen Substraction operation")
  result = num1-num2
  print("Difference : ",result)
elif option == 3:
  print("You have choosen Multiplication operation")
  result = num1*num2
  print("Product : ", result)
elif option == 4:
  print("You have choosen division operation")
  result = num1/num2
  print("Remainder : ",result)
else:
  print("Invalid Value")
print("\nThank you for performing operations.")