import pygame as pg
from sudoku import Board
from typing import Any



class Window:

    flags:dict[str,Any] = {
        "bg_color":(200,200,200),
        "board_color":(170,170,170),
        "line_color":(100,100,100),
        "border_size": 10,
        "line_width": 1,
        "bigline_width":4,
        "default_size":(400,500),
    }

    def __init__(self,board:Board|None=None) -> None:
        
        self.board:Board = board if not board is None else Board()
        self.init_pg()

    def init_pg(self):

        pg.init()
        pg.font.init()
        self.font = pg.font.Font('freesansbold.ttf',32)
        self.screen = pg.display.set_mode(self.flags["default_size"],pg.RESIZABLE|pg.DOUBLEBUF)
        pg.display.set_caption("Sudoku")
    
    def frame(self):
        '''run each frame to handle rendering and interaction,
        returns false if process should stop'''

        self.screen.fill(self.flags["bg_color"])

        self.draw_grid()
        self.draw_digits()
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
        else: return True

    def draw_grid(self):
        '''draws the sodoku grid at the top of the screen'''

        # make board:
        b = self.flags["border_size"]
        w = self.screen.get_rect().width
        rect = pg.Rect(b,b,w-2*b,w-2*b)
        r = int(b/2)
        c = rect.width/9 # cell size
        pg.draw.rect(self.screen,self.flags["board_color"],rect,border_radius=r)
        self.rect = rect; '''rect of the board'''

        # draw gridlines:
        for i in range(1,9):
            # rows:
            start = (rect.topleft[0],rect.topleft[1] +c*i)
            end = (rect.topright[0],rect.topright[1] +c*i)
            width = self.flags["line_width"] if  i%3 else self.flags["bigline_width"]
            pg.draw.line(self.screen,self.flags["line_color"],start, end,width)

            # cols:
            start = (rect.topleft[0] +c*i,rect.topleft[1])
            end = (rect.bottomleft[0]+c*i,rect.bottomleft[1] )
            pg.draw.line(self.screen,self.flags["line_color"],start, end,width)

    def draw_digits(self):

        
        txt = self.font.render("TEST 0123",True, self.flags["line_color"], "white")
        txt.get_rect().center = (200,200)


    def __del__(self):
        pg.font.quit()
        pg.quit()







def main():
    win = Window()
    while win.frame():pass


if __name__ == "__main__":
    main()