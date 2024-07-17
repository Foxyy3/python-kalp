import math
from turtle import *
def kalp(e):
    return 15*math.sin(e)**3
def kalpe(e):
    return 12*math.cos(e)-5*\
    math.cos(2*e)-2*\
    math.cos(3*e)-\
    math.cos(4*e)
speed(10000)
bgcolor ("black")
for m in range(6000):
    goto(kalp(m)*20,kalpe(m)*20)
    for i in range(5):
        color("red")
        goto(0,0)
done(exit)