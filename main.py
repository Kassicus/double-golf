import pygame
import color
import objects
import maps
import random

pygame.init()

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

        self.left_course = objects.Course(0, 0, 600, 900, color.light_green, 300, 600, [maps.left_map_one])
        self.right_course = objects.Course(600, 0, 600, 900, color.dark_green, 300, 600, [maps.right_map_one])

        self.indicator_ball = objects.IndicatorBall(self.left_course.ball, self.right_course.ball)

    def start(self):
        while self.running:
            self.events = pygame.event.get()

            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()

            self.update()

    def draw(self):
        self.screen.fill(color.black)

        self.left_course.draw(self.screen)
        self.right_course.draw(self.screen)

        self.indicator_ball.draw(self.screen)
    
    def update(self):
        self.indicator_ball.update(self.events)

        self.left_course.update()
        self.right_course.update()

        pygame.display.update()
        self.clock.tick(60)

game = Game(1200, 900, "Double Golf")
game.start()

pygame.quit()
