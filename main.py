import pygame
from collisionsMap import collision
from collision import * 
from background import *

pygame.init()

screen = pygame.display.set_mode((1920, 1080))
height = screen.get_height()
width = screen.get_width()

offset = {
    'x': width / 2,
    'y': height / 2
}

tileSize = 16
zoomMapLevel = 4

collisionsArray = collision()
collisionsMap = [int]

for i in range(0, len(collisionsArray), 35):
    collisionsMap.append(collisionsArray[0+i: 36+i])

FPS = 144
background = Background()
player_pos = pygame.Vector2(width / 2, height / 2)
    
clock = pygame.time.Clock()

for i in range(1, len(collisionsMap), 1):
    for j in range(0, 35, 1):
        if (collisionsMap[i][j] == 1):
            Collision(j*tileSize*zoomMapLevel, i*tileSize*zoomMapLevel)

text = ["on va tester les dialogues", "oui"]
bg = (pygame.image.load(background.imgSrc)).convert_alpha()

def dialogues(text_lines):
    pygame.font.init()
    font = pygame.font.SysFont(None, 65)

    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(width-width+300, height/2+200, width-590, height-760))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(width-width+315, height/2+215, width-620, height-790))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(width-width+345, height/2+240, width-width+225, 220))

    text_y_position = 770
    for line in text_lines:
        text_surface = font.render(line, True, (255, 255, 255))
        text_rect = (1200 // 2, text_y_position)
        screen.blit(text_surface, text_rect)
        text_y_position += 50

def info():
    pygame.font.init()
    font = pygame.font.SysFont(None, 50)
    text_info = "Press e to show dialogue, arrows to move"
    text_surface = font.render(text_info, True, (255, 255, 255))
    text_rect = (0, 0)
    screen.blit(text_surface, text_rect)

def main():
    while True:
        screen.fill('black')
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.blit(bg, (background.x, background.y))
        pygame.draw.circle(screen, "red", player_pos, 20)

        for i in allCollisions:
            pygame.draw.circle(screen, "red", (i.x,i.y), 8)

        info()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            background.x += 1
            for i in allCollisions:
                i.x +=1
        if keys[pygame.K_RIGHT]:
            background.x -= 1
            for i in allCollisions:
                i.x -=1
        if keys[pygame.K_UP]:
            background.y += 1
            for i in allCollisions:
                i.y +=1
        if keys[pygame.K_DOWN]:
            background.y -= 1
            for i in allCollisions:
                i.y -=1
        if keys[pygame.K_e]:
            dialogues(text)

        pygame.display.flip()

main()
