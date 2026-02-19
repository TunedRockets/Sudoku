import pygame as pg
from sudoku import Board
from typing import Any



class Window:

    flags:dict[str,Any] = {
        "bg_color":(200,200,200),
        "board_color":(170,170,170),
        "line_color":(100,100,100),
        "select_color":(150,150,230),
        "border_size": 10,
        "line_width": 1,
        "bigline_width":4,
        "default_size":(400,500),
        "digit_font":'freesansbold.ttf',
        "digit_ratio": 0.85
    }

    def __init__(self,board:Board|None=None) -> None:
        
        self.board:Board = board if not board is None else Board()
        self.selected = (5,5)
        self.init_pg()

    def init_pg(self):

        pg.init()
        pg.font.init()
        self.font = pg.font.Font(self.flags['digit_font'],32)
        self.screen = pg.display.set_mode(self.flags["default_size"],pg.RESIZABLE|pg.DOUBLEBUF)
        pg.display.set_caption("Sudoku")
    
    def frame(self):
        '''run each frame to handle rendering and interaction,
        returns false if process should stop'''

        self.screen.fill(self.flags["bg_color"])

        self.draw_grid()
        self.draw_digits()
        self.draw_selected()
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.select()
        pg.display.flip()
        return True

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

        # fix font if needed:
        c = self.rect.width/9 # cell size
        fs = int(c * self.flags['digit_ratio'])
        if fs != self.font.size('0')[1]:
            self.font = pg.font.Font(self.flags['digit_font'],fs)


        for idx, d in enumerate(self.board):
            if d == 0: continue
            x,y = divmod(idx,9)
            txt = self.font.render(str(d),True,self.flags["line_color"])
            size = txt.get_rect().size
            self.screen.blit(txt, (
                self.rect.topleft[0] + c*(x+0.5)-size[0]/2,
                self.rect.topleft[1] + c*(y+0.5)-size[1]/2,
            ))


    def select(self):
        x,y = pg.mouse.get_pos()
        x -= self.rect.topleft[0]
        y -= self.rect.topleft[1]
        c = self.rect.width/9 # cell size
        x_cell = int(x/c)
        y_cell = int(y/c)
        print(f"{x_cell=}, {y_cell=}")
        if not(x_cell <= 9 and y_cell <= 9):
            return
        self.selected = (x_cell,y_cell)

    def draw_selected(self):
        '''draw the selected square'''

        c = self.rect.width/9 # cell size
        tl = (self.rect.topleft[0] + c*self.selected[0], self.rect.topleft[1] + c*self.selected[1])
        br = (self.rect.topleft[0] + c*(self.selected[0]+1), self.rect.topleft[1] + c*(self.selected[1]+1))
        rect = pg.Rect(tl[0],tl[1],(br[0]-tl[0]),(br[1]-tl[1]))
        pg.draw.rect(self.screen,self.flags["select_color"],
                      rect,
                      self.flags["bigline_width"],
                      int(self.flags["bigline_width"]))



    def __del__(self):
        pg.font.quit()
        pg.quit()







def main():
    win = Window()
    win.board[0,2] = 5
    win.board[0,1] = 2
    win.board[3,7] = 7
    while win.frame():pass


if __name__ == "__main__":
    main()