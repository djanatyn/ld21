import pygame
import maps
pygame.init()
pygame.mixer.init()
pygame.font.init()

size = 640, 480
clock = pygame.time.Clock()
pygame.key.set_repeat(100,100)

wall = pygame.image.load("wall.png")
floor = pygame.image.load("floor.png")
coin = pygame.image.load("coin.png")
title = pygame.image.load("title.png")
gui = pygame.image.load("gui.png")

screen = pygame.display.set_mode(size)

bump = pygame.mixer.Sound("bump.wav")
ping = pygame.mixer.Sound("coin.wav")

score = pygame.font.Font("visitor1.ttf",18)

pwalkfront = pygame.image.load("player_front.png")
pwalkright = pygame.image.load("player_right.png")
pwalkback = pygame.image.load("player_back.png")
pwalkleft = pygame.image.load("player_left.png")

enemy = pygame.image.load("robot.png")

class Player:
    def __init__(self,posx,posy):
        self.posx = posx
        self.posy = posy
        self.position = [posx * 30, posy * 30]
        self.image = pwalkfront
        self.location = maps.list[0]
        self.coin = 0
    def update(self):
        self.position = [self.posx * 30, self.posy * 30]
        if self.location.array[self.posy][self.posx] == 2:
            ping.play()
            self.location.array[self.posy][self.posx] = 0
            self.coin += 1
        if self.location.array[self.posy][self.posx] > 2:
            newmap = self.location.array[self.posy][self.posx]
            self.posx, self.posy = self.location.exits[newmap][1]
            mapnum = self.location.exits[newmap][0]
            self.location = maps.list[mapnum]
        screen.blit(self.image,self.position)
    def run(self,event):
        potx = 0; poty = 0
        if event.key == pygame.K_LEFT:
            potx = -1;
            self.image = pwalkleft;
        elif event.key == pygame.K_RIGHT:
            potx = 1;
            self.image = pwalkright
        elif event.key == pygame.K_UP:
            poty = -1;
            self.image = pwalkback
        elif event.key == pygame.K_DOWN:
            poty = 1;
            self.image = pwalkfront
        if potx != 0 or poty != 0:
            if self.location.array[self.posy + poty][self.posx + potx] != 1:
                self.posx += potx; self.posy += poty
            else:
                bump.play()
class Enemy:
    def __init__(self,posx,posy):
        self.posx = posx
        self.posy = posy
        self.position = [posx * 30, posy * 30]
        self.time = 0
    def move(self):
        if self.time > 250:
            self.time = 0; potx = 0; poty = 0
            if frogman.posx > self.posx: potx = 1
            if frogman.posx < self.posx: potx = -1
            if frogman.posy > self.posy: poty = 1
            if frogman.posy < self.posy: poty = -1
            if frogman.location.array[self.posy + poty][self.posx] != 1:
                self.posy += poty
            if frogman.location.array[self.posy][self.posx + potx] != 1:
                self.posx += potx
    def update(self):
        self.position = [self.posx * 30, self.posy * 30]
        screen.blit(enemy,self.position)

frogman = Player(5,5)
badguy = Enemy(10,10)
gamequit = 0

def showmap(mapname):
    row = 0; column = 0;
    for maprow in mapname:
        column = 0
        for tile in maprow:
            if tile == 1:
                screen.blit(wall,[column * 30, row * 30])
            elif tile == 2:
                screen.blit(coin,[column * 30, row * 30])
            else:
                screen.blit(floor,[column * 30, row * 30])
            column += 1
        row += 1

def getinput():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            frogman.run(event)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE: pygame.quit(); gamequit = 1

def scoreboard():
    text = score.render("coins: %s" % (frogman.coin),0,(0,0,0))
    screen.blit(text,(500,10))

pygame.mixer.music.load("title.wav")
pygame.mixer.music.play(-1)
while not gamequit:
    badguy.time += clock.tick(30)
    getinput()
    showmap(frogman.location.array)
    frogman.update()
    badguy.move()
    badguy.update()
    screen.blit(title,(0,360))
    screen.blit(gui,(480,0))
    scoreboard()
    pygame.display.flip()
