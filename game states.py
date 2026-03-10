import pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("State Machine Demo")

BLACK = (0, 0, 0)

# === Main Map State ===
class MainState:
    def __init__(self):
        self.bg_color = (200, 200, 255)
        self.door = pygame.Rect(550, 180, 50, 50)
        self.data = {} 

    def update(self):
        pass

    def draw(self):
        screen.fill(self.bg_color)
        pygame.draw.rect(screen, BLACK, self.door)


# === House Map State ===
class HouseState:
    def __init__(self):
        self.bg_color = (200, 255, 200)
        self.door = pygame.Rect(10, 180, 50, 50)
        self.data = {}

    def update(self):
        pass

    def draw(self):
        screen.fill(self.bg_color)
        pygame.draw.rect(screen, BLACK, self.door)


# Create state----------------------------------------
main = MainState()
house = HouseState()
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
                current_state = house
            elif current_state == house and house.door.collidepoint(mx, my):
                current_state = main

    current_state.update()
    current_state.draw()
    pygame.display.flip()

pygame.quit()
