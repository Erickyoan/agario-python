import pygame
import random
from prototype.factory import circle_creator
from iterator.agregado import agregate
from iterator.iterador import iterator
  
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
CAFE = (90, 50, 15)
BLANCO =(255,255,255)

# score
score=0

cantidad_circulos = 2000
velocidad=2

#


pygame.init()
dimensiones = (1000, 1000)
Pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Agar.io")

lista_circulos = []
creator = circle_creator()

for i in range(cantidad_circulos):
    lista_circulos.append(creator.get_circle())


#enemy
xe= random.randrange(1000)
ye= random.randrange(1000)

posicionxe = random.randrange(1000)
posicionye = random.randrange(1000)
radio_circuloe= 10

posicionx = random.randrange(1000)
posiciony = random.randrange(1000)
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

    if x < posicionx and x < 1000:
        posicionx = posicionx -velocidad
    else:
        posicionx = posicionx +velocidad
        
    if y < posiciony and y < 1000:
        posiciony = posiciony - velocidad
    else:
        posiciony = posiciony + velocidad
    
    #---Movimiento enemy
    
    if xe < posicionxe and xe < 1000:
        posicionxe = posicionxe -velocidad
    else:
        posicionxe = posicionxe +velocidad
        
    if ye < posicionye and ye < 1000:
        posicionye = posicionye - velocidad
    else:
        posicionye = posicionye + velocidad
        
    
   
        
    scoreText=pygame.font.Font(None, 102)
    
    
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
            
            xre = abs(x1 - posicionxe)
            xye = abs(y1 - posicionye)
            
            if  xr <= radio_circulo and xy <= radio_circulo:
                 circle.set_position(random.randrange(800),random.randrange(600))
                 radio_circulo = radio_circulo + 0.1
            
       
            
        
            
            if  xre <= radio_circuloe and xye <= radio_circuloe:
                 circle.set_position(random.randrange(800),random.randrange(600))
                 radio_circuloe = radio_circuloe + 0.1
            
            # if  xre <=  and xye <= radio_circuloe:
            #      circle.set_position(random.randrange(800),random.randrange(600))
            #      radio_circuloe = radio_circuloe + 0.1
                 
                 
            pygame.draw.circle(Pantalla, circle.get_color(), circle.get_position(), circle.get_radio())
        
        
        else:
            flag = False
            
#--    for circle in lista_circulos:
#--        pygame.draw.circle(Pantalla, circle.get_color(), circle.get_position(), circle.get_radio())
    
    
    # Dibujo del Score
    Pantalla.blit(scoreText.render(str(score), True, BLANCO),(5,5))
    
    pygame.draw.circle(Pantalla, ROJO, [posicionx, posiciony], int(radio_circulo))
    pygame.draw.circle(Pantalla,CAFE,[posicionxe, posicionye], int(radio_circuloe))
    
    
    score=(int(radio_circulo))
    
        
    #--Todos los dibujos van antes de esta línea
    pygame.display.flip()
    reloj.tick(20)  # Limitamos a 20 fotogramas por segundo

pygame.quit()