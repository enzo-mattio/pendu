import random
import pygame
from pygame.locals import *


AUTHORIZED_KEYS=[ord(i) for i in range(x,y)]

with open(f"asset/mot_facile.txt") as fichier:
  liste_mot_up = fichier.read()

liste_mot_up=liste_mot_up.split('\n')

print(liste_mot_up)
mot_random = random.choice(liste_mot_up)

display_mot=["_"]*len(mot_random)

DISPLAYSURF.blit(TIMES_NEW.render(' '.join(display_mot), True, BLACK)(posx,posy))
#BingChilling

def interactive_gameplay(display_mot):
  temp_word=''
  for event in events:
    if event.type==pygame.KEYDOWN and event.unicode in AUTHORIZED_KEYS :
      if event.key == pygame.R_BACKSPACE or event.unicode =='\08x':
        temp_word=temp_word[:-1]
        display_mot[len(temp_word)]='_'
      if event.unicode in mot_random:
        temp_word+=event.unicode
        display_mot[len(temp_word-1)]=event.unicode
    pygame.display.update()

