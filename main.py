import numpy as np
import pygame as pg


class Matrix:
    def __init__(self, app, font_size=40):
        self.app = app
        self.FONT_SIZE = font_size
        self.SIZE = self.ROWS, self.COLS = app.HEIGHT // font_size, app.WIDTH // font_size
        self.katakana = np.array([chr(int('0x30a0', 16) + i) for i in range(96)])
        self.font = pg.font.SysFont('ms mincho', font_size, bold=True)

        self.matrix = np.random.choice(self.katakana, self.SIZE)


    def run(self):
        self.draw()

    def draw(self):
        for y, row in enumerate(self.matrix):
            for x, char in enumerate(row):
                pos = x * self.FONT_SIZE, y * self.FONT_SIZE
                char = self.font.render(char, False, (0, 170, 0))
                self.app.surface.blit(char, pos)


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
        self.matrix.run()
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



