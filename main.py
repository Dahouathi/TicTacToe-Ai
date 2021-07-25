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
def permute(n):
    if n==1 :return 2
    if n==2 : return 1
class Player():
    """ class player contain the type of the player"""
    def __init__(self,state) :
        self.state = state #can be an X or O
        self.wins = False
    
        
    def draw_action(self,i,j,matrix):
        i,j=j,i # permutation cos the pyglet orientation is reversed 
        
        if self.state == 'X':
            matrix[j,i]=1
            
            
        else:
            #cercle=pyglet.shapes.Circle(W*(i+1/2),W*(size-j-1/2),W/2,color=(255,0,60),batch=batch)
            matrix[j,i]=2
        # batch.draw()
        # print(matrix)
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
                                self.wins=True
                                exit = True
                            else : count=0
                        if size-i >=3:
                        
                            for k in range(size-i):
                                if matrix[i+k,j]==n : 
                                    count+=1
                                if count ==3 : break
                            if count ==3:
                                print('{} player Wins '.format(self.state))
                                self.wins=True
                                exit = True
                            else : count=0
                        if size-j >=3:
                            for k in range(size-j):
                                if matrix[i,k+j]==n : 
                                    count+=1
                                if count ==3 : break
                            if count ==3:
                                print('{} player Wins '.format(self.state))
                                self.wins=True
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
                                self.wins=True
                                exit = True
                            else : count=0
                        if size-i >=4:
                        
                            for k in range(size-i):
                                if matrix[i+k,j]==n : 
                                    count+=1
                                if count ==4 : break
                            if count ==4:
                                print('{} player Wins '.format(self.state))
                                self.wins=True
                                exit = True
                            else : count=0
                        if size-j >=4:
                            for k in range(size-j):
                                if matrix[i,k+j]==n : 
                                    count+=1
                                if count ==4 : break
                            if count ==4:
                                print('{} player Wins '.format(self.state))
                                self.wins=True
                                exit = True
                            else : count=0
        if exit==True : return True
        # print('next tour')
        return False

class RandomPlayer(Player):
    def __init__(self, state):
        super().__init__(state)
        self.type='random'

    def choose_move(self,matrix):
        Game_over=False
        
        list_moves=[]
        for i in range(size):
            for j in range(size):
                if matrix[i,j]==0 : list_moves.append((i,j))
        # print('list_moves')
        # print(list_moves)
        if(len(list_moves)!=0):
            i,j=choice(list_moves)
            return i,j,Game_over
        Game_over=True
        # print('its tie')
        return (-1,-1 ,Game_over) #when it's tie       

class HumanPlayer(Player):
    def __init__(self, state):
        super().__init__(state)
        self.type='human'
        self.i=-1
        self.j=-1
        
    def choose_move(self,matrix):
        Game_over=False
        i=self.i
        j=self.j
        if self.state=='X':
            n=1
        else : n=2
        if matrix[i,j]==n:
            # print('this spot is already filled')
            i=-1
            j=-1
        elif matrix[i,j]==permute(n):
            print('u blind ?')
            i=-1
            j=-1
        return i,j,Game_over
        
class Window (pyglet.window.Window):
    def __init__(self, X_player, O_player):
        super(Window, self).__init__(width, height, 'Tic Tac Toe')
        self.batch =  pyglet.graphics.Batch()
        self.matrix= np.zeros((size,size)) # represent the Grid initialized to 0 
                                            # X==>1 O ==>2
        
        self.current_player=X_player #first player is the X player
        self.Game_over = False
        self.dt=1.0
    def draw_Grid(self):
        batch=self.batch
        W=height/size
        for i in range(size+1):
            line1=pyglet.shapes.Line(W*i,0,W*i,height, 5, color=(50,40,30), batch=self.batch)
            line2=pyglet.shapes.Line(0,W*i,width,W*i, 5, color=(50,40,30), batch=self.batch)
            self.batch.draw()

    def draw_current_state(self):
        
        for i in range(size):
            for j in range(size):
                if self.matrix[i,j]==1 :
                    i,j=j,i
                    line1=pyglet.shapes.Line(W*(i),W*(size-j),W*(i+1),W*(size-j-1),color=(255,0,0),batch=self.batch)
                    #line1=pyglet.shapes.Line(W*(size-j),W*(i),W*(size-j-1),W*(i+1),color=(255,0,0),batch=batch)
                    line2=pyglet.shapes.Line(W*(i),W*(size-j-1),W*(i+1),W*(size-j),color=(255,0,0),batch=self.batch)
                    #line2=pyglet.shapes.Line(W*(size-j-1),W*(i),W*(size-j),W*(i+1),color=(255,0,0),batch=batch)
                    i,j=j,i
                    self.batch.draw()
                if self.matrix[i,j]==2:
                    i,j=j,i
                    cercle=pyglet.shapes.Arc(W*(i+1/2),W*(size-j-1/2),W/2.1,angle=2*pi,start_angle=0,closed=True,color=(0,0,255),batch=self.batch)
                    i,j=j,i
                    self.batch.draw()
    def on_mouse_motion(self, x, y, dx, dy):
        pass
    def on_mouse_press(self, x, y, button, modifiers):
        print(x/width,y/height)
        if self.current_player.type =='human':
            i=int(x/W)
            j=int(y/W)
            self.current_player.i=size-1-j
            self.current_player.j=i
            print(self.current_player.i,self.current_player.j)
            # self.current_player.draw_action(i,j,self.matrix)
        
    
    
    def on_draw(self):
        
        self.clear()
        pyglet.clock.tick()
        self.draw_Grid()
        #self.current_player.draw_action(0,2,self.matrix)
        #self.current_player.check_win(self.matrix,self.Game_over)
        self.draw_current_state()
        if not self.Game_over:
            self.dt+=0.2
        pyglet.clock.schedule_interval_soft(self.update,self.dt) #funny cos there is multiple function i tried all of them and this worked just fine
        
        # self.batch.draw()
    
    def update(self, dt) :
        if self.Game_over==False :
            i,j,self.Game_over=self.current_player.choose_move(self.matrix)
            if(i!=-1 and j!=-1):
                
                # print('win bch norsom')
                # print(i,j)
                self.current_player.draw_action(i,j,self.matrix)
                self.Game_over=self.current_player.check_win(self.matrix)
                if(self.current_player.state=='X'):
                    self.current_player=O_player
                else : self.current_player=X_player
        
    def check_tie(self):
        if(not X_player.wins and not O_player.wins) : print("it'z a tie")
            
    
        
            
        
if __name__ == '__main__':
    X_player=HumanPlayer('X')
    O_player=RandomPlayer('O')
    window = Window(X_player, O_player)
    pyglet.app.run()


