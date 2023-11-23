import pygame
from player import Player
from collisionsMap import collision
from collision import * 
from background import *

pygame.init()

screen = pygame.display.set_mode((1920, 1080))
height = screen.get_height()
width = screen.get_width()

#offset that moves the camera at the load of map
offset = {
    'x': width / 2,
    'y': height / 2
}

#size of each tile
tileSize = 16
#the zoomlevel exported from tiled
zoomMapLevel = 4

#1dArray with all collisions
collisionsArray = collision()
#2dArray witl all collisions
collisionsMap = [int]


#Make 1d to 2dArray
for i in range(0, len(collisionsArray), 35):
    collisionsMap.append(collisionsArray[0+i: 36+i])

FPS = 144

#create instance of background class 
background = Background()
player_pos = pygame.Vector2(width / 2, height / 2)
    
clock = pygame.time.Clock()

#create instance of all collision
for i in range(1, len(collisionsMap), 1):
    for j in range(0, 35, 1):
        if (collisionsMap[i][j] == 1):
            Collision(j*tileSize*zoomMapLevel, i*tileSize*zoomMapLevel)

text = ["on va tester les dialogues", "oui"]
#.convert_alpha() is very important, without it the game is much laggier
bg = (pygame.image.load(background.imgSrc)).convert_alpha()

def dialogues(text_lines):
    pygame.font.init()
    font = pygame.font.SysFont(None, 65)

    #draw the white outter line from dialogue
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(width-width+300, height/2+200, width-590, height-760))
    #draw the black inner line
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(width-width+315, height/2+215, width-620, height-790))
    #draw the character face
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(width-width+345, height/2+240, width-width+225, 220))

    text_y_position = 770
    #allow to have multiple lines of dialogue
    for line in text_lines:
        text_surface = font.render(line, True, (255, 255, 255))
        text_rect = (1200 // 2, text_y_position)
        screen.blit(text_surface, text_rect)
        text_y_position += 50

def info():
    #display all the info at the top of the screen
    pygame.font.init()
    font = pygame.font.SysFont(None, 50)
    text_info = "Press e to show dialogue, arrows to move"
    text_surface = font.render(text_info, True, (255, 255, 255))
    text_rect = (0, 0)
    screen.blit(text_surface, text_rect)

def move():
    #keys event
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        for i in allCollisions:
            check_collisions('left', i)
            #print(player.position_x, player.position_y)
        player.position_x -= 1
        background.x += 1
        for i in allCollisions:
            i.x +=1
    if keys[pygame.K_RIGHT]:
        player.position_x += 1
        background.x -= 1
        for i in allCollisions:
            i.x -=1
    if keys[pygame.K_UP]:
        player.position_y -= 1
        background.y += 1
        for i in allCollisions:
            i.y +=1
    if keys[pygame.K_DOWN]:
        player.position_y += 1
        background.y -= 1
        for i in allCollisions:
            i.y -=1
    if keys[pygame.K_e]:
        dialogues(text)

def check_collisions(direction: str, collision: Collision):
    if direction == 'left':
        #print(player.position_x, player.position_y, collision.x, collision.y)
        if (player.position_x - player.width <= collision.x + collision.size): #and
            #player.position_x <= collision.x and
            #player.position_y <= collision.y and
            #player.position_y >= collision.y):
            print("collision")
        else:
            print("pas collision")
    return True 

def main():
    while True:
        #re fill the whole screen therefore make it refresh each frame
        screen.fill('black')
        #limit frames by 144 atm
        clock.tick(FPS)

        #quit the game if f4
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        #fill the screen with background image at x, y
        screen.blit(bg, (background.x, background.y))
        #draw the player (just a red circle atm)
        pygame.draw.circle(screen, "red", player_pos, 20)

        #draw every collision
        for i in allCollisions:
            pygame.draw.circle(screen, "red", (i.x*4,i.y*4), 80)

        #display info text
        info()
        #get inputs and move the char
        move()

        #apply all the blit
        pygame.display.flip()

player = Player(width/2, height/2)
for i in allCollisions:
    #print(i.x, i.y)
    pass

main()
