import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.speed(0) # maximum speed



def equilateral(longueur) :
    polygone(longueur,3)
        
def carré(longueur) :
    polygone(longueur,4)
        
def polygone(longueur, nb_cotes):
    for _ in range (nb_cotes):
        t.forward(longueur)
        t.left(360/nb_cotes) 
        

polygone(100,5)
polygone(200,5)

turtle.exitonclick()