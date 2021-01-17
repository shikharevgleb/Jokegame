import pygame as pg
class window:
    height = 480
    width = 640
    
screen = pg.display.set_mode(Window.width, Window.height)

class Button(self):
    def __init__(self):
        pass
    def draw(self):
        pass
    def is_click(self):
        pass
    def do (self):
        pass
    def set_text(self):
        pass
    def set_color(self):
        pass
    def set_text(self):
        pass
    
    
    
    
    
    
fps = 60

running = True
while running:
    clock.tick(FPS)
    screen.fill(colors.BLUE)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False