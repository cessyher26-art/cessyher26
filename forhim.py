import turtle
from turtle import *

wn = Screen( )
wn.bgcolor('black')

t =  turtle. Turtle( )
t.pencolor('white')

def curve( ):
    for i in range(200):
        t.rt(1)
        t.fd(1)
        
def heart( ):
     t.fillcolor('plum')
     t.begin_fill( )
     t.lt(140)
     t.fd(113)
     curve( )
     t.lt(120)
     curve( )
     t.fd(113)
     t.end_fill( )
     
heart( )
t.ht( )

def write(message, pos):
     x,y = pos
     t.penup( )
     t.goto(x,y)
     t.color('white')
     style = ('Stencil Std', 9, 'italic')
     t.write(message, font = style)
     
write('I', (-68,95))
write('L', (-55,95))
write('O', (-40,95))
write('V', (-20,95))
write('E', (-2,95))
write('Y', (23,95))
write('O', (38,95))
write('U', (57,95))
write('B', (-20,55))
write('A', (-2,55))
write('B', (17,55))
write('I', (35,55))

wn.mainloop( )