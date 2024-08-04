from mdesign import screen_height, screen_width
import pygame
import random

white = (255,255,255)

class Paddle:
    def __init__(self, side, color = white):
        self.initial_pos = 50
        self.width, self.height = 10, 100
        self.speed = 10
        self.color = color
        self.side = side.lower()
        if self.side == 'left':
            self.x, self.y = self.initial_pos, (screen_height // 2) - (self.height // 2)
        elif self.side == 'right':
            self.x, self.y = screen_width - self.initial_pos - self.width, (screen_height // 2) - (self.height // 2)

class Ball:
    def __init__(self, color = white, size = 15):
        self.size = size
        self.speed_x, self.speed_y = 2, random.uniform(-7,7)
        self.color = color
        self.x, self.y = screen_width // 2, screen_height // 2

class Screen:
    def __init__(self):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.display = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Arjan's Pong Game")