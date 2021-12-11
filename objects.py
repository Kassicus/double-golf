import pygame
import color

class IndicatorBall():
    def __init__(self, _left_ball, _right_ball):
        self.x = 600
        self.y = 450

        self.radius = 15

        self.x_power = 0
        self.y_power = 0

        self.left_ball = _left_ball
        self.right_ball = _right_ball

        self.dampener = 10

        self.dragging = False

        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

    def draw(self, _surface):
        pygame.draw.circle(_surface, color.tranparent_black, (self.x, self.y), self.radius)

        if self.dragging:
            pygame.draw.line(_surface, color.red, (self.x, self.y), (self.mouse_x, self.mouse_y), 3)

    def update(self, _events):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

        x_offset = int(self.mouse_x - self.x)
        y_offset = int(self.mouse_y - self.y)

        self.x_power = int(-x_offset / self.dampener)
        self.y_power = int(-y_offset / self.dampener)

        for event in _events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.dragging = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.impart_velocity()
                self.dragging = False

    def impart_velocity(self):
        self.left_ball.x_vel, self.left_ball.y_vel = self.x_power, self.y_power
        self.right_ball.x_vel, self.right_ball.y_vel = self.x_power, self.y_power

class GameBall():
    def __init__(self, _x, _y, _parent):
        self.x = _x
        self.y = _y

        self.radius = 10

        self.x_vel = 0
        self.y_vel = 0

        self.friction = 0.975

        self.parent = _parent

    def draw(self, _surface):
        pygame.draw.circle(_surface, color.white, (self.x, self.y), self.radius)

    def update(self, _active_walls):
        self.x_vel = self.x_vel * self.friction
        self.y_vel = self.y_vel * self.friction

        self.x += self.x_vel
        self.y += self.y_vel

        self.checkCollisions(_active_walls)

    def checkCollisions(self, _active_walls):
        if self.x - self.radius < self.parent.x:
            self.x_vel = abs(self.x_vel)
        if self.x + self.radius > self.parent.x + self.parent.width:
            self.x_vel = -abs(self.x_vel)

        if self.y - self.radius < self.parent.y:
            self.y_vel = abs(self.y_vel)
        if self.y + self.radius > self.parent.y + self.parent.height:
            self.y_vel = -abs(self.y_vel)

        for wall in _active_walls:
            if self.y > wall.y + wall.height:
                if wall.x < self.x < wall.x + wall.width:
                    if self.y - self.radius < wall.y + wall.height:
                        self.y_vel = -self.y_vel
            elif self.y < wall.y:
                if wall.x < self.x < wall.x + wall.width:
                    if self.y + self.radius > wall.y:
                        self.y_vel = -self.y_vel

            if self.x > wall.x + wall.width:
                if wall.y < self.y < wall.y + wall.height:
                    if self.x - self.radius < wall.x + wall.width:
                        self.x_vel = -self.x_vel
            elif self.x < wall.x:
                if wall.y < self.y < wall.y + wall.height:
                    if self.x + self.radius > wall.x:
                        self.x_vel = -self.x_vel

class Hole():
    def __init__(self):
        pass

class Wall(pygame.sprite.Sprite):
    def __init__(self, _parent, _x, _y, _width, _height):
        pygame.sprite.Sprite.__init__(self)

        self.parent = _parent

        self.x = _x + self.parent.x_offset
        self.y = _y + self.parent.y_offset

        self.width = _width
        self.height = _height

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color.purple_gray)

        self.rect = (self.x, self.y)

        self.parent.walls.add(self)

    def update(self):
        self.rect = (self.x, self.y)

class Map():
    def __init__(self, _x_offset, _y_offset):
        self.walls = pygame.sprite.Group()
        self.holes = pygame.sprite.Group()

        self.x_offset = _x_offset
        self.y_offset = _y_offset

    def draw(self, _surface):
        self.walls.draw(_surface)

    def update(self):
        self.walls.update()

class Course():
    def __init__(self, _x, _y, _width, _height, _color, _ball_x, _ball_y, _maps=[]):
        self.x = _x
        self.y = _y

        self.width = _width
        self.height = _height

        self.color = _color

        self.ball = GameBall(self.x + _ball_x, self.y + _ball_y, self)

        self.maps = _maps
        self.active_map = self.maps[0]

    def draw(self, _surface):
        pygame.draw.rect(_surface, self.color, (self.x, self.y, self.width, self.height))
        
        self.ball.draw(_surface)
        self.active_map.draw(_surface)

    def update(self):
        self.ball.update(self.active_map.walls)
        self.active_map.update()