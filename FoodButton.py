import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Fish Simulator")
clock = pygame.time.Clock()

class Fish:
    def __init__(self):
        self.fishImage = pygame.image.load("BlueFish.png").convert_alpha()
        pygame.Surface.set_colorkey (self.fishImage, [255,0,255])
        self.xpos = random.randint(0, 750)
        self.ypos = random.randint(0, 550)
        self.speed = 1
        self.xDir = random.randint(-1,1)
        self.yDir = random.randint(-1,1)
        self.last_change_time = time.time() #grab starting time

    def move(self):
        # move the fish
        self.xpos += self.xDir* self.speed
        self.ypos += self.yDir * self.speed

        # Change direction every 3 seconds
        if time.time() - self.last_change_time > 3:  
            self.xDir = random.randint(-1,1)
            self.yDir = random.randint(-1,1)
            self.last_change_time = time.time() #reset the time

        # Check for collision with walls and change direction
        if self.xpos <= 0 or self.xpos >= 750:
            self.xDir *= -1
        if self.ypos <= 0 or self.ypos>= 550:
            self.yDir *= -1

    def draw(self, screen):
        screen.blit(self.fishImage, (self.xpos, self.ypos))

# food variables
fish = Fish()
food_size = 10
food_x = 0
food_y = 0
food_falling = False
food_speed = 30


#button---------+++++++++++++
button_rect = pygame.Rect(650, 10, 140, 40)
font = pygame.font.SysFont(None, 24)

running = True
while running:# Game loop########################################################
    clock.tick(60)
    #input/event section-----------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
           
    if event.type == pygame.MOUSEBUTTONDOWN: #Key
        if button_rect.collidepoint(event.pos):
            if not food_falling:
                food_x = random.randint(10, 790)
                food_y = 0
                food_falling = True

    #physics/update section--------------------------
    fish.move()
    # --- Food falling ---
    if food_falling:
        food_y += food_speed

    fish_rect = pygame.Rect(fish.xpos, fish.ypos,
                            fish.fishImage.get_width(),
                            fish.fishImage.get_height())

    food_rect = pygame.Rect(food_x, food_y, food_size, food_size) #define the food rect

    # Collision with fish
    if fish_rect.colliderect(food_rect):
        food_falling = False # food stops falling
        fish.fishImage = pygame.transform.scale( #makes image to have width and height
            fish.fishImage,
            (fish.fishImage.get_width()+2, fish.fishImage.get_height()+2)# make bigger fish when eats
        )
        
        
    # Food falls off screen
    if food_y > 900:
        food_falling = False

    #render section----------------------------------

    screen.fill((0, 150, 255))


    fish.draw(screen)
    if food_falling:
        pygame.draw.rect(screen, (255, 200, 0), (food_x, food_y, food_size, food_size))

   
    pygame.draw.rect(screen, (200, 200, 200), button_rect) #button
    text = font.render("Feed Fish", True, (0,0,0))
    screen.blit(text, (button_rect.x+20, button_rect.y+10))    
    # Update the display
    pygame.display.flip()

    #end of game loop!#######################################################

pygame.quit()
