# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 23:55:50 2018

@author: Aksam
"""

#Tests, Loops, and Escapes
checkingAccountBalance = 4
if checkingAccountBalance < 10:
    thisWeeksFood = 'ramen'
else:
    thisWeeksFood = 'goodRamen'

thisWeeksFood

checkingAccountBalance = 400
if checkingAccountBalance < 10:
    thisWeeksFood = 'ramen'
elif checkingAccountBalance < 100:
    thisWeeksFood = 'good ramen'
elif checkingAccountBalance < 200:
    thisWeeksFood = 'better ramen'
else:
    thisWeeksFood = 'ramen that is truly profound in its goodness'

thisWeeksFood

#and, or, (and) not
true_statement = 1 # non‐empty strings are true
false_statement = 0 # empty strings are false
if true_statement==1 and false_statement==0:
    print("right")
else:
    print("wrong")
    
#loop
li = ['Red Leicester', 'Gruyere', 'Camembert', 'Parmesan', 'Mozarella', 'Cheddar']
#iterate over list
for x in li: print(x)
