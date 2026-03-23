import pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("State Machine Demo")

BLACK = (0, 0, 0)


font1=pygame.font.SysFont("arial",48,True); #choose font
text1=font1.render("intructions/tutorial",True,(0,0,0)); #say what to print to screen
text2=font1.render("tropical tank",True,(0,0,0)); #say what to print to screen
text3=font1.render("freshwater tank",True,(0,0,0)); #say what to print to screen
text4=font1.render("fish collection book",True,(0,0,0)); #say what to print to screen



# === Main Map State ===
class MainState:
    def __init__(self):
        self.bg_color = (200, 200, 255)
        self.door = pygame.Rect(100, 170, 50, 50)
        self.doort = pygame.Rect(100, 240, 50, 50)
        self.doorfw = pygame.Rect(100, 310, 50, 50)
        self.doorfc = pygame.Rect(100, 390, 50, 50)
        self.data = {} 

    def update(self):
        pass

    def draw(self):
        screen.fill(self.bg_color)
        pygame.draw.rect(screen, BLACK, self.door)
        pygame.draw.rect(screen, BLACK, self.doort)
        pygame.draw.rect(screen, BLACK, self.doorfw)
        pygame.draw.rect(screen, BLACK, self.doorfc)
        screen.blit(text1,(200,170)) #draw text
        screen.blit(text2,(200,240))
        screen.blit(text3,(200,310))
        screen.blit(text4,(200,390))


# === tutorial State ===
class HouseState:
    def __init__(self):
        self.bg_color = (255, 255, 255)
        self.door = pygame.Rect(10, 10, 50, 50)
        self.data = {}

    def update(self):
        pass

    def draw(self):
        screen.fill(self.bg_color)
        pygame.draw.rect(screen, BLACK, self.door)
        
        
# === Tropical tank State ===
class ttankstate:
    def __init__(self):
        self.bg_color = (0, 100,0)
        self.door = pygame.Rect(10, 10, 50, 50)
        self.data = {}

    def update(self):
        pass

    def draw(self):
        screen.fill(self.bg_color)
        pygame.draw.rect(screen, BLACK, self.door)
        
        
# === freshwater tank State ===
class fwtankstate:
    def __init__(self):
        self.bg_color = (0, 128,128)
        self.door = pygame.Rect(10, 10, 50, 50)
        self.data = {}

    def update(self):
        pass

    def draw(self):
        screen.fill(self.bg_color)
        pygame.draw.rect(screen, BLACK, self.door)
        
        
# === collection book State ===
class fishdexstate:
    def __init__(self):
        self.bg_color = (255, 255, 255)
        self.door = pygame.Rect(10, 10, 50, 50)
        self.data = {}

    def update(self):
        pass

    def draw(self):
        screen.fill(self.bg_color)
        pygame.draw.rect(screen, BLACK, self.door)


# Create state----------------------------------------
main = MainState()
tutorial = HouseState()
tropical = ttankstate()
fresh = fwtankstate()
fishcaught = fishdexstate()
current_state = main 

# Game loop ------------------------------------------------------
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            
            if current_state == main and main.door.collidepoint(mx, my):
                current_state = tutorial
            elif current_state == tutorial and tutorial.door.collidepoint(mx, my):
                current_state = main
                
            if current_state == main and main.doort.collidepoint(mx, my):
                current_state = tropical
            elif current_state == tropical and tropical.door.collidepoint(mx, my):
                current_state = main
                
            if current_state == main and main.doorfw.collidepoint(mx, my):
                current_state = fresh
            elif current_state == fresh and fresh.door.collidepoint(mx, my):
                current_state = main
                
            if current_state == main and main.doorfc.collidepoint(mx, my):
                current_state = fishcaught
            elif current_state == fishcaught and fishcaught.door.collidepoint(mx, my):
                current_state = main

    current_state.update()
    current_state.draw()
    pygame.display.flip()
    
    

pygame.quit()
