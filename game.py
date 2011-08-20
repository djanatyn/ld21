import pygame

pygame.init()

size = 640, 480
clock = pygame.time.Clock()

wall = pygame.image.load("wall.png")
floor = pygame.image.load("floor.png")

screen = pygame.display.set_mode(size)

testmap = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

def showmap(mapname):
    row = 0; column = 0;
    for maprow in mapname:
        column = 0
        for tile in maprow:
            if tile == 1:
                print "wall at (%s,%s)" % (row,column)
                screen.blit(wall,[column * 40, row * 40])
            elif tile == 0:
                print "floor at (%s,%s)" %  (row,column)
                screen.blit(floor,[column * 40, row * 40])
            column += 1
        row += 1

while True:
    clock.tick(30)
    showmap(testmap)
    pygame.display.flip()



