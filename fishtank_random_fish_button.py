import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1200, 800))

cash = 500
fish_tank_fw = []
fishtype = 0
    
# --- Class Definitions ---
class Fish:
    def __init__(self):
        self.xpos = random.randint(0, 750)
        self.ypos = random.randint(0, 550)
        
    def fish_random(self, screen):
        global fishtype
        if cash >= 25:
            fishrand = random.randint(0, 100)
            if fishrand == 30:
                fish1 = pygame.draw.rect(screen, (250, 250, 250), (self.xpos, self.ypos, 40, 40))
                fish_tank_fw.append(fish1)
                fishtype = 0
            elif fishrand == 55:
                fish2 = pygame.draw.rect(screen, (30, 30, 30), (self.xpos, self.ypos, 40, 40))
                fish_tank_fw.append(fish2)
                fishtype = 0
            else:
                fish3 = pygame.draw.rect(screen, (80, 80, 80), (self.xpos, self.ypos, 40, 40))
                fish_tank_fw.append(fish3)
                fishtype = 0
        
        
class Button:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.is_open = False
        self.color_closed = (139, 69, 19)  # Brown
        self.color_open = (255, 215, 0)    # Gold

    def check_click(self, mouse_pos):
        mx, my = mouse_pos
        if (mx > self.x and mx < self.x + self.width and
            my > self.y and my < self.y + self.height):
            self.is_open = True

    def toggle_closed(self):
        self.is_open = False

    def draw(self, screen):
        if self.is_open == True:
            current_color = self.color_open
        else:
            current_color = self.color_closed
        pygame.draw.rect(screen, current_color, (self.x, self.y, self.width, self.height))


button = Button(240, 140, 115, 100) #instantiate an object
fish = Fish()
running = True


while running:
    #Event Handling-----------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
           
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                button.check_click(event.pos)
                if cash >= 25:
                    fish.fish_random(screen)
                    print(fish_tank_fw)
                    fishtype = 1
                else:
                    print("NOT ENOUGH CASH")
                    
           
        if event.type == pygame.MOUSEBUTTONUP:
            button.toggle_closed()

    #Render Section-------------------------------------------------------------------
    screen.fill((0, 0, 180))
    fish.fish_random(screen)
    button.draw(screen)
    pygame.display.flip()

pygame.quit()