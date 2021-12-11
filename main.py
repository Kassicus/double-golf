import pygame
import color
import objects

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

        self.left_map = objects.Map(0, 0, 600, 900, color.light_green, 300, 600)
        self.right_map = objects.Map(600, 0, 600, 900, color.dark_green, 300, 600)

        self.indicator_ball = objects.IndicatorBall(self.left_map.ball, self.right_map.ball)

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

        self.left_map.draw(self.screen)
        self.right_map.draw(self.screen)

        self.indicator_ball.draw(self.screen)
    
    def update(self):
        self.indicator_ball.update(self.events)

        self.left_map.update()
        self.right_map.update()

        pygame.display.update()
        self.clock.tick(60)

game = Game(1200, 900, "Double Golf")
game.start()

pygame.quit()