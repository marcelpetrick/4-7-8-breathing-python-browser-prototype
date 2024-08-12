import asyncio
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Breathwork Exercise")

# Define constants
background_color = (0, 0, 0)
circle_color = (0, 0, 255)  # Blue color
screen_width, screen_height = screen.get_size()
center_x, center_y = screen_width // 2, screen_height // 2
radius_min = 50
radius_max = 200

async def breathwork():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Breathing in (4 seconds)
        for t in range(120):  # 120 frames at 30 FPS = 4 seconds
            radius = radius_min + (radius_max - radius_min) * (t / 120)
            draw_circle(radius)
            await asyncio.sleep(0)

        # Hold breath (7 seconds)
        for t in range(210):  # 210 frames at 30 FPS = 7 seconds
            variation = math.sin(t / 30 * math.pi) * 5  # slight variation
            radius = radius_max + variation
            draw_circle(radius)
            await asyncio.sleep(0)

        # Breathing out (8 seconds)
        for t in range(240):  # 240 frames at 30 FPS = 8 seconds
            radius = radius_max - (radius_max - radius_min) * (t / 240)
            draw_circle(radius)
            await asyncio.sleep(0)

    pygame.quit()

def draw_circle(radius):
    screen.fill(background_color)
    pygame.draw.circle(screen, circle_color, (center_x, center_y), int(radius))
    pygame.display.flip()

asyncio.run(breathwork())
