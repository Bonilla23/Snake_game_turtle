import turtle
import time
import random

# Tiempo de gracia
posponer = 0.1

#Marcador
score = 0
high_score = 0

# Configuración de la ventana
wn = turtle.Screen()
wn.title("Juego de la Serpiente")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0)

#Cabeza de serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square") 
cabeza.color("white")
cabeza.penup() # Sin dejar el rastro
cabeza.goto(0,0) # Posicion centro
cabeza.direction = "stop"

#Cuerpo serpiente
segmentos = []

#Comida de la serpiente
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle") 
comida.color("red")
comida.penup() # Sin dejar el rastro
comida.goto(0,100) # Posicion centro

#Marcador de puntos
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0         High Score: 0")

# Funciones de movimiento
def arriba():
    cabeza.direction = "up"

def abajo():
    cabeza.direction = "down"

def izquierda():
    cabeza.direction = "left"

def derecha():
    cabeza.direction = "right"


def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor() # Almacenar la variable Y
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor() # Almacenar la variable Y
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor() # Almacenar la variable Y
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor() # Almacenar la variable Y
        cabeza.setx(x + 20)

# Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

# Para correr el juego
while True:
    wn.update() #Actulizar la pantalla

    # Colisiones bordes
    if cabeza.xcor() > 280 or cabeza.ycor() < -290 or cabeza.ycor() > 290 or cabeza.xcor() < -290:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        #Esconder los segmentos
        for segmento in segmentos:
            segmento.goto(10000, 10000)

        # Limpiar segmentos
        segmentos.clear()

        #Resetear marcador
        score = 0
        texto.clear()
        texto.write("Score: {}  High Score: {}".format(score,high_score), font=("Courier",10,"normal"))
    # El cuadrado por defecto es 20pixel x 20 pixel
    # Para que la comida aparezca en un sitio al azar
    if cabeza.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square") 
        nuevo_segmento.color("grey")
        nuevo_segmento.penup() # Sin dejar el rastro
        segmentos.append(nuevo_segmento)

        #Aumentar marcador
        score += 10
        if score > high_score:
            high_score = score

        texto.clear()
        texto.write("Score: {}  High Score: {}".format(score,high_score), font=("Courier",10,"normal"))

    #Para que se mueva con el cuerpo
    totalSeg = len(segmentos) # Total de cuerpo
    for index in range(totalSeg -1,0,-1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)
    
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    mov()

    # Colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            # Esconder los segmentos
            for segmento in segmentos:
                segmento.goto(1000,1000)

            # Limpiar la lista
            segmentos.clear()

            # Resetear marcador
            score = 0
            texto.clear()
            texto.write("Score: {}  High Score: {}".format(score,high_score), font=("Courier",10,"normal"))

    time.sleep(posponer)

