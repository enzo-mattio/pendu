import random
import pygame
from pygame import *
from pygame.locals import *
import keyboard
import os 
import random




# Désignation des couleurs
WHITE=(255,255,255)
BLACK=(0,0,0)
RED = (255,0,0)
BLUE=(0,0,255)

# Initalisation variable
mot_trouve = ""
mot_tampon=""
mot_random=""
lettre_tapee = ""
lettre_dans = []
lettre_fausse = ''
lettre_utilise=""
mot_trouve_affiche = ""
alphabet="abcdefghijklmnopqrstuvwxyz"
errors =  0
choix="facile"

win = False
lose = False
game_on = False

# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre
window_size = (800, 600)
game_space_size=(400,600)

game_place = (0,0)

# Création de la fenêtre
screen = pygame.display.set_mode(window_size)
DISPLAYSURF=pygame.display.set_mode(window_size)

game_space=pygame.Surface(game_space_size)


# Définition des tailles des boutons
button_width = 100
button_height = 50

# Définition des positions des boutons
button1_x = 450
button1_y = 200

# Dessin du premier bouton
button1=pygame.Rect(button1_x, button1_y, button_width, button_height)

# Dessin du second bouton

font1 = pygame.font.SysFont('chalkduster.ttf', 72)


# _____________________________________________________________ #

AUTHORIZED_KEYS = [ord(chr(i)) for i in range(65, 91)]



display_mot=["_"]*len(mot_random)
text = font1.render(' '.join(display_mot), True, BLACK)
game_space.blit(text, (20, 200))

#BingChilling

def interactive_gameplay(display_mot):
  global errors
  temp_word=''
  for event in events:
    if event.type==pygame.KEYDOWN and event.unicode in AUTHORIZED_KEYS :
      if event.key == pygame.R_BACKSPACE or event.unicode =='\08x':
        temp_word=temp_word[:-1]
        display_mot[len(temp_word)]='_'
      if event.unicode in mot_random:
        temp_word+=event.unicode
        display_mot[len(temp_word)-1]=event.unicode
      else:
        if event.unicode not in mot_random and lettre_fausse:
          lettre_fausse += event.unicode
          errors = len(lettre_fausse)


def afficher_mot_trouve(couleur, x, y):
  mot_trouve_affiche = ""
  
  for i in mot_tampon:
    if i in lettre_tapee:
      mot_trouve_affiche += i
    else:
      mot_trouve_affiche += "_"
    
  texte = font1.render(mot_trouve_affiche, True, couleur)
  game_space.blit(texte, (x, y))
  
def gagne():
  win = False
  if mot_trouve_affiche == mot_random:
    texte_win = font1.render("c'est gagné", True, BLACK)
    game_space.blit(texte_win, (20,400))
  else:
    pass

def ajout_lettre():
  global lettre_dans, alphabet, lettre_tapee, errors, lettre_fausse
  for lettres in alphabet:
    if keyboard.release(lettres):
      lettre_tapee += lettres
      game_space.fill(RED)
      
    else:
      pass
  if lettre_tapee in mot_random:
    lettre_dans += lettre_tapee
    
  else:
    if lettre_tapee in lettre_fausse :
      pass
    else:
      lettre_fausse += lettre_tapee
  errors = len(lettre_fausse)

def draw_errors(x,y):
  global errors
  
  img = pygame.image.load(f'img/pendu{errors}.png')
  img.convert()
  rect = img.get_rect()
  rect.center = x//2, y//2
  DISPLAYSURF.blit(img, rect)
  pygame.draw.rect(DISPLAYSURF, WHITE, rect, 1)
  
def choix_mot(choix):
  liste_mot_up = []
  with open(f"asset/mot_{choix}.txt") as fichier:
    liste_mot_up = fichier.read()
  liste_mot_up=liste_mot_up.split('\n')
  return random.choice(liste_mot_up)

mot_random=choix_mot("moyen")



    
DISPLAYSURF.fill(WHITE)
game_space.fill(RED)
 
running = True


while running:
  
  events=pygame.event.get()
  
    
  # pygame.draw.rect(DISPLAYSURF, BLACK, button1)
  
  DISPLAYSURF.blit(game_space, (0,0)) 
  draw_errors(400, 300)
  # afficher_mot_trouve(BLACK, 20,200)
  interactive_gameplay(display_mot)
  # ajout_lettre()
  # verif_lettre()
  gagne()
  
 
  # erreur = font1.render(lettre_utilise, True, BLACK)
  # game_space.blit(erreur, (20, 600))
  
  
  pygame.display.update()
  for event in events:
    if event.type == pygame.KEYDOWN:
      if event.key == K_ESCAPE:
        running = False
  


# Quitter Pygame
pygame.quit()


  
  
