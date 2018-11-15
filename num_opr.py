# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 23:22:50 2018

@author: Aksam
"""
#Variable types
s = 'hello world'
i = 42
f = 3.14159
print(s)
type(s)
type(i)
type(f)

#Numerical operations
i = 42
f = 3.14159
# addition uses the plus sign (+)
sum = i + f
# subtraction uses the minus sign (‐)
diff = i - f
# multiplication uses the asterisk (*)
prod = i * f
# division uses the slash (/)
quo = i / f
# and exponents use a double‐asterisk (**)
pow = i ** f
print('sum',sum)
print('diff',diff)
print('prod',prod)
print('quo',quo)
print('pow',pow)

#quote used
s = 'hello "world", if that is your real name.'
print(s)
s2 ="That's World, to you, buddy."
print(s2)
s3 = '''hello "world", if that is your real name.That's World, to you, buddy.'''
print(s3)


#Concatenating (+) strings
name = 'Nathaniel I. Krefman'
middle_initial = name[11]
first = name[0:9]
last = name[13:]

simple_name = first + ' ' + last
print(simple_name)


#
i = 42
f = 3.14159265
string = 'variables can be interpolated as strings here %s and here %s' % (i,f)
print(string)


