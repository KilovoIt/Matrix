import numpy as np
import pygame as pg


class Matrix:
    def __init__(self, app):
        pass

class MatrixVision:
    def __init__(self):
        self.RES = self.WIDTH, self.HEIGHT = 1400, 800
        pg.init()
        self.screen = pg.display.set_mode(self.RES)
        self.surface = pg.Surface(self.RES)
        self.clock = pg.time.Clock()
        self.matrix = Matrix(self)

    def draw(self):
        self.surface.fill(pg.Color('black'))
        self.screen.blit(self.surface, (0,0))

    def run(self):
        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.flip()
            self.clock.tick(30)


if __name__ == '__main__':
    app = MatrixVision()
    app.run()



