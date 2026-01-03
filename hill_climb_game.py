import pygame
import sys
import math

# ---------- INITIAL SETUP ----------
pygame.init()
WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Hill Climb Game")

clock = pygame.time.Clock()

# ---------- COLORS ----------
WHITE = (255, 255, 255)
GREEN = (50, 200, 50)
BLACK = (0, 0, 0)
BLUE = (50, 100, 255)

# ---------- CAR ----------
car_width = 60
car_height = 30
car_x = 200
car_y = 200
car_speed = 1
gravity = 0.5
velocity_y = 0

# ---------- HILL FUNCTION ----------
def get_ground_y(x):
    return 350 + 40 * math.sin(x * 0.01)

# ---------- MAIN LOOP ----------
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---------- KEYS ----------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        car_speed += 0.22
    elif keys[pygame.K_LEFT]:
        car_speed -= 0.22
    else:
        car_speed *= 0.95

    car_x += car_speed

    # ---------- GRAVITY ----------
    velocity_y += gravity
    car_y += velocity_y

    ground_y = get_ground_y(car_x)

    if car_y + car_height >= ground_y:
        car_y = ground_y - car_height
        velocity_y = 0

    # ---------- DRAW HILLS ----------
    for x in range(0, WIDTH, 5):
        y = get_ground_y(x + car_x - 200)
        pygame.draw.circle(screen, GREEN, (x, int(y)), 5)

    # ---------- DRAW CAR ----------
    pygame.draw.rect(screen, BLUE, (200, car_y, car_width, car_height))
    pygame.draw.circle(screen, BLACK, (215, car_y + car_height), 10)
    pygame.draw.circle(screen, BLACK, (245, car_y + car_height), 10)

    # ---------- TEXT ----------
    font = pygame.font.SysFont(None, 30)
    text = font.render("Use LEFT and RIGHT arrow keys", True, BLACK)
    screen.blit(text, (20, 20))

    pygame.display.update()

pygame.quit()
sys.exit()
