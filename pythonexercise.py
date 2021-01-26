# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 16:56:42 2021

@author: vadlamani
"""

import datetime
import math
def time():
    Date = datetime.datetime.now()
    print(Date.strftime("%B-%d-%Y %H:%M:%S:%f"))
def area():
    radius = float(input("Enter the radius:"))
    print(math.pi * radius * radius)
def color():
    color_list = ["Red","Green","White","Black"]
    print("First Color: " + color_list[0])
    print("Last Color: " + color_list[3])
def compute():
    result = str(input("Pick any number: "))
    print(int(result) + int(result + result) + int(result * 3))
def different():
    value = int(input("How many numbers do you want?"))
    inputVal = ""
    for i in range(value):
        j = input("Enter your value")
        inputVal = inputVal + " " + j
    # inputVal = inputVal[0,len(inputVal)-1]
    TotalValues = inputVal.split();
    contains = "";
    i = 0
    same = False
    for i in TotalValues:
        if str(i) in contains:
            same = True
            break
        contains = contains + str(i);
    if same:
        print("The numbers are not all different from each other")
    else:
        print("The numbers are all different from each other")
def prime():
    value = int(input("What is your n value"))
    valueSum = 0
    placeholder = False
    for num in range(2, value+1):
        for i in range(2,num-1):
            if int(num%i) == 0:
                placeholder = True
                break
        if not placeholder:
            valueSum += num
        else:
            placeholder = False
    print(valueSum)
def duplacates():
    value = int(input("How many values do you want? "))
    inputVal = ""
    for i in range(value):
        j = input("Enter your value ")
        inputVal = inputVal + " " + j
    duplacates = list(set(inputVal.split()))
    print(duplacates)
def dictionarySort():
    dict1 = {1:1, 2:3, 5:2, 4:2}
    sort = sorted(dict1.values())
    sort2 = sorted(dict1.keys())
    print("sorted values: " + str(sort))
    print("sorted keys: " + str(sort2))
def duplacatesDictionary():
    dict1 = {1:1, 2:3, 4:2, 5:2, 4:2}
    output = {}
    for i,j in dict1.items():
        if j not in output.values():
            output[i] = j
    print(output)
    
    
            
        
