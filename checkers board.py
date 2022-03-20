import math
import turtle
tao = turtle.Pen()
tao.shape('turtle')

def go(x,y):
    '''move to (x,y)'''
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

def standby():
    '''turn left 90 degree'''
    tao.penup()
    tao.left(90)

def star1():
    '''start to draw star'''
    tao.forward(10)
    tao.left(180-18)
    tao.pendown()
    tao.forward(10*math.sin(36*math.pi/180)*math.cos(36*math.pi/180))

def star2():
    '''draw 4 V-shape'''
    tao.right(180-108)
    tao.forward(10*math.sin(36*math.pi/180)*math.cos(36*math.pi/180))
    tao.left(180-36)
    tao.forward(10*math.sin(36*math.pi/180)*math.cos(36*math.pi/180))

def star3():
    '''end star'''
    tao.right(180-108)
    tao.forward(10*math.sin(36*math.pi/180)*math.cos(36*math.pi/180))
    tao.left(180-18)
    tao.penup()
    tao.forward(10)
    standby()

def star():
    '''draw star'''
    standby()
    star1()
    for i in range(4):
        star2()
    star3()

def rectangular():
    '''draw rectangular'''
    tao.penup()
    tao.forward(20)
    tao.pendown()
    tao.left(90)
    tao.forward(20)
    for i in range(3):
        tao.left(90)
        tao.forward(40)
    tao.left(90)
    tao.forward(20)
    tao.penup()
    tao.left(90)
    tao.forward(20)
    standby()
    standby()

'''draw checkers board'''

vertical = 8
count = 0
x = -140
y = -140
go(x,y)
while vertical > 0:
    horizontal = 8
    while horizontal > 0:
        if count % 2 == 0:
            star()
            rectangular()
        else:
            rectangular()
        count = count + 1
        tao.forward(40)
        horizontal = horizontal - 1
    go(x,y+40)
    vertical = vertical - 1
    y = y + 40
    count = count + 1
