import pygame
from game_objects import Rectangle
from config import screen_width, screen_height, white, black, lowering_rate, speed, rect_color
from input_handler import handle_input
from utils import print_position

rectangle = Rectangle(100, 100, 50, 50)

# Pygame 초기화
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rectangle Moving")

# 게임 루프
running = True
counter = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if counter % lowering_rate == 0:
        handle_input(rectangle)
    if counter % (lowering_rate*5) == 0:
        print_position(rectangle)
    counter += 1
    screen.fill(white)
    pygame.draw.rect(screen, rect_color, (rectangle.x, rectangle.y, rectangle.width, rectangle.height))
    pygame.display.flip()

# Pygame 종료
pygame.quit()