# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 23:40:41 2018

@author: Aksam
"""

#Basic Data Structures - Lists
li = ['duck', 'season']
li2 = ['wabbit', 'season']
li3 = ['...Fire']

print(li)
print(li2)
print(li3)

#access single item in list
print(li[0], li2[0], li3[0])
print(li[:])


#add single item to list
li.append(li2[0])
print(li)
li.append(li2[1])
print(li)

#combine two lists by extension
li.extend(li2)
print(li2)
print(li)

#combine two list by concatenation
li4 = li + li3
print(li)
print(li3)
print(li4)

#print out slices of list
print(li4)
print(li4[2:])
print(li4[:4])
print(li4[1:3])

#Changing lists in place
#create list of zeros
noLi = 4*[0]
noLi
#modify items in list
mice_brain = 10
rat_brain = 20
human_brain = 500
noLi[2] = mice_brain
noLi[1] = rat_brain
noLi[3] = human_brain
noLi

#sort list
noLi.sort()
noLi
#reverse order
noLi.reverse()
noLi


#A tuple is essentially a list that you can not change.
trpA = ('protein', 'TIM Barrel')
type(trpA)


#Dictionaries
#initialize a couple of dictionaries
names = {'aaron':'hardin', 'mike':'lawson', 'peter':'combs'}
drinks = {'mike':'coffee', 'aisha':'caffeine', 'peter':'soda'}
wines = {'red':'cabernet','white':'pinot grigio',\
'sparkling':'blanc de noirs', 'sticky':'muscato'}
#print dictionaries
names
drinks
wines

#find a particular value
names['aaron']
drinks['peter']
wines['sparkling']

#add single item to dictionary
drinks['debbie'] = 'diet coke'
print drinks