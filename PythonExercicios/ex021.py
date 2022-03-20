'''Primeira Solução

import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()

pygame.event.wait()
input()'''

'''Segunda Solução'''
'''from playsound import playsound

playsound('musica.mp3')
input()'''
import pygame
pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play(start=35)
input()


