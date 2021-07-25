import pyglet
from pyglet.graphics import vertex_list
from pyglet.libs.x11.xlib import None_
from pyglet.text import Label
import numpy as np
from math import pi
from random import choice
from pyglet.window.key import N
size = 3
width=480
height=480
W=height/size

class Player():
    """ class player contain the type of the player"""
    def __init__(self,state,type) :
        self.state = state #can be an X or O
        self.type  = type #humain_player, AI_player, random_player
       
    def choose_move(self,matrix,Game_over):
        if self.type=='random':
            list_moves=[]
            for i in range(size):
                for j in range(size):
                    if matrix[i,j]==0 : list_moves.append((i,j))
            # print('list_moves')
            # print(list_moves)
            if(len(list_moves)!=0):return choice(list_moves)
            Game_over=True
            # print('its tie')
            return -1,-1 #when it's tie

    def draw_action(self,i,j,matrix):
        i,j=j,i # permutation cos the pyglet orientation is reversed 
        batch=pyglet.graphics.Batch()
        if self.state == 'X':
            matrix[j,i]=1
            line1=pyglet.shapes.Line(W*(i),W*(size-j),W*(i+1),W*(size-j-1),color=(255,0,0),batch=batch)
            #line1=pyglet.shapes.Line(W*(size-j),W*(i),W*(size-j-1),W*(i+1),color=(255,0,0),batch=batch)
            line2=pyglet.shapes.Line(W*(i),W*(size-j-1),W*(i+1),W*(size-j),color=(255,0,0),batch=batch)
            #line2=pyglet.shapes.Line(W*(size-j-1),W*(i),W*(size-j),W*(i+1),color=(255,0,0),batch=batch)
            
            
        else:
            #cercle=pyglet.shapes.Circle(W*(i+1/2),W*(size-j-1/2),W/2,color=(255,0,60),batch=batch)
            cercle=pyglet.shapes.Arc(W*(i+1/2),W*(size-j-1/2),W/2.1,angle=2*pi,start_angle=0,closed=True,color=(0,0,255),batch=batch)
            matrix[j,i]=2
        batch.draw()
        print(matrix)
    def check_win(self,matrix):
        if self.state=='X':
            n=1
        else : n=2
        
        exit=False
        i=-1
        while(i < size-1 and exit == False):
            i+=1
            if(size==3):
                for j in range(size):
                    count=0

                    if matrix[i,j]==n:
                        # print('ani 5tart')
                        # print(i,j)
                        if size-i>=3 and size-j >=3 :
                            
                            for k in range(size-i):
                                if matrix[i+k,j+k]==n : 
                                    count+=1
                                if count ==3 : break
                            if count ==3:
                                print('{} player Wins '.format(self.state))
                                exit = True
                            else : count=0
                        if size-i >=3:
                        
                            for k in range(size-i):
                                if matrix[i+k,j]==n : 
                                    count+=1
                                if count ==3 : break
                            if count ==3:
                                print('{} player Wins '.format(self.state))
                                exit = True
                            else : count=0
                        if size-j >=3:
                            for k in range(size-j):
                                if matrix[i,k+j]==n : 
                                    count+=1
                                if count ==3 : break
                            if count ==3:
                                print('{} player Wins '.format(self.state))
                                exit = True
                            else : count=0
            else:
                for j in range(size):
                    count=0

                    if matrix[i,j]==n:
                        # print('ani 5tart')
                        # print(i,j)
                        if size-i>=4 and size-j >=4 :
                            
                            for k in range(size-i):
                                if matrix[i+k,j+k]==n : 
                                    count+=1
                                if count ==4 : break
                            if count ==4:
                                print('{} player Wins '.format(self.state))
                                exit = True
                            else : count=0
                        if size-i >=4:
                        
                            for k in range(size-i):
                                if matrix[i+k,j]==n : 
                                    count+=1
                                if count ==4 : break
                            if count ==4:
                                print('{} player Wins '.format(self.state))
                                exit = True
                            else : count=0
                        if size-j >=4:
                            for k in range(size-j):
                                if matrix[i,k+j]==n : 
                                    count+=1
                                if count ==4 : break
                            if count ==4:
                                print('{} player Wins '.format(self.state))
                                exit = True
                            else : count=0
        if exit==True : return True
        print('next tour')
        return False


                        
                        
class Window (pyglet.window.Window):
    def __init__(self, X_player, O_player):
        super(Window, self).__init__(width, height, 'Tic Tac Toe')
        self.batch =  pyglet.graphics.Batch()
        self.matrix= np.zeros((size,size)) # represent the Grid initialized to 0 
                                            # X==>1 O ==>2
        
        self.current_player=X_player #first player is the X player
        self.Game_over = False
    
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
        #self.current_player.draw_action(0,2,self.matrix)
        #self.current_player.check_win(self.matrix,self.Game_over)
        
        if self.Game_over==False :
            i,j=self.current_player.choose_move(self.matrix, self.Game_over)
            if(i!=-1 and j!=-1):
                print('win bch norsom')
                print(i,j)
                self.current_player.draw_action(i,j,self.matrix)
                self.Game_over=self.current_player.check_win(self.matrix)
            # if(self.current_player=='X'):
            #     self.current_player=O_player
            # else : self.current_player=X_player
        

        
if __name__ == '__main__':
    X_player=Player('X','random')
    O_player=Player('O','random')
    window = Window(X_player, O_player)
    pyglet.app.run()


