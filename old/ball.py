import pygame
import color

class Ball():
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

        self.radius = 15

        self.x_velocity = 5
        self.y_velocity = 5

        self.friction = .2

        self.x_offset = 0
        self.y_offset = 0

    def draw(self, surface):
        pygame.draw.circle(surface, color.white, (self.x, self.y), self.radius)

    def update(self, parent):
        if self.x_velocity < 0:
            self.x_velocity += self.friction
        if self.x_velocity > 0:
            self.x_velocity -= self.friction
        
        if self.y_velocity < 0:
            self.y_velocity += self.friction
        if self.y_velocity > 0:
            self.y_velocity -= self.friction

        self.x += self.x_velocity
        self.y += self.y_velocity

        self.checkCollisions(parent)

    def checkCollisions(self, parent):
        if self.x - self.radius < parent.x:
            self.x_velocity = -self.x_velocity
        if self.x + self.radius > parent.x + parent.width:
            self.x_velocity = -self.x_velocity
        
        if self.y - self.radius < parent.y:
            self.y_velocity = -self.y_velocity
        if self.y + self.radius > parent.y + parent.height:
            self.y_velocity = -self.y_velocity