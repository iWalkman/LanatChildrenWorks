print "Hello world"

f = 5.0
i = 5 
s = "Five"
b = True

print "string to float"
t = '5'
print type(t)
t = int(t)
print type(t)

print f
print i
print s
print b

print type(f)
print type(i)
print type(s)
print type(b)

str = "lanat"
print len(str)

print str + "the best"

print str[:3]

#a = input()
#print type(a)
print "Math"

import math

print abs(-9)

print 67**2
print pow(67,2)

print math.sqrt(4)

print int(5.89)
print round(5.89)
print round(5.89,1)

import random 

print random.randint(1,100)


print "if switch"

#bool statemants
x == 4 # x equal 4
x == 7 # x equal 7
x != 7 # x not equal 7
x != 4 # x not equal 4
x  > 5 # x bigger 5
x  < 5 # x less 5
x >= 6 # x bigger or equal 6
x <= 6 # x less or equal 6

x = 8 
y = 13 
x == 8 and y < 15 #  x equal 8 and y less 15
x > 8 and y < 15 #  x bigger 8 and y less 15
x != 0 or y >15 #  x not equal 0 or y bigger 15
x < 0 or y >15 #  x less 0 or y bigger 15

#if
tovar1 = 50
tovar2 = 50
if tovar1+ tovar2 > 99 :
	print "Perfect"
else:
	print "Something wrong"

#elif
x = -10
 
if x > 0:
     print (1)
elif x < 0:
     print (-1)
else:
     print (0)

#list

t = [23, 656, -20, 67, -45]   # список целых чисел
[4.15, 5.93, 6.45, 9.3, 10.0, 11.6]   # список из дробных чисел
["Katy", "Sergei", "Oleg", "Dasha"]   # список из строк
["Moscow", "Titova", 12, 148]   # смешанный список
[[0, 0, 0], [0, 0, 1], [0, 1, 0]]   # список, состоящий из списков

[45, -12, 'april'] + [21, 48.5, 33]
[45, -12, 'april', 21, 48.5, 33]
[[0,0],[0,1],[1,1]] * 2
[[0, 0], [0, 1], [1, 1], [0, 0], [0, 1], [1, 1]]

print  len(t)
print t[0]
print t[0:3]
print t[3:0]
t[3] = 'r'
print t[3]
t[3:4] = [10,20]
print t[3:4]

#dictionary

 d = {'bird': 'Vorobey', 'mouse': 'Polyevka', 'dog': 'Sobaken', 'cat': 'Myrlyka'}

 print dic['cat']

 d['elephant'] = 'Dambo'
 del(d['elephant'])


#while

str1 = "+" 
i = 0
while i < 10:
	print (str1)
	i = i + 1

#for
for x in xrange(1,10):
	print x

for g in t:
	print g

for key in d:
	d[key] = d[key] + '!'
	

l = [6,2,9,20]

for i in range(len(l)-1):
	min = l[i]
	mini = i
	for j in range(i,len(l)):
		if l[j] < min:
			min = l[j]
			mini = j
		l[i],l[mini] = l[mini],l[i]
print l



def right_input():
	try:
		
		return input()
	except NameError:
		return raw_input()
	else:
		pass
	finally:
		pass

print "------"

s= ''
for i in range(1,10):
	s+='-'
print s

def hr(n):
	s = ''
	for i in range(n):
		s+='_'
	print s

def hf(n):
	s = ''
	for i in range(n//2):
		s+='_'
	s = s + "New Task" + s
	print s


def sort(l):
	for i in range(len(l)-1):
		min = l[i]
		mini = i
		for j in range(i,len(l)):
			if l[j] < min:
				min = l[j]
				mini = j
			l[i],l[mini] = l[mini],l[i]
		return l


f = open(path,'w')
f.writeln('Hello,')
f.writeln('world')
f.close()


f = open(path,'r')
f.read()
file.readline()
lines = file.readlines()
f.close

f1 = open(path,'w')
f1.writelines(lines)
#usage when you need to close file automaticaly
with open("my_file") as somefile:
    do_something(somefile)

from tkinter import *
root = Tk()
