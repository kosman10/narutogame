import pygame
from sys import exit

from pygame.constants import K_LEFT, KEYDOWN, KEYUP, K_a, K_d, K_w
from spritesheet import Spritesheet

class Naruto:
    def __init__(self):
        self.bottom_x = 100
        self.bottom_y = 400
        self.gravity = 0
        self.standing = True
        self.moving_left = False
        self.moving_right = False
        self.jumping = False
        self.blocking = False
        self.facing_right = True
        self.facing_left = False
        self.stand = [[9,338,35,52],[58,338,37,52],[109,340,36,50],[161,339,35,51]]
        self.stand_index = 0
        self.move = [[9,421,37,47],[66,420,40,46],[122,422,38,46],[180,422,32,46],[229,421,38,47],[284,420,39,46],[345,422,38,46],[400,422,32,46]]
        self.move_index = 0
        self.jump = [[9,516,33,43],[54,495,40,51],[107,495,39,51],[167,494,34,52],[216,494,34,52],[269,516,33,43],[319,524,34,35],[366,516,33,43]]
        self.jump_index = 0

    def stand_animation(self):
        n = 5
        x,y,w,h = naruto.stand[round(naruto.stand_index/n)]
        naruto.stand_image = naruto_spritesheet.get_sprite(x,y,w,h)
        if naruto.facing_right:
            pass
        if naruto.facing_left:
            naruto.stand_image = pygame.transform.flip(naruto.stand_image, True, False)
        naruto.stand_rect = naruto.stand_image.get_rect(midbottom = (naruto.bottom_x,naruto.bottom_y))
        screen.blit(naruto.stand_image, naruto.stand_rect)
        naruto.stand_index += 1
        if round(naruto.stand_index/n) >= len(naruto.stand):
            naruto.stand_index = 0


    def move_animation(self,direction):
        n = 3
        x,y,w,h = naruto.move[round(naruto.move_index/n)]
        naruto.move_image = naruto_spritesheet.get_sprite(x,y,w,h)
        if direction == "right":
            pass
        elif direction == "left":
            naruto.move_image = pygame.transform.flip(naruto.move_image, True, False)
        naruto.move_rect = naruto.move_image.get_rect(midbottom = (naruto.bottom_x,naruto.bottom_y))
        screen.blit(naruto.move_image, naruto.move_rect)
        naruto.move_index += 1
        if round(naruto.move_index/n) >= len(naruto.move):
            naruto.move_index = 0
    

    def jump_animation(self, direction):
        naruto.standing = False
        n = 5
        x,y,w,h = naruto.jump[round(naruto.jump_index/n)]
        naruto.jump_image = naruto_spritesheet.get_sprite(x,y,w,h)
        if direction == "right":
            pass
        elif direction == "left":
            naruto.jump_image = pygame.transform.flip(naruto.jump_image, True, False)
        naruto.jump_rect = naruto.jump_image.get_rect(midbottom = (naruto.bottom_x,naruto.bottom_y))
        naruto.jump_rect.bottom += naruto.gravity
        screen.blit(naruto.jump_image, naruto.jump_rect)
        naruto.jump_index += 1
        if round(naruto.jump_index/n) >= len(naruto.jump):
            naruto.jumping = False
            naruto.gravity = 0
            naruto.jump_index = 0
       


#Initialising the game
pygame.init()
screen = pygame.display.set_mode((792,448))
pygame.display.set_caption("Naruto Game")
clock = pygame.time.Clock()
konoha_bg = pygame.image.load("assets/images/konoha_bg.png").convert_alpha()
konoha_bg = pygame.transform.scale(konoha_bg, (792,448))
ichiraku = pygame.image.load("assets/images/ichiraku.png").convert_alpha()
ichiraku.set_colorkey((49,82,140))
naruto_spritesheet = Spritesheet("assets/images/naruto.png")
sasuke_spritesheet = Spritesheet("assets/images/sasuke.png")

naruto = Naruto()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_d:
                naruto.standing = False
                naruto.jumping = False
                naruto.blocking = False
                naruto.moving_right = True
                naruto.facing_right = True
                naruto.moving_left = False
                naruto.facing_left = False
            
            if event.key == K_a:
                naruto.standing = False
                naruto.jumping = False
                naruto.blocking = False
                naruto.moving_right = False
                naruto.facing_right = False
                naruto.moving_left = True
                naruto.facing_left = True

            if event.key == K_w:
                naruto.standing = False
                naruto.jumping = True            
        
        if event.type == KEYUP:
            if event.key == K_d:
                naruto.standing = True
                naruto.jumping = False
                naruto.blocking = False
                naruto.moving_right = False
                naruto.facing_right = True
                naruto.moving_left = False
                naruto.facing_left = False  

            if event.key == K_a:
                naruto.standing = True
                naruto.jumping = False
                naruto.blocking = False
                naruto.moving_right = False
                naruto.facing_right = False
                naruto.moving_left = False
                naruto.facing_left = True
            


    screen.blit(konoha_bg, (0,0))
    screen.blit(ichiraku, (0,0))
    
    keys = pygame.key.get_pressed()


    if naruto.standing:
        naruto.stand_animation()

    if naruto.jumping:
        if naruto.gravity > -40:
            naruto.gravity -= 2
        else:
            naruto.gravity += 2
        if naruto.facing_right and not naruto.moving_right:
            naruto.jump_animation("right")
        if naruto.facing_right and naruto.moving_right:
            naruto.jump_animation("right")
            naruto.bottom_x += 5
        if naruto.facing_left and not naruto.moving_left:
            naruto.jump_animation("left")
        if naruto.facing_left and naruto.moving_left:
            naruto.jump_animation("left")
            naruto.bottom_x -= 5
    
    if naruto.moving_right and not naruto.jumping:
        if naruto.bottom_x >= 750:
            naruto.bottom_x += 0   #Preventing the sprite from leaving the display surface
            naruto.move_animation("right")
        else:
            naruto.bottom_x += 5
            naruto.move_animation("right")
        
    if naruto.moving_left and not naruto.jumping:
        if naruto.bottom_x <= 30:
            naruto.bottom_x += 0    #Preventing the sprite from leaving the display surface
            naruto.move_animation("left")
        else:
            naruto.bottom_x -= 5
            naruto.move_animation("left")
    
    if not (naruto.jumping or naruto.moving_left or naruto.moving_right):
        naruto.standing = True

    pygame.display.update()
    clock.tick(60)
    
# Need to match the end of the jump animations to sync with the end of the jump so they seamlessly touch the ground together
# Restructure code
# More animations needed