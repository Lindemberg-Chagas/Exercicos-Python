#criar um tocador de mp3
import pygame
pygame.init()
pygame.mixer.music.load('hungriahiphop-amor-e-fe.mp3')
pygame.mixer.music.play()
input()
pyagame.event.wait()
