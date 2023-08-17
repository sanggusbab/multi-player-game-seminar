import pygame

counter = 0
def handle_input(keys, cutout_rect, move_speed, bg_w, bg_h, last_change_time, image_index, change_interval):
    global counter
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, image_index

        if event.type == pygame.KEYDOWN:
            if event.key in keys:
                keys[event.key] = True
        elif event.type == pygame.KEYUP:
            if event.key in keys:
                keys[event.key] = False
    
    current_time = pygame.time.get_ticks()
    # 이미지 변경 로직
    if current_time - last_change_time >= change_interval:
        dx, dy = 0, 0

        # Check horizontal movement
        if keys[pygame.K_LEFT] and cutout_rect.left > move_speed:
            dx -= move_speed
        if keys[pygame.K_RIGHT] and cutout_rect.right < bg_w - move_speed:
            dx += move_speed

        # Check vertical movement
        if keys[pygame.K_UP] and cutout_rect.top > move_speed:
            dy -= move_speed
        if keys[pygame.K_DOWN] and cutout_rect.bottom < bg_h - move_speed:
            dy += move_speed
        if dx != 0 or dy != 0:
            cutout_rect.move_ip(dx, dy)
            last_change_time = current_time
            # 0.2초마다 5px씩 움직인다.
            # 0.6초마다 image_index를 변화시킨다.
        if counter % 3 == 0:
            if dx != 0 or dy != 0:
                # 이미지 변경을 기존의 순서대로 처리
                if dx < 0:
                    image_index = (image_index + 1) % 4
                elif dx > 0:
                    image_index = (image_index + 1) % 4 +4
                else:
                    if dy <0:
                        image_index = (image_index + 1) % 4
                    elif dy>0:
                        image_index = (image_index + 1) % 4 +4
        counter += 1

    return True, image_index
