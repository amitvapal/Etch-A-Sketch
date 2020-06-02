'''
Student Name: Amitva Pal
Game title: Etch a Sketch
Period: 6/7
Features of Game: User is able to draw anything they want to and clear the screen and make another one if they want to
'''

import pygame, sys                                      #pulls in the special code functions for pygame
pygame.init()                                           #initialize game engine

w=640                                                   #Open and set window size
h=480                                                   #must code graphics to auto resize based on window size
size=(w,h)
surface = pygame.display.set_mode(size)

pygame.display.set_caption("Etch a Sketch")          #set window title

#declare global variables here

BLACK    = (   0,   0,   0)                             #Color Constants 
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

#other global variables (WARNING: use sparingly):
leftRect = pygame.Rect(0,0,w/10,h)
topRect = pygame.Rect(0,0,w,h/10)
rightRect = pygame.Rect(w*9/10,0,w*9/10,h)
bottomRect = pygame.Rect(0, h*8/10, w, h*8/10)


def drawScene():
    surface.fill(WHITE)
    pygame.draw.rect(surface, RED, leftRect, 0)
    pygame.draw.rect(surface, RED, topRect, 0)
    pygame.draw.rect(surface, RED, rightRect, 0)
    pygame.draw.rect(surface, RED, bottomRect, 0)
    name = pygame.image.load("etch.gif").convert_alpha()
    surface.blit(name, [w/3.5,h*7.5/10])
    pygame.draw.ellipse(surface, WHITE, (w/20, h*8.2/10,70,70),0)
    pygame.draw.ellipse(surface, WHITE, (w-w*1.5/9, h*8.2/10,70,70),0)
    
    
def drawBrush(brushPos, color):
    pygame.draw.circle(surface, color,brushPos, 4 ,0)

def moveBrush(keys,brushPos):
    if keys[pygame.K_UP] == True:
        brushPos[1] -= 1
    if keys[pygame.K_LEFT] == True:
        brushPos[0] -= 1    
    if keys[pygame.K_RIGHT] == True:
        brushPos[0] += 1    
    if keys[pygame.K_DOWN] == True:
        brushPos[1] += 1 
    if topRect.collidepoint(brushPos):
        brushPos[1]+=1
    if bottomRect.collidepoint(brushPos):
        brushPos[1]-=1   
    if rightRect.collidepoint(brushPos):
        brushPos[0]-=1 
    if leftRect.collidepoint(brushPos):
        brushPos[0]+=1    

    return brushPos


def getColorChoice(keys,color):
        if keys==pygame.K_1:
            color = RED
        elif keys==pygame.K_2:
            color= BLUE
        elif keys==pygame.K_3:
            color = GREEN 
        elif keys==pygame.K_0:
            color = BLACK
        return color    



    

clock = pygame.time.Clock()                            # Manage timing for screen updates
                                                        # Uncomment when timing/animation is needed


#Program helper functions:






# -------- Main Program Loop -----------
def main():
    brushPos = [int(w/2), int(h/2)]
    drawScene()
    color = BLACK
    #every program should have a main function
                                                        #other functions go above main
    
    #declare local game variables here 
    #brushPos = brush()
    
    while (True):
        
        keys = pygame.key.get_pressed()
        brushPos = moveBrush(keys, brushPos)
        
        for event in pygame.event.get():                #get all events in the last 1/60 sec & process them
            
            if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                pygame.quit();                          #for ending the game & closing window
                sys.exit();
                
            
        
            # if your program has a button, mouse, or keyboard interaction, code goes at this indentation level
            
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                brushPos=[int(w/2), int(h/2)]
                drawScene()
                color = BLACK
            if event.type == pygame.KEYDOWN:
                color = getColorChoice(event.key,color)
                
        
        # ongoing game logic that occurs ever 1/60 second goes @ this indentation level
        
        
      
                                     #set background color
        
        #drawing code goes here
        
        
        drawBrush(brushPos, color)
        clock.tick(60)                                  #Change FPS - frames per sec- when animating
        pygame.display.update()                          #updates the screen- usually in main
        
        
        
            
main()                                                   #this calls the main function to run the program
