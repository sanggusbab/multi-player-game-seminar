# game_objects/rectangle.py

from config import screen_width, screen_height

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        # 화면 밖으로 나가지 않도록 위치 조절
        if new_x < 0:
            new_x = 0
        elif new_x > screen_width - self.width:
            new_x = screen_width - self.width

        if new_y < 0:
            new_y = 0
        elif new_y > screen_height - self.height:
            new_y = screen_height - self.height

        self.x = new_x
        self.y = new_y
