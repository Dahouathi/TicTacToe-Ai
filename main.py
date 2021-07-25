import pyglet
from pyglet.graphics import vertex_list
from pyglet.libs.x11.xlib import None_
from pyglet.text import Label

number_of_X = 3
width=480
height=480
W=height/number_of_X

class Player():
    def __init__(self,state) :
        self.state = state #can be an X or E
        self.i =None
        self.j =None
        self.clicking=False
    
    def draw_action(self):
        i=self.i
        j=self.j

        if  self.clicking:
            if self.state == 'x':
                batch=pyglet.graphics.Batch()
                line1=pyglet.shapes.Line(W*i,W*j,W*(i+1),W*(j+1),color=(255,0,0),batch=batch)
                line2=pyglet.shapes.Line(W*i,W*(j+1),W*(i+1),W*j,color=(255,0,0),batch=batch)
                batch.draw()
                
            else: pass


class Window (pyglet.window.Window):
    def __init__(self):
        super(Window, self).__init__()
        self.batch =  pyglet.graphics.Batch()
        print(self.height)
        title='Tic Tac Toe'
        self.set_size(width, height)
        self.set_caption(title)
        self.current_player=Player('x')
    def draw_lines(self):
        batch=self.batch
        W=height/number_of_X
        for i in range(number_of_X+1):
            line1=pyglet.shapes.Line(W*i,0,W*i,height, 5, color=(50,40,30), batch=batch)
            line2=pyglet.shapes.Line(0,W*i,width,W*i, 5, color=(50,40,30), batch=batch)
            self.batch.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        pass
    def on_mouse_press(self, x, y, button, modifiers):
        print(x/width,y/height)
        self.current_player.clicking = True
        self.current_player.i=0
        self.current_player.j=0

    
    def on_draw(self):
        
        self.clear()
        self.draw_lines()
        self.current_player.draw_action()
        
if __name__ == '__main__':
    window = Window()
    pyglet.app.run()


