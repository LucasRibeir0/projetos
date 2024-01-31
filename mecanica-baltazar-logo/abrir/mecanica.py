import turtle,time
caneta = turtle.Turtle()

caneta.speed(0.1)
caneta.ht()
caneta.pensize(3)
caneta.color("white")
tela = turtle.Screen()
tela.bgcolor("grey11")


def horizontal():
    for h in range(100):
        caneta.right(0.5)
        caneta.forward(1)
    for h in range(110):
        caneta.left(0.5)
        caneta.forward(1.2)

def vertical():
    caneta.left(110)
    caneta.forward(130)

def LadoEsquerdo():
    caneta.right(114)
    caneta.forward(30)
    caneta.right(68)
def LadoDireito():
    caneta.left(60)
    caneta.forward(30)
    caneta.left(115)
def texto():
    caneta.penup()
    caneta.home()
    fonte1 = ("Brush",41,"bold")
    caneta.color("yellow")
    caneta.setpos(-115,90)
    caneta.write("mecânica", font=(fonte1))
    fonte2 = ("Brush",65,"bold")
    caneta.setpos(-110,20)
    caneta.write("Baltazar", font = (fonte2))
def contatos():
    time.sleep(1)
    fonte3 = ("!Crass Roots OFL",14)
    fonte4 = ("!Crass Roots OFL",24,"bold")
    fonte5 = ("AFONT LIGHT PERSONAL USE",14,"bold")
    caneta.color("white")
    caneta.setpos(-90,-45)
    caneta.write("Whatsapp: ", font=(fonte5))
    caneta.setpos(-90,-75)
    ddd = caneta.write("51", font=(fonte3))
    caneta.setpos(-65,-90)
    caneta.write("99986-5262",font=(fonte4))
    time.sleep(0.5)
    caneta.setpos(150,-45)
    caneta.write("Contato: ",font=(fonte5))
    caneta.setpos(150,-75)
    caneta.write("51",font =(fonte3))
    caneta.setpos(170,-90)
    caneta.write("3466-9632",font=(fonte4))
    time.sleep(1)
def endereco():
    fonte5 = ("AFONT LIGHT PERSONAL USE",20,"bold")
    caneta.setpos(-200,-150)
    caneta.write("Rua Latino Coelho, 250 Est. Velha - Canoas",font=(fonte5))



caneta.penup()
caneta.setx(-100)
caneta.pendown()
vertical()
caneta.right(70)
horizontal()
caneta.right(225)
vertical()
caneta.right(70)
horizontal()
'''LadoEsquerdo()
horizontal()
LadoDireito()
horizontal()
LadoEsquerdo()
horizontal()'''
texto()
contatos()
endereco()
time.sleep(2)
tela.bgcolor("black")
time.sleep(25)

