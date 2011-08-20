import pygame
import maps
pygame.init()
pygame.mixer.init()
pygame.font.init()

size = 640, 480
clock = pygame.time.Clock()

wall = pygame.image.load("wall.png")
floor = pygame.image.load("floor.png")
coin = pygame.image.load("coin.png")

screen = pygame.display.set_mode(size)

bump = pygame.mixer.Sound("bump.wav")
ping = pygame.mixer.Sound("coin.wav")

score = pygame.font.Font("terminus.ttf",14)

pwalkfront = pygame.image.load("player_front.png")
pwalkright = pygame.image.load("player_right.png")
pwalkback = pygame.image.load("player_back.png")
pwalkleft = pygame.image.load("player_left.png")

class Player:
    def __init__(self,posx,posy):
        self.posx = posx
        self.posy = posy
        self.position = [posx * 40, posy * 40]
        self.image = pwalkfront
        self.location = maps.testmap
        self.coin = 0
    def update(self):
        self.position = [self.posx * 40, self.posy * 40]
        if self.location.array[self.posy][self.posx] == 2:
            ping.play()
            self.location.array[self.posy][self.posx] = 0
            self.coin += 1
        if self.location.array[self.posy][self.posx] > 2:
            newmap = self.location.array[self.posy][self.posx]
            
        screen.blit(self.image,self.position)
    def run(self,event):
        potx = 0; poty = 0
        if event.key == pygame.K_LEFT:    potx = -1; self.image = pwalkleft
        elif event.key == pygame.K_RIGHT: potx = 1;  self.image = pwalkright
        elif event.key == pygame.K_UP:    poty = -1; self.image = pwalkback
        elif event.key == pygame.K_DOWN:  poty = 1;  self.image = pwalkfront

        if self.location.array[self.posy + poty][self.posx + potx] != 1:
            self.posx += potx; self.posy += poty
        else:
            bump.play()

frogman = Player(5,5)
gamequit = 0

def showmap(mapname):
    row = 0; column = 0;
    for maprow in mapname:
        column = 0
        for tile in maprow:
            if tile == 1:
                screen.blit(wall,[column * 40, row * 40])
            elif tile == 2:
                screen.blit(coin,[column * 40, row * 40])
            else:
                screen.blit(floor,[column * 40, row * 40])
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
    screen.blit(text,(280,80))

pygame.mixer.music.load("room1.wav")
pygame.mixer.music.play(-1)
while not gamequit:
    clock.tick(30)
    getinput()
    showmap(frogman.location.array)
    frogman.update()
    scoreboard()
    pygame.display.flip()
