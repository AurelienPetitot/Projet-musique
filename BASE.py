from music21 import *
import pygame , sys
import time
import pyautogui
from pynput.keyboard import Key, Controller

#Gestion Interface Pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))

COULEUR_BLANCHE = pygame.Color(255, 255, 255)

ECRAN = pygame.display.set_mode((400,400))
ECRAN.fill(COULEUR_BLANCHE)
pygame.display.set_caption("MELODIE MAKER")

done = False


# 1. Partie Piano Numerique

pygame.mixer.init()
pygame.mixer.music.load("PIANO.ogg")
n = pygame.mixer.Sound("PIANO-A4.ogg")
j = pygame.mixer.Sound("PIANO-A_4.ogg")
COMMA = pygame.mixer.Sound("PIANO-B4.ogg")
w = pygame.mixer.Sound("PIANO-C4.ogg")
s = pygame.mixer.Sound("PIANO-C_4.ogg")
x = pygame.mixer.Sound("PIANO-D4.ogg")
d = pygame.mixer.Sound("PIANO-D_4.ogg")
c = pygame.mixer.Sound("PIANO-E4.ogg")
v = pygame.mixer.Sound("PIANO-F4.ogg")
g = pygame.mixer.Sound("PIANO-F_4.ogg")
b = pygame.mixer.Sound("PIANO-G4.ogg")
h = pygame.mixer.Sound("PIANO-G_4.ogg")



# 1. A : Gestion Touche clavier


MELODIE=[]

keyboard = Controller()
def main():
    a = time.time()
    SUITE = True


    while SUITE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                SUITE = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    
                    
                    
                    for i in MELODIE:
                        print(MELODIE)
                        note = i[1]
                        #print(note)
                        temps = i[0]
                        #print(temps)

                        
                        

                        
                        keyboard.press(note)
                        
                        keyboard.type(".")
                        pyautogui.press("p")
                        pyautogui.press("l")
                        pyautogui.press("a")
                        pyautogui.press("y")
                        pyautogui.press("(")
                        pyautogui.press(")")
                        pyautogui.press("backspace")

                        
                        
                    
                        
                        time.sleep(temps)
                        pygame.mixer.fadeout(1000)
                        
                    return MELODIE
                                
                    

                
                
                
                if event.key == pygame.K_w:
                    w.play()
                if event.key == pygame.K_s:
                    s.play()
                if event.key == pygame.K_x:
                    x.play()
                if event.key == pygame.K_d:
                    d.play()
                if event.key == pygame.K_c:
                    c.play()
                if event.key == pygame.K_v:
                    v.play()
                if event.key == pygame.K_g:
                    g.play()
                if event.key == pygame.K_b:
                    b.play()
                if event.key == pygame.K_h:
                    h.play()
                if event.key == pygame.K_n:
                    n.play()
                if event.key == pygame.K_j:
                    j.play()
                if event.key == pygame.K_COMMA:
                    COMMA.play()

                bb = time.time()
                MELODIE.append([round(bb-a,2), pygame.key.name(event.key)])
                print(bb-a)
                print(MELODIE)
                
                

            elif event.type == pygame.KEYUP:
                pygame.mixer.fadeout(1000)

            
            

main()










    
                
            
       
