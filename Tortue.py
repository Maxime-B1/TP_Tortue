import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.speed(0) # maximum speed



def equilateral(longueur) :
    polygone(longueur,3)
        
def carré(longueur) :
    polygone(longueur,4)
        
def polygone(longueur, nb_cotes, ajout=0, deviation=0):
    angle = (360/nb_cotes) - deviation
    for _ in range (nb_cotes):
        t.forward(longueur)
        longueur=longueur+ajout
        t.right(angle)
        

polygone(100, 4, 20, 5)

turtle.exitonclick()