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
        #for c in ("turquoise", "purple", "green", "pink"):
            #t.color(c)
        t.forward(longueur)
        longueur=longueur+ajout
        t.right(angle)
        
def figure1() :
    l=5
    for _ in range (50):
        polygone(l,4, 5, 1)
        l=l+4*5
    
figure1()

turtle.exitonclick()