#Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um círculo azul de 
# 100 px de diâmetro no centro da tela que se move da esquerda para a direita. 
# Sempre que chegar na extremidade direita, o círculo deve voltar à extremidade esquerda, 
# retomando o movimento da esquerda para a direita. 
from question_10 import BLACK, BLUE
import pygame
from pygame.locals import *

pygame.init()
largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
RED, BLUE = (255, 0, 0), (0, 0, 255)
tela.fill(BLACK)   
x, y = largura_tela/2, altura_tela/2


def draw_blue_circle(x,y):
    cor = BLUE
    pygame.draw.circle(tela, BLUE, (x, y), 50)
        
def move_element(x,y):        
    if x < largura_tela:
        x += 0.5
    elif x == largura_tela:
        x += 0.5
    elif x > largura_tela:
        x = 0.5
    return x,y    

def write_text(text):
    font = pygame.font.Font(None, 24)
    text = font.render(text, 1, WHITE)
    textpos = text.get_rect(centerx=tela.get_width()/2)
    tela.blit(text, textpos)

stop = False
while not stop:
    tela.fill(BLACK)    
    write_text("Question 11 - TP3")    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True              
                               
    x, y = move_element(x, y)
    draw_blue_circle(x, y)   
    pygame.display.update() 
                   
pygame.display.quit()
pygame.quit()