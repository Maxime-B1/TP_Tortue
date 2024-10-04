import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.speed(0) # maximum speed



def equilateral(longueur) :
    for _ in range (3):
        t.forward(longueur)
        t.left(120)
        
def carré(longueur) :
    for _ in range (4):
        t.forward(longueur)
        t.left(90)
        
        
l = int(input("Quels longueur veut tu ? "))
carré(l)
turtle.exitonclick()