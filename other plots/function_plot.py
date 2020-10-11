from turtle import *
from math import atan2, sqrt, sin, cos
from math import pi
from PIL import Image

def parabola2():
    #y = 0.5*a*x^2 - b
    a = 0.03
    b=50
    scale = 5
    X0 = (0,0.5/a-b)
    penup()
    goto(0,-b)
    pendown()
    for t in range(0,20):
        x = scale*t
        goto(x,0.5*a*x**2-b) 
    
    penup()
    goto(0,-b)
    pendown()
    for t in range(0,20):
        x = -scale*t
        goto(x,0.5*a*x**2-b) 
    
    penup()
    x = scale*10
    goto(x,150-b)
    seth(270)
    pendown()
    goto(x,100-b)
    stamp()
    goto((x,0.5*a*x**2-b))
    goto(X0)
    dot()
    
    return 'parabola'



def ellipse2():
    #(x/a)^2+(y/b)^2=1
    a,b = 5,4
    c = sqrt(a**2-b**2)
    scale = 30
    F0=(c*scale,0)
    F1=(-c*scale,0)
    
    n=50
    up()
    goto(a*scale,0)
    down()
    for i in range(0,721,4):
        x = a*scale*cos(i*pi/180/2)
        y = b*scale*sin(i*pi/180/2)
        goto(x,y)
    
    up()
    goto(F1)
    down()
    dot()
    up()
    goto(F0)
    down()
    dot()
    seth(90)
    for k in range(1):
        (x,y) = pos()
        i=0
        while (x/a)**2+(y/b)**2<scale**2:
            fd(1)
            (x,y)=pos()
            if(abs(y-b*scale/3)<0.1):
                stamp()
        angle = atan2(y-F1[1],x-F1[0])*180/pi
        seth(180+angle)
        fd(150)
        stamp()
        goto(F1)
        (x,y) = pos()
        i=0
        while (x/a)**2+(y/b)**2<scale**2:
            fd(1)
            (x,y)=pos()
        angle = atan2(y-F0[1],x-F0[0])*180/pi
        seth(180+angle)
        goto(F0)
    fd(20)
    stamp()
    
    return 'ellipse'
    
        
#moth
def moth_trace():
    step = 1
    dot()
    angleconst = 60
    up()
    goto(160,0)
    (x,y) = pos()
    angle = atan2(y,x)*180/pi
    seth(180-angleconst+angle)
    down()
    i=0
    while abs(pos())>2 and i<3000:
        fd(step)
        (x,y) = pos()
        angle = atan2(y,x)*180/pi
        seth(180-angleconst+angle)
        i += 1
        if i==200:
            stamp()
    print('moth')


def main():
    setup(400,400)
    speed(0)
    #parabola2()
    #ellipse2()
    moth_trace()
    
    ht()    

if __name__ == "__main__":
    TurtleScreen._RUNNING=True
    main()
    exitonclick()