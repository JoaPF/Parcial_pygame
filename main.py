from datos import lista
from funciones import *
import pygame
from pygame import draw
#sonido_fondo = pygame.mixer.Sound("pac_man/sound/pac_man.mp3")
#pygame.mixer.Sound.play(sonido_fondo, -1)

#Colores
blanco = (255,255,255)
negro = (0,0,0)
rojo = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
dorado = (248, 222, 65)
titulo_azul = (86, 98, 246)
rojo_salir = (245, 37, 50)
naranja =  (255, 147, 0)

#          0: inicio, 1: juego, 2: puntajes
pantalla = 0
running = True
p_inicio = True
p_puntajes = False
jugando = False


pygame.init() #Se inicializa pygame

screen = pygame.display.set_mode([800,800]) #Se crea una ventana
img_fondo = pygame.image.load("imagenes/fondo.png")

sonido_fondo = pygame.mixer.Sound("sonidos/musicafondo.mp3")
sonido_fondo.set_volume(0.05)


font = pygame.font.SysFont("arial", 25)

#TITULOS
font_titulos = pygame.font.SysFont("timesnewroman", 30,True)
txt_titulo = font_titulos.render("DESAFIO PREGUNTADOS",True,negro)
txt_titulo_puntajes = font_titulos.render("",True,negro)
#MENU PRINCIPAL
txt_boton_jugar = font.render("Jugar",True,negro)
txt_boton_puntajes = font.render("Puntajes",True,blanco)
txt_boton_salir = font.render("Salir",True,blanco)


rect_titulo =pygame.Rect(10,10,100,50)

boton_jugar = pygame.Rect(216,532,100,50)
boton_puntajes = pygame.Rect(350,532,100,50)
boton_salir = pygame.Rect(482,532,100,50)

while running:
    screen.blit(img_fondo,(0,0))
    pygame.mixer.Sound.play(sonido_fondo, -1) # "-1" para loop

    #obtengo eventos
    for event in pygame.event.get():
        #Se verifica si el usuario cerro la ventana
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN :
            if boton_jugar.collidepoint(event.pos):
                pantalla = 1

            if boton_puntajes.collidepoint(event.pos):
                pantalla = 2

            if boton_salir.collidepoint(event.pos):
                running = False


    match pantalla:
        #Menu principal
        case 0:
            screen.blit(txt_titulo,(200,50))

            draw.rect(screen,dorado,boton_jugar,border_radius=15)
            draw.rect(screen,naranja,boton_puntajes,border_radius=15)
            draw.rect(screen,rojo_salir,boton_salir,border_radius=15)
            screen.blit(txt_boton_jugar,(234,541))
            screen.blit(txt_boton_puntajes,(350,541))
            screen.blit(txt_boton_salir,(505,541))

        #juego
        case 1:

            print("jugando")
            pantalla = 0

        #pantalla de puntajes
        case 2:
            print("puntajes:")
            with open("puntajes.json") as set_datos:
                datos = json.load(set_datos)
            ordenar_lista_en_dict(datos,"puntajes","puntaje")
            print(datos["puntajes"][0]["nombre"],":",datos["puntajes"][0]["puntaje"])
            print(datos["puntajes"][1]["nombre"],":",datos["puntajes"][1]["puntaje"])
            print(datos["puntajes"][2]["nombre"],":",datos["puntajes"][2]["puntaje"])
            pantalla = 0



    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        pass
    
    pygame.display.flip()#Muestra los cambios en la pantalla
pygame.quit()
