import pygame
from config import screen_width, screen_height, move_speed, bg_w, bg_h, change_interval
from .images import load_character_images
from .utils import handle_input

def run_game():
    pygame.init()

    background = pygame.image.load('src/AmongHSMap_final.png')
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Among HandS")

    cutout_rect = pygame.Rect(3500, 1000, screen_width, screen_height)
    cutout = background.subsurface(cutout_rect)

    keys = {
        pygame.K_LEFT: False,
        pygame.K_RIGHT: False,
        pygame.K_UP: False,
        pygame.K_DOWN: False
    }

    last_change_time = pygame.time.get_ticks()
    image_index = 0
    character_images = load_character_images()
    character_size = (80, 60)
    
    running = True
    while running:
        running, image_index = handle_input(keys, cutout_rect, move_speed, bg_w, bg_h, last_change_time, image_index, change_interval)

        # 이미지 잘라내기
        cutout = background.subsurface(cutout_rect)

        # 캐릭터 위치 계산
        # width 1000 character width 100-> character.x? 1000/2 - 100/2 =450
        character_x = (screen_width - character_size[0]) // 2
        character_y = (screen_height - character_size[1]) // 2

        # 화면 업데이트
        screen.blit(cutout, (0, 0))
        screen.blit(character_images[image_index], (character_x, character_y))
        pygame.display.update()

    pygame.quit()
