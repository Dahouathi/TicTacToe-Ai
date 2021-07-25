import pyglet
from pyglet.graphics import vertex_list
from pyglet.libs.x11.xlib import None_
from pyglet.text import Label
import numpy as np
from math import pi
size = 3
width=480
height=480
W=height/size

class Player():
    """ class player contain the type of the player"""
    def __init__(self,state,type) :
        self.state = state #can be an X or O
        self.type  = type #humain_player, AI_player, random_player
       
    
    def draw_action(self,i,j):
        i,j=j,i # permutation cos the pyglet orientation is reversed 
        batch=pyglet.graphics.Batch()
        if self.state == 'X':
            
            line1=pyglet.shapes.Line(W*(i),W*(size-j),W*(i+1),W*(size-j-1),color=(255,0,0),batch=batch)
            #line1=pyglet.shapes.Line(W*(size-j),W*(i),W*(size-j-1),W*(i+1),color=(255,0,0),batch=batch)
            line2=pyglet.shapes.Line(W*(i),W*(size-j-1),W*(i+1),W*(size-j),color=(255,0,0),batch=batch)
            #line2=pyglet.shapes.Line(W*(size-j-1),W*(i),W*(size-j),W*(i+1),color=(255,0,0),batch=batch)
            
            
        else:
            #cercle=pyglet.shapes.Circle(W*(i+1/2),W*(size-j-1/2),W/2,color=(255,0,60),batch=batch)
            cercle=pyglet.shapes.Arc(W*(i+1/2),W*(size-j-1/2),W/2.1,angle=2*pi,start_angle=0,closed=True,color=(0,0,255),batch=batch)
        batch.draw()
    
    def check_win(self,matrix):
        pass

class Window (pyglet.window.Window):
    def __init__(self, X_player, O_player):
        super(Window, self).__init__(width, height, 'Tic Tac Toe')
        self.batch =  pyglet.graphics.Batch()
        self.matrix= np.zeros((size,size)) # represent the Grid initialized to 0 
                                            # X==>1 O ==>2
        self.matrix[2,0]=1
        print(self.matrix)
        self.current_player=O_player #first player is the X player

    
    def draw_Grid(self):
        batch=self.batch
        W=height/size
        for i in range(size+1):
            line1=pyglet.shapes.Line(W*i,0,W*i,height, 5, color=(50,40,30), batch=batch)
            line2=pyglet.shapes.Line(0,W*i,width,W*i, 5, color=(50,40,30), batch=batch)
            self.batch.draw()

   
    def on_mouse_motion(self, x, y, dx, dy):
        pass
    def on_mouse_press(self, x, y, button, modifiers):
        print(x/width,y/height)
        

    
    def on_draw(self):
        self.clear()
        self.draw_Grid()
        self.current_player.draw_action(0,2)

        
if __name__ == '__main__':
    X_player=Player('X','random')
    O_player=Player('O','random')
    window = Window(X_player, O_player)
    pyglet.app.run()


