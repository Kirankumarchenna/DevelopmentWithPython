a, b, c = 10, 20, 30
print(a + b + c)
print(type(a))
a = 'Hello'
a = True
print(a)
print(type(a))


def f(): print("Good boy")  ##Defining a function and printing something without any class any method anything


f()  ##Simply calling the function.

for i in range(10):
    print(i)

x = 10 if a > b else 30
print(x)

x = 20.5
if x == 20:
    print("Hello", type(x))
else:
    print("Pora", type(x))

import math

print(math.sqrt(5))

from random import *

for i in range(10):
    print('Your OTP is: ', randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9),
          sep="")

from random import *

print(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), sep='')

import keyword

var = keyword.kwlist
print(var)

a = 10
print('This value has been stored under object: ', id(a))

a = 0B1010
print(a)

a = 0o456
print(a)

a = 0xFace
print(a)

print(bin(470972))
print(bin(0XFace))
print(oct(42224))

f = 1.3e8
print(f)

a = 10 + 34j
b = 34 + 45j
print(type(a))
print(a)
print(a + b)
print(a - b)
print(a.real)
print(a.imag)

a = 'Hello'
for i in range(5):
    print(a[i])

b = 'Bagunnava'
print(b[1:5])

a = 'Kiran '
print(a * 10)

print(int(476.390))
print(float(476))
print(int(476.390))
print(int(True))
print(int(False))
print(complex(78, 43))
print(complex(True))
print(bool(3.4))

x = [10, 20, 30, 40]
y = bytes(x)
print(type(y))
print("Value of a second letter in an array: ", y[1])
for i in y:  ##For each loop
    print(i)
for i in range(len(y)):  ##For loop
    print(y[i])

##y[0]= 23           ##This couldn't be possible bcz Bytes are immutable
a = [10, 30, 70, 89]
b = bytearray(a)
print(type(b))
b[0] = 130           ##This assiging operation has been performed bcz bytearray is mutable and the range must be 0-256 only
for i in b:
    print(i)

l=[]                ##List must be specified as [] square Braces
print(type(l))
l.append('Kiran')
l.append(90)
l.append(78)
l.append(67)
l.append('Hello all')
print(l)
print(l[1:4])
l.remove(78)
print(l)

k = [29, 'Kiran', True]
k1 = k*2
print(k1)

k = (78, 76, 45, 'Kiran')  ##Tuple
print(type(k))
print(k)
##k[0] = 89    ##cannot allowed bcz immutable

r1 = range(10)
r2 = range(10, 90)
r3 = range(10, 90, 5)
for i in r3:
    print(i)

s = {10, 30, 20, 10, 20, 30}
print(s)               ##No duplicates and no insertion order maintainance
s.add('Kiran')
s.add('Kumar')          ##Mutable
print(s)

