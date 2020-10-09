import pygame
import random
from prototype.factory import circle_creator
from iterator.agregado import agregate
from iterator.iterador import iterator
  
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
CAFE = (90, 50, 15)

cantidad_circulos = 2000

pygame.init()
Dimensiones = (800, 600)
Pantalla = pygame.display.set_mode(Dimensiones)
pygame.display.set_caption("Agar.io")

lista_circulos = []
creator = circle_creator()

for i in range(cantidad_circulos):
    lista_circulos.append(creator.get_circle())

posicionx = random.randrange(400)
posiciony = random.randrange(500)
radio_circulo = 10

Terminar = False
#Se define para poder gestionar cada cuando se ejecuta un fotograma
reloj = pygame.time.Clock()

while not Terminar:
    #---Manejo de eventos
    for Evento in pygame.event.get():
        if Evento.type == pygame.QUIT:
            Terminar = True

    #---La lógica del juego

    #---Movimiento del circulo
    x, y = pygame.mouse.get_pos()

    if x < posicionx and x < 800:
        posicionx = posicionx -1
    else:
        posicionx = posicionx +1
    if y < posiciony and y < 600:
        posiciony = posiciony - 1
    else:
        posiciony = posiciony + 1
        
    agregado = agregate(lista_circulos)
    iterador = agregado.get_iterador()

    #---Código de dibujo----
    Pantalla.fill(NEGRO)
    #--Todos los dibujos van después de esta línea
    flag = True
    while flag:
        circle = iterador.has_next()
        if circle != None:
            x1,y1 = circle.get_position()
            xr = abs(x1 - posicionx)
            xy = abs(y1 - posiciony)
            if  xr <= radio_circulo and xy <= radio_circulo:
                 circle.set_position(random.randrange(800),random.randrange(600))
                 radio_circulo = radio_circulo + 0.1
            pygame.draw.circle(Pantalla, circle.get_color(), circle.get_position(), circle.get_radio())
        else:
            flag = False

#--    for circle in lista_circulos:
#--        pygame.draw.circle(Pantalla, circle.get_color(), circle.get_position(), circle.get_radio())

    pygame.draw.circle(Pantalla, ROJO, [posicionx, posiciony], int(radio_circulo))

    #--Todos los dibujos van antes de esta línea
    pygame.display.flip()
    reloj.tick(20)  # Limitamos a 20 fotogramas por segundo

pygame.quit()