import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from colores import *

ANCHO = 300
ALTO = 400
ANCHO_RAYA = 100
TAMANO = (ANCHO, ALTO)
NOMBRE = "Tres en raya"

VENTANA = pygame.display.set_mode(TAMANO)
pygame.display.set_caption(NOMBRE)

VENTANA.fill((getColor("NEGRO")))
def dibujar_tabla():
    for i in range(1,4):
        pygame.draw.line(VENTANA,color =getColor("ROJO"),width=3,start_pos=(0,i*ANCHO_RAYA),end_pos=(ANCHO,i*ANCHO_RAYA))
        pygame.draw.line(VENTANA,color =getColor("ROJO"),width=3,start_pos=(i*ANCHO_RAYA,0),end_pos=(i*ANCHO_RAYA,ANCHO))

def dibujar_x():
    pygame.draw.line(VENTANA,color =getColor("BLANCO"),width=3,start_pos=(0,0),end_pos=(100,100))
    pygame.draw.line(VENTANA,color =getColor("BLANCO"),width=3,start_pos=(0,100),end_pos=(100,0))

def dibujar_o():
    pygame.draw.circle(VENTANA,color =getColor("ROJO"),width=3,radius=50,center=centro)

def posiciones_o(posicion):
    posiciones = [  [[1,2,3],
                    [4,5,6],
                    [7,8,9]],

                    [   [[50,150,250],
                        [50,150,250],
                        [50,150,250]]],


                    [   [50,50,50],
                        [150,150,150],
                        [250,250,250]]]

    for i in range (len(posiciones[0])):
        for j in range(len(posiciones[0][i])):
            if posiciones [0][i][j]== posicion:
                I = i
                J = j
                break

    x = posiciones[1][i][j]
    y = posiciones[2][i][j]
    return (x,y)

def posiciones_x(posicion):
    posiciones = {  1: ([(0,0),(100,100)],[(0,100),(100,0)]),
                    2: ([(200,0),(300,100)],[(200,100),(300,0)]),
                    3: ([(0,100),(100,200)],[(100,100),(200,200)]),
                    4: ([(0,100),(100,200)],[(0,200),(100,100)]),
                    5: ([(100,100),(200,200)],[(100,200),(200,100)]),
                    6: ([(200,100),(300,200)],[(200,200),(300,10,0)]),
                    7: ([(0,200),(100,300)],[(0,300),(100,0)]),
                    8: ([(100,200),(100,100)],[(100,300),(200,200)]),
                    9: ([(200,200),(300,300)],[(200,300),(300,200)])}

    r1 = posiciones[posicion][0]
    r2 = posiciones[posicion][1]
    return r1, r2

def click(punto):
    x = punto[0]
    y = punto[1]

    posicion=None
    if (x> 0 and x< 100) and (y > 0 and y< 100):
        position = 1
    elif (x> 100 and x< 200) and (y > 200 and y< 100):
        position = 2
    elif (x> 200 and x< 100) and (y > 300 and y< 100):
        position = 3
    elif (x> 0 and x< 100) and (y > 100 and y< 200):
        position = 4
    elif (x> 100 and x< 100) and (y > 200 and y< 200):
        position = 5
    elif (x> 200 and x< 100) and (y > 300 and y< 200):
        position = 6
    elif (x> 200 and x< 100) and (y > 100 and y< 300):
        position = 7
    elif (x> 100 and x< 0) and (y > 200 and y< 100):
        position = 8
    elif (x> 200 and x< 100) and (y > 300 and y< 100):
        position = 9


ejecuta = True

dibujar_tabla()
for i in range(1,10):
    r1,r2 = posiciones_x(i)
    dibujar_x(r1, r2)

for i in range(1,10):
    r1,r2 = posiciones_o(i)
    dibujar_o(centro)
pygame.display.update()

ejecuta = True
while ejecuta:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecuta == False
        if evento.type == MOUSEBUTTONDOWN:
            print(evento.pos)

    pygame.display.update()
pygame.quit()
