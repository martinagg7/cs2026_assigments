""" Let's try estimating PI through lots of different ways
@author: Patrick """

import math
import sys

# A function for guessing pi could be helpful...
def guessPi(guess):
    precision = 6 # amount of decimals we want in output
    diff = round(abs(math.pi - guess), precision)
    print("Guess of ", round(guess, precision), end='')
    print(" is off by", diff)


print("Naive guesses:")
guessPi(3.141593)
guessPi(4)
guessPi(22/7)



# Archimedes estimated pi using triangles and trigonometry.  
# Lets try it out here! See lecture slides...
def archimedies(numTriangles):
    innerAngle = 360/numTriangles
    innerAngle = math.radians(innerAngle)
    lenEachSide = 2 * math.sin(innerAngle/2)
    perimeter = lenEachSide * numTriangles
    radius = 1
    return perimeter / (2 * radius)

print("Archimedies:")
guessPi(archimedies(4))
guessPi(archimedies(8))
guessPi(archimedies(20))
guessPi(archimedies(20000))


# Lets try Leibniz ....  See lecture slides 



def leibniz(numTerms):
    numTracker = 0
    denom = 1
    isPlus = True
    for i in range(numTerms):
        if isPlus:
            numTracker += 1.0 / denom
        else:
            numTracker -= 1.0 / denom

        # for the next terms:
        isPlus = not isPlus
        denom = denom + 2

    combinedTerms = numTracker
    return 4 * combinedTerms

print("Leib:")
guessPi(leibniz(4))
guessPi(leibniz(8))
guessPi(leibniz(20))
guessPi(leibniz(20000))



# let's try wallis' approach.  See lecture slides
def wallis(numTerms):
    termsProd = 1
    for currNum in range(1, numTerms + 1, 2):
        top = currNum + 1  # each piece of the term
        botLeft = currNum
        botRight = currNum + 2
        # creates a term pair: 
        termPair = (top / botLeft) * (top / botRight) 
        termsProd *= termPair  # multiplies them into big product!
    return termsProd * 2

print("Wallis guesses:")
guessPi(wallis(1))
guessPi(wallis(4))
guessPi(wallis(8))
guessPi(wallis(20000))



import turtle
import random

def showMontePi(numDarts):
    wn = turtle.Screen()
    wn.setworldcoordinates(-1, -1, 1, 1) # this world center at 0,0
    pen = turtle.Turtle()
    pen.speed(6)
    pen.up()
    pen.goto(0,-1)
    pen.down()
    pen.circle(radius=1, steps=20)
    pen.up()
    
    dotsInCircle = 0
    for i in range(numDarts):
        x = random.random() * 2 - 1  # decimal between -1 and 1
        y = random.random() * 2 - 1
        distance = math.sqrt(x**2 + y**2)
        pen.goto(x, y)
        if distance <= 1:
            dotsInCircle += 1 
            pen.color("blue")
        else:
            pen.color("red")
        pen.dot(8)
        pi = dotsInCircle / (i+1) * 4
        print(pi)
    turtle.done()
    wn.exitonclick()
    return pi

print("Now some Monte-Python:")
showMontePi(3000)



print("Exiting Demo early..."); sys.exit(0)



# archived....

# archimedes estimated pi using triangles and trigonometry.  
# Lets try it out here! See lecture slides...
def arch(numSides):
    innerAng = 360 / numSides # inner angle of triangle
    # outside edge length of that triangle: 
    sideLen = 2 * math.sin(math.radians(innerAng) / 2)
    perim = numSides * sideLen # perimeter of shape
    radius = 1
    return perim / (2*radius) # pi = perimeter/diameter

print("Archimedes guesses:")
guessPi(arch(4))
guessPi(arch(8))
guessPi(arch(80))
guessPi(arch(8000))

# Lets try Leibniz ....  See lecture slides 
def leib(numTerms):
    termsSum = 0
    for currNum in range(numTerms):
        sign = 1 if currNum % 2 == 0 else -1
        aTerm = 4 / ((currNum * 2) + 1) # creates the term
        termsSum += sign * aTerm # sums them together
    return termsSum
        
print("leibniz guesses:")
guessPi(leib(1))
guessPi(leib(2))
guessPi(leib(20))
guessPi(leib(2000))


# let's try wallis' approach.  See lecture slides
def wallis(numTerms):
    termsProd = 1
    for currNum in range(1, numTerms + 1, 2):
        top = currNum + 1  # each peice of the term
        botLeft = currNum
        botRight = currNum + 2
        # creates a term pair: 
        termPair = (top / botLeft) * (top / botRight) 
        termsProd *= termPair  # multiplies them into big product!
    return termsProd * 2

print("Wallis guesses:")
guessPi(wallis(1))
guessPi(wallis(3))
guessPi(wallis(333))


import turtle
import random
def showMontePi(numDarts):
    wn = turtle.Screen()
    wn.setworldcoordinates(0, 0, 1, 1)
    try:
        pen = turtle.Turtle() # funny exception in sypder sometimes
    except:
        pen = turtle.Turtle()
    
    pen.goto(0,-1)
    pen.circle(1)
    numInCircle = 0
    pen.up()
    for i in range(numDarts):
        x = random.random()
        y = random.random()
        distance = math.sqrt(x**2 + y**2)
        pen.goto(x, y)
        if distance <= 1:
            numInCircle = numInCircle + 1
            pen.color("blue")
        else:
            pen.color("red")
        pen.dot()
        pi = numInCircle / (i+1) * 4
        print(pi)
    
    turtle.done()
    wn.exitonclick()
    return pi

print("Now some Monte-Pithon:")
# showMontePi(3000)


print("Exiting Demo early..."); sys.exit(0)



# some archived code....

def guessPi(n):
    diff = round(math.pi - n, 9)
    print("Your guess has error", diff)

guessPi(3)
guessPi(3.14)
guessPi(3.14159)
print("Exiting..."); sys.exit(0)


def archimedes(numSides):
    innerAngle = 360 / numSides
    oneSide = math.sin(math.radians(innerAngle / 2))
    return (oneSide * numSides)

# def archimedies(numSides):
#     innerA = 360 / numSides
#     oneSide = 2 * math.sin(innerA/2/180)
#     circum = oneSide * numSides
#     mypi = circum / 2
#     print("Archimedes with", numSides, "calculates to", mypi)
#     return mypi

guessPi(archimedes(4))
guessPi(archimedes(16))




























sys.exit(0) # prevents code below from running

def guessPi(guess):
    ''' shows a guess and how much error it has '''
    print('you guessed', guess, end=' ')
    print('your error is', abs(math.pi - guess))

print('basic guesses:')
guessPi(3)
guessPi(4)
guessPi(22/7)


def archimedes(numSides):
    innerAngle = 360 / numSides
    oneSide = math.sin(math.radians(innerAngle / 2))
    return (oneSide * numSides)

print("archimedes's estimates:")
guessPi(archimedes(4))
guessPi(archimedes(6))
guessPi(archimedes(11111))

def leibniz(numTerms):
    piGuess = 0
    isPlus = True
    for denom in range(1, numTerms*2, 2):
        term = 4/denom
        if isPlus:
            piGuess += term
        else:
            piGuess -= term
        isPlus = not isPlus
    return piGuess

print('Leibniz estimates:')
guessPi(leibniz(1))
guessPi(leibniz(3))
guessPi(leibniz(11111))

def wallis(numPairs):
    piGuess = 2
    for i in range(1, numPairs+1):   # [0]
        numer = 2 * i
        denom1 = numer - 1
        denom2 = numer + 1
        termPair = (numer / denom1) * (numer / denom2)
        piGuess *= termPair
    return piGuess

print("Wallis's estimates:")
guessPi(wallis(1))
guessPi(wallis(2))
guessPi(wallis(11111))


# sys.exit()
# print('does this line of code happen?')

import turtle
import random

def showMontePi(numDarts):
    wn = turtle.Screen()
    wn.setworldcoordinates(0, 0, 1, 1)
    try:
        pen = turtle.Turtle() # funny exception in sypder sometimes
    except:
        pen = turtle.Turtle()
    
    pen.goto(0,-1)
    pen.circle(1)
    numInCircle = 0
    pen.up()
    for i in range(numDarts):
        x = random.random()
        y = random.random()
        distance = math.sqrt(x**2 + y**2)
        pen.goto(x, y)
        if distance <= 1:
            numInCircle = numInCircle + 1
            pen.color("blue")
        else:
            pen.color("red")
        pen.dot()
        pi = numInCircle / (i+1) * 4
        print(pi)
    
    turtle.done()
    wn.exitonclick()
    return pi

print("Now some Monte-Pithon:")
# showMontePi(3000)
