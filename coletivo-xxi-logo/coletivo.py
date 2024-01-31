import turtle
from time import sleep
print("Desenvolvido por: Lucas Ribeiro Goncalves")
print("2022")
#Inicializando turtle
caneta = turtle.Turtle()
caneta.ht()
caneta.speed(0.0001)
caneta.pensize(5)
caneta.color("white")
tela = turtle.Screen()
tela.bgcolor("#f8d74a")


def CurvaPalma():
    caneta.forward(50)
    for c in range(80):
        caneta.right(1)
        caneta.forward(0.5)
    caneta.forward(100)
def palma():
    caneta.fillcolor("white")
    caneta.begin_fill()
    caneta.penup()
    caneta.setpos(-100,-200)
    caneta.pendown()
    caneta.left(180)
    caneta.forward(40)
    caneta.left(40)
    caneta.forward(30)
    caneta.right(60)

    for c in range(230):
        if c <= 50:
            caneta.right(0.8)
            caneta.forward(1.5)
        elif c > 50 and c <=150:
            caneta.right(0.5)
            caneta.forward(2)
        elif c > 150 and c<= 230:
            caneta.right(1)
            caneta.forward(1)
    for c in range(20):
        caneta.right(0.2)
        caneta.forward(0.5)
    caneta.left(17)
    caneta.forward(180)
    caneta.right(20)
    for c in range(85):
        caneta.right(1.6)
        caneta.forward(1.2)
    caneta.left(115)

    CurvaPalma()

    caneta.right(26)
    for c in range(95):
        caneta.right(1.2)
        caneta.forward(1.2)
    caneta.left(133)
    caneta.forward(66)
    caneta.end_fill()
    caneta.penup()
def DedoMindinho():
    #Lado esquerdo do dedinho
    caneta.setpos(-215,82)
    caneta.fillcolor("white")
    caneta.begin_fill()
    caneta.pendown()
    for c in range(35):
        caneta.right(3)
        caneta.forward(1)
    caneta.forward(40)
    for c in range(20):
        caneta.left(1)
        caneta.forward(0.5)
    for c in range(68):
        caneta.right(1)
        caneta.forward(1)
    caneta.left(95)
    caneta.forward(10)
    caneta.right(45)
    caneta.forward(30)
    #Lado direito do dedinho
    for c in range(60):
        caneta.right(3.1)
        caneta.forward(1)

    caneta.forward(156)
    caneta.right(25)
    caneta.forward(10)
    caneta.end_fill()
    caneta.penup()
def DedoAnelar():

    caneta.setpos(-125, 118)
    caneta.fillcolor("white")
    caneta.begin_fill()
    caneta.pendown()
    def InicioDoAnelar():
        for c in range(55):
            caneta.right(3)
            caneta.forward(1.2)
    InicioDoAnelar()

    caneta.forward(50)
    caneta.right(70)
    caneta.forward(15)
    caneta.left(120)
    caneta.forward(15)
    caneta.right(50)
    caneta.forward(60)
    caneta.right(70)
    caneta.forward(15)
    caneta.left(150)
    caneta.forward(15)
    caneta.right(90)
    caneta.forward(50)
    InicioDoAnelar()
    caneta.right(8)
    caneta.forward(180)
    caneta.end_fill()
    caneta.penup()
def DedoMedio():
    caneta.setpos(-80,111)
    caneta.fillcolor("white")
    caneta.begin_fill()
    caneta.pendown()
    for c in range(70):
        caneta.left(2.2)  # 2
        caneta.forward(0.7)
    caneta.forward(60)
    for c in range(57):
        if c <= 30:
            caneta.left(3)
            caneta.forward(0.8)
        else:
            caneta.right(9)
            caneta.forward(2)
    caneta.left(150)  # 140
    caneta.forward(100)
    for c in range(89):  # 91
        caneta.left(2)
        caneta.forward(0.7)
    caneta.forward(196)
    caneta.end_fill()
    caneta.penup()
def DedoIndicador():
    caneta.setpos(37,104)

    caneta.fillcolor("white")
    caneta.begin_fill()
    caneta.pendown()
    for c in range(65):
        caneta.right(3.3)
        caneta.forward(1)
    caneta.left(16)
    caneta.forward(22)
    for c in range(40):
        caneta.right(2)
        caneta.forward(0.8)
    caneta.left(150)
    caneta.forward(18)
    caneta.right(63)
    caneta.forward(134)
    for c in range(90):
        caneta.right(2.1)
        caneta.forward(0.8)
    caneta.forward(60)
    caneta.right(53)
    caneta.forward(30)
    caneta.left(120)
    caneta.forward(30)
    caneta.right(62)
    caneta.forward(93)
    caneta.end_fill()
    caneta.penup()
def DedoPolegar():
    caneta.setpos(94,-13)
    caneta.fillcolor("white")
    caneta.begin_fill()
    caneta.pendown()
    for c in range(40):
        caneta.left(1.5)
        caneta.forward(1)
    caneta.left(80)
    caneta.forward(50)
    caneta.left(50)
    caneta.forward(20)
    caneta.right(120)
    caneta.forward(20)
    caneta.left(65)
    caneta.forward(50)
    for c in range(100):
        caneta.left(2.2)
        caneta.forward(1.5)
    caneta.right(19)
    caneta.forward(85)
    caneta.end_fill()
    caneta.penup()
    sleep(1)
def texto():
    caneta.setpos(-285,15)
    roxo = ("#5d16ec")
    fonte1 = ("StationNo.7w00-Seven",85)
    fonte2 = ("StationNo.7w00-Seven",75)
    caneta.color(roxo)
    caneta.write("Coletivo",font=(fonte1))
    caneta.setpos(-165,-100)
    caneta.write("XXI",font=(fonte2))
    sleep(2)
def contato():
    caneta.setpos(-225,-270)
    preto = (0,0,0)
    fonte = ("StationNo.7w00-Seven",35)
    caneta.color(preto)
    caneta.write("@coletivoxxi",font=(fonte))

#Chamando as funções
palma()
DedoMindinho()
DedoAnelar()
DedoMedio()
DedoIndicador()
DedoPolegar()
texto()
contato()
sleep(10)
