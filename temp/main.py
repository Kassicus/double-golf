import pygame

pygame.init()

black = pygame.Color(0, 0, 0, 255)
white = pygame.Color(255, 255, 255, 255)
red = pygame.Color(255, 0, 0, 255)
blue = pygame.Color(0, 0, 255, 255)
light_green = pygame.Color(21, 99, 20)
dark_green = pygame.Color(0, 56, 13, 255)

class Map():
    def __init__(self, _x, _y, _width, _height, _color):
        self.x = _x
        self.y = _y

        self.width = _width
        self.height = _height

        self.color = _color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

class Ball():
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

        self.x_vel = 0
        self.y_vel = 0

        self.friction = 0.0002

        self.radius = 15

    def draw(self, surface):
        pygame.draw.circle(surface, white, (self.x, self.y), self.radius)

    def update(self, parent):
        self.x_vel = self.x_vel * self.friction
        self.y_vel = self.y_vel * self.friction

        self.x += self.x_vel
        self.y += self.y_vel



class Game():
    def __init__(self, _width, _height, _title):
        self.width = _width
        self.height = _height
        
        self.title = _title

        self.screen = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption(self.title)

        self.running = True

        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()

        self.map_left = Map(0, 0, 600, 900, light_green)
        self.map_right = Map(600, 0, 600, 900, dark_green)

    def start(self):
        while self.running:
            self.events = pygame.event.get()

            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()

            self.update()

    def draw(self):
        self.screen.fill(black)

        self.map_left.draw(self.screen)
        self.map_right.draw(self.screen)

    def update(self):
        pygame.display.update()
        self.clock.tick(60)

game = Game(1200, 900, "Double Golf")
game.start()

pygame.quit()