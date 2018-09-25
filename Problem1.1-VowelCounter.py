#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 17:08:46 2018

@author: anmolkhandeparkar
"""

#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s. 
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
#For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5

s = input("Enter a string: ")
vowelCounter = 0

for i in range(0,len(s)):
    if s[i] == "a" or s[i] == "e" or s[i] == "o" or s[i] == "i" or s[i] == "u":
        vowelCounter = vowelCounter + 1

print("Number of vowels: " + str(vowelCounter))
