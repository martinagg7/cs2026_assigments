""" Learn a bit about how functions work...
@author: Patrick """

'''We can use the python interpreter to explore some of these while coding.  
try using help(str) or help(len) when using the interactive Python '''

import sys

import matplotlib # test that this work...
print("Exiting demo..."); sys.exit()


name = " Patrick     "
name = name.strip() # removes out whitespace on ends of strings!
# strip function is useful especially if the user is typing input
course = "   cs2064 ".strip()

print(name, "is taking", course)

courseNum = int(course[-4:])
print("that is in the ", 1000*int(courseNum/1000), "s range", sep='')


print("Exiting demo..."); sys.exit()


# what is that 'sep' part above?  Answer: a default parameter!
print("Default parameters let us change the ", end='')
print("default","behavior","of","functions", sep='#')

print(1,2,3,4, sep="   ", end='!!! \n') # newline is a special character

# making our own default parameters:
def greeting(who, loudness=0, says="hello"):
    ending = "!" * loudness
    print(who, "says:", says, ending)

greeting("Mario")
greeting("Luigi", says="GREAT SCOTT", loudness=5)


print(list("hello"))
print(" , ".join(list("hello"))) # another nice string function: join
# it makes a list of things into one string



# functions are objects.  Python has lots of built-in ones...
print("Calling the length function on hello is:", len('hello'))
print("The len function itself is:", len)

### hmmm... can we create a len function?



print(print)

import math
print(math, " <-- modules in python are objects too!")
print(math.sin)


def greeting():
    print('hi')
# a = 4
# def greeting():
#     global a
#     a = 7
#     print("hi there")
#     print("a is", a)
# print(a)

print(greeting())

# print(a)

print(greeting) 
print("Functions we define have a location ^^^ in our computer's memory")

# print(a = 7)

def greeting():
    pass
print(greeting) 
print("re-defining that function changes it !!!")

otherGreet = greeting

print(otherGreet)


# want to learn more about a built-in function?  Use the help function!
# print(help(math.sin))
# print(help(sys.exit))

print("Exiting demo..."); sys.exit()
















# Functions and return!
myList = [1, 2, 3 ,4]
print(myList)
print(set(myList))
print([myList])
print(set("hello world"))




# Familiar functions (built-ins!)
# See all the builtin functions: https://docs.python.org/3.11/library/functions.html
# print, len, help, type, int, str, bool, range
help(print)
print("loading time", end='... \n\n\n')
import time
time.sleep(1)
print('done!')
print("The", "answer", "is", 3*14, sep='', end='')
help(str)
print(int("00011011101101011", base=2))
print(str(1) + str(1))
help(range)
print(list(range(2, 400, 13)))


# String METHODS
# capitalize, strip
print("Hello World".upper())
print("  \n\n\n  Hello   ".strip())
print("  Hello  to the  \n\n   world! ".split())

# Cool list functions
# zip, next
# Also: unzipping using * (pretty advanced...)






# help(zip)
alphas = 'a b c'.split()
sounds = 'do re me'.split()
nums = [1,2,3]

for a, s, n in zip(alphas, sounds, nums):
    print(f"{n=} {a} {s}") # whoa an f-string?
print(f"{sounds=}")

# for c in [1,2,3,4,9,8,7,6]:
#     print(c)

# for a,b in zip("hello", "world"):
#     print(a,b)

i = 3333
print(type(i))
print(sys.getsizeof(i))


print()


sys.exit()

# Learning about data sizes: 
# sys.getsizeof()
### Also, floating point precision


### Functions as THINGS (objects)
help(help)

def half(x):
    return x/2

def triple(x):
    return x*3

for fun in [half, triple]:
    print(fun(5))










# Old version with other tidbits, but doesn't 
# need a live demo::: 

# phrase = "hello World!"
# print(phrase.capitalize())

numbers = [1,       2,      3]
letters = [   'a',     'b',    'c']
zipped = zip(numbers, letters)
#print(type(zipped))

#print(next(zipped))
#print(next(zipped))
#print(next(zipped))
# print(next(zipped))  <-- this one breaks

#print(list(zipped))

numbers_set = {1,2,3}
letters_set = {'a', 'b', 'c'}
#print(list(zip(numbers_set, letters_set)))
#print(list(zip(letters_set, numbers_set)))

#print(sys.getsizeof('abcde'))
#print(sys.getsizeof('abcd'))
#print(sys.getsizeof(42))
#print(sys.getsizeof(-42))
#print(sys.getsizeof(424242424242424242424242424242))
#print(sys.getsizeof(42424242424242424242))

# 0, 1, 2, 3, ...., 8, 9, 10, 11, 12, ..., 98, 99, 100, 101, 102
# 0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101, ...
# 10010100 10010111 10101001 10100101
# 11111111 11111111 11111111 11111111 + 1
# 00000000 00000000 00000000 00000001 00000000 00000000 00000000 00000000

#print(sys.getsizeof(42.42))
#print(sys.getsizeof(4242424242424242424242424242424242424242.42))
#print(sys.getsizeof(42.4242424242424242424242424242424242424242))
#print(sys.getsizeof(42424242424242424242.424242422424242424242424242))

# IEEE 754
# +/-  exponent   precision
#  1      8          23

# 10^4 10^3 10^2 10^1 10^0 . 10^-1, 10^-2, 10^-3, 10^-4
# 2^4 2^3 2^2 2^1 2^0 . 2^-1 2^-2 2^-3 2^-4
# 0.5 -> 0.1
# 0.25 -> 0.01
# 0.0625 -> 0.0001
# 0.1 -> 0.000110011001100110011001100110011001100110011001100...

def applyFunction(data, func):
    results = []
    for item in data:
        results.append(func(item))
    return results

def square(value):
    return value**2

myList = [1, -2, -5, 6.2]

# print(applyFunction(myList, abs))
# print(applyFunction(myList, float))
# print(applyFunction(myList, square))

myFunctions = [abs, float, square]

for f in myFunctions:
    # print(applyFunction(myList, f))
    pass

i = abs
# print(i(-5))


### CLASS 
alistOfChars=list("hello world")
separator = "..."
print(alistOfChars)
print(separator.join(alistOfChars))
print(print)
print(print.__doc__)
print(help(print))

print=4
print(print)