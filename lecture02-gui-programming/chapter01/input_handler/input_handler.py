# input_handler.py

import pygame
from config import speed

def handle_input(rectangle):
    global speed  # 전역 변수로 속도를 관리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rectangle.move(-speed, 0)
    if keys[pygame.K_RIGHT]:
        rectangle.move(speed, 0)
    if keys[pygame.K_UP]:
        rectangle.move(0, -speed)
    if keys[pygame.K_DOWN]:
        rectangle.move(0, speed)
    if keys[pygame.K_EQUALS]:  # + 키로 속도 증가
        speed += 1
    if keys[pygame.K_MINUS]:  # - 키로 속도 감소
        speed = max(1, speed - 1)  # 최소 속도는 1로 유지
