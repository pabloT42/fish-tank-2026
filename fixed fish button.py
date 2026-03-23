import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1200, 800))

fish_tank_fw = []

    
# --- Class Definitions ---
class Fish:
    def __init__(self):
        self.xpos = random.randint(0, 750)
        self.ypos = random.randint(0, 550)
        self.color = random.choice([(250, 250, 250),(30, 30, 30),(80, 80, 80)])
        
    def draw(self,screen):
        pygame.draw.rect(screen, self.color, (self.xpos,self.ypos, 40, 40))
        
        
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
            return True
        return False

    def toggle_closed(self):
        self.is_open = False

    def draw(self, screen):
        if self.is_open == True:
            color = self.color_open
        else:
            color = self.color_closed
            
        pygame.draw.rect(screen, color, (self.x,self.y, self.width, self.height))
        
        

button = Button(240, 140, 115, 100) #instantiate an object


running = True
while running:
    #Event Handling-----------------------------------------------------------------
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
           
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if button.check_click(event.pos):
                    new_fish = Fish()
                
                fish_tank_fw.append(new_fish)
        
           
            elif event.type == pygame.MOUSEBUTTONUP:
                button.toggle_closed()

    #Render Section-------------------------------------------------------------------
    screen.fill((0, 0, 180))
    
    for fish in fish_tank_fw:
        fish.draw(screen)
    
    button.draw(screen)
    pygame.display.flip()

pygame.quit()
