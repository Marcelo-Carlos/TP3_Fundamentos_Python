#Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um quadrado vermelho de 100 px de lado no centro da tela. O quadrado deve ser capaz de se movimentar vertical e horizontalmente através de teclas do computador. Pode ser ‘a’,’s’,’d’,’w’ ou as setas do teclado. (código e printscreen)
import pygame
from pygame.locals import *

pygame.init()
screen_with, screen_heigth = 800, 600
tela = pygame.display.set_mode((screen_with, screen_heigth))
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
RED, BLUE = (255, 0, 0), (0, 0, 255)
tela.fill(BLACK)
square_width, square_height = 30, 30

class Teclas:
    def __init__(self, w, a, s, d):
        self.w = w
        self.a = a
        self.s = s
        self.d = d
        
x, y = screen_with/2 - square_width, screen_heigth/2 - square_height
teclas = Teclas(False, False, False, False)


def draw_square_red(x,y):
    cor = RED
    pygame.draw.rect(tela, cor, (x,y,square_width, square_height), 0)
        
def move_rect(teclas, x,y):
    if teclas.w and y > 0:
        y -= 1
    elif teclas.a and y < screen_heigth - 30:
        y += 1
    if teclas.s and x > 0:
        x -= 1
    elif teclas.d and x < screen_with-30:
        x += 1
    return x,y    

def write_text(text):
    font = pygame.font.Font(None, 24)
    text = font.render(text, 1, WHITE)
    textpos = text.get_rect(centerx=tela.get_width()/2)
    tela.blit(text, textpos)


terminou = False
while not terminou:
    tela.fill(BLACK)    
    write_text("Question 10 - TP3")    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        #Enquanto estiver pressionado     
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                teclas.w = True
            elif event.key == K_a:
                teclas.a = True
            if event.key == K_s:
                teclas.s = True
            if event.key == K_d:
                teclas.d = True
        #Momento que parar a tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                teclas.w = False
            elif event.key == pygame.K_a:
                teclas.a = False
            elif event.key == pygame.K_s:
                teclas.s = False
            elif event.key == pygame.K_d:
                teclas.d = False                 
        
    x, y = move_rect(teclas, x, y)
    draw_square_red(x, y)
    pygame.display.update() 
            
pygame.display.quit()
pygame.quit()