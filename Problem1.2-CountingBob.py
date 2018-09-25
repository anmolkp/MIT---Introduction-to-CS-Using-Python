#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 17:21:12 2018

@author: anmolkhandeparkar
"""

#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s. 
#For example, if s = 'azcbobobegghakl', then your program should print
#Number of times bob occurs is: 2

s = input("Enter any string: ")
bobCounter = 0

for i in range(0,len(s)-2):
    if s[i] + s[i+1] + s[i+2] == "bob":
        bobCounter = bobCounter + 1
print("Number of times bob occurs is: " + str(bobCounter))