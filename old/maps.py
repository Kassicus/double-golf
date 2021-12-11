import pygame
import ball
import color

class Club():
    def __init__(self, _primary, _secondary):
        self.primary_ball = _primary
        self.secondary_ball = _secondary

        self.dampener = 50

        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

        self.x_offset = self.mouse_x - self.primary_ball.x
        self.y_offset = self.mouse_y - self.primary_ball.y

    def draw(self, surface):
        pygame.draw.line(surface, color.red, (self.primary_ball.x, self.primary_ball.y), (self.mouse_x, self.mouse_y), 3)

        pygame.draw.line(surface, color.blue, (self.primary_ball.x, self.primary_ball.y), (self.primary_ball.x - self.x_offset, self.primary_ball.y - self.y_offset), 3)

    def update(self, events):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

        self.x_offset = self.mouse_x - self.primary_ball.x
        self.y_offset = self.mouse_y - self.primary_ball.y

        change_x_velocity = (-self.x_offset / self.dampener)
        change_y_velocity = (-self.y_offset / self.dampener)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.primary_ball.x_velocity = change_x_velocity
                self.primary_ball.y_velocity = change_y_velocity

                self.secondary_ball.x_velocity = change_x_velocity
                self.secondary_ball.y_velocity = change_y_velocity

class Map():
    def __init__(self, _x, _y, _width, _height, _color, _ball_x, _ball_y): # _obstacles, _hole
        self.x = _x
        self.y = _y

        self.width = _width
        self.height = _height

        self.color = _color

        self.ball = ball.Ball(self.x + _ball_x, self.y + _ball_y)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

        self.ball.draw(surface)

    def update(self):
        self.ball.update(self)
