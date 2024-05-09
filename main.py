import pygame
import sys
import random
import bloques
import plataforma
import pelota
import colores

pygame.init()

plataforma = Plataforma.constructor(color = colores.getColor("AZUL"),
                                    ancho = 80,
                                    alto = 20,
                                    x = 400,
                                    y = 50,
                                    velocidad = 7)

pelota = Pelota.constructor(colores.getColor("RANDOM"),
                            radio = 20,
                            x = 400,
                            y = 300,
                            velocidad = 15)


pygame.draw.rect(VENTANA,
                Plataforma.getColor(plataforma),)

velocidad_bola = 5

ancho_plataforma, alto_plataforma = 100, 20
