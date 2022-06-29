# Given a python function named smallest that accepts 
#a list of unsorted intergers and returns the smallest number in the list
# def smallest():
#     my_list=[78,56,67,45,2,45,10,3]
#     small=my_list[0]
#     for i in my_list:
#         if i < small:
#             small=i
#     print(small)
# smallest()
# #Take a string and return half its length in uppercase
# text="My mother is kind"
# half_text=len(text)//2
# half_text2=text[0:half_text].upper()
# print(half_text2)
# nested loops
# for i in ("Hello","Dear"):
#     for j in ("Good","Bye"):
#         print(i,j)

# for a in range(1,4):
#     for b in range(3,6):
#         print(a*b,end="\n")
# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same
# from itertools import count
# def name_properties():
#   my_names=["hildah","sakins","anota","mollen","judy","ma"]
#   names_qualified=[]
#   for name in my_names:
#     three = name[0]==name[-1]
#     if len(name)>=2 and three:
#         names_qualified.append(name)
#         count_ofnames=len(names_qualified)
#   print(count_ofnames)
# name_properties()

# def match_ends():
#     sentences=["Gooodpeople","badvibes","sendmoney","hildah","sakins","anota","mollen","judy","aa"]
#     sentence2=[]
#     for x in sentences:
#           if len(x)>=2 and x[0]==x[-1]:
#            sentence2.append(x)
#            sentences3=len(sentence2)     
#     print(sentences3) 
# match_ends()

# def outer_fun(a, b):
#     square = a ** 2

#     # inner function
#     def addition(a, b):
#         return a + b

#     # call inner function from outer function
#     add = addition(a, b)
#     # add 5 to the result
#     return add + 5

# result = outer_fun(5, 10)
# print(result)

# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
# def add(nums):
#     if nums:
#        return nums +add (nums - 1)
#     else:
#         return 0

# print(add(10))

# y=1+2+3+4+5+6+7+8+9+10
# print(y)

# def display_student(name, age):
#     print(name, age)

# display_student("Benard", 26)
# show_student=display_student

# # A. donuts
# # Given an int count of a number of donuts, return a string
# # of the form 'Number of donuts: <count>', where <count> is the number
# # passed in. However, if the count is 10 or more, then use the word 'many'
# # instead of the actual count.
# # So donuts(5) returns 'Number of donuts: 5'
# # and donuts(23) returns 'Number of donuts: many'

# def count():
#  number=int(input("Enter your number of doughnuts: "))
#  if number<10:
#     print("Your number of doughnuts is: " ,number)
#  else:
#      number >=10
#      print("Your number of doughnuts is many")
# count()
#         # checking the type of a
# a=123
# def fun():
#     a=[]
# print(type(a))

#     #reversing a string statement  without in-built methods
# def read_from_end():
#  sentence="Lona is a peaceful happy soul" 
#  for words in sentence:
#     print(words[-1] - words[0]) 
# read_from_end()   

# string formatting
from unittest.util import sorted_list_difference


fnames = ['file1','file2','file10','file11']
fnames.sort()
print(fnames)
fnames = ['file1','file2','file10','file11']
sorted(fnames)
print(fnames)
t=(1,2,3)
s="The three values are:{:d},{:d},{:d}".format(*t)
print(s)

numss_string="{:d},{:d}"
num=(456,453)
print(f"The formatted values are {numss_string.format(*num)}")

given_tuple=(4,30,2017,2,27)
expected_output=sorted(given_tuple)
print(expected_output)

task='{:20}{:10}{:20}{:8}'.format('First', '$99.01', 'Second', '$88.09')  
print(task)



