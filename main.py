import pyglet
from pyglet.graphics import vertex_list
from pyglet.libs.x11.xlib import None_
from pyglet.text import Label
import numpy as np
from math import pi
from random import choice
import sqlite3 as sq
size = 3
width=480
height=480
W=height/size
def permute(n):
    if n==1 :return 2
    if n==2 : return 1
np.random.seed(42)
A=np.random.rand(size,size)  
table=dict()
def id(matrix):
    return np.trace(np.dot(A,matrix))


con= sq.connect('scores.db')
cur= con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Scores
                (Id INT PRIMARY KEY , Score INT) """)


def add_(id,score):
    cur.execute("REPLACE INTO Scores VALUES ({},{})".format(id,score))
    con.commit()
def check_(id):
    cur.execute("select score from Scores where Id='{}'".format(id))
    l=cur.fetchone()
    if l!=None : return l[0]
    else : return None

add_(0,100)
print(check_(0))
# cur.execute("SELECT * FROM Scores")



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
                        if i>=2 and size-j>=2:
                            for k in range(min(size-j,3)):
                                if matrix[i-k,j+k]==n:
                                    count+=1
                            if count ==3:
                                # print('{} player Wins '.format(self.state))
                                self.wins=True
                                exit = True
                            else : count=0
                        if size-i>=2 and size-j >=2 :
                            
                            for k in range(min(size-j,min(size-i,3))):
                                if matrix[i+k,j+k]==n : 
                                    count+=1
                                if count ==3 : break
                            if count ==3:
                                # print('{} player Wins '.format(self.state))
                                self.wins=True
                                exit = True
                            else : count=0
                        if size-i >=2:
                        
                            for k in range(min(size-i,3)):
                                if matrix[i+k,j]==n : 
                                    count+=1
                                if count ==3 : break
                            if count ==3:
                                # print('{} player Wins '.format(self.state))
                                self.wins=True
                                exit = True
                            else : count=0
                        if size-j >=2:
                            for k in range(min(size-j,3)):
                                if matrix[i,k+j]==n : 
                                    count+=1
                                if count ==3 : break
                            if count ==3:
                                # print('{} player Wins '.format(self.state))
                                self.wins=True
                                exit = True
                            else : count=0
            else:
                for j in range(size):
                    count=0

                    if matrix[i,j]==n:
                        # print('ani 5tart')
                        # print(i,j)
                        if i>=3 and size-j>=3:
                            for k in range(min(size-j,4)):
                                if matrix[i-k,j+k]==n:
                                    count+=1
                            if count ==4:
                                # print('{} player Wins '.format(self.state))
                                self.wins=True
                                exit = True
                            else : count=0
                        if size-i>=3 and size-j >=3 :
                            
                            for k in range(min(size-j,min(size-i,4))):
                                if matrix[i+k,j+k]==n : 
                                    count+=1
                                if count ==4 : break
                            if count ==4:
                                # print('{} player Wins '.format(self.state))
                                self.wins=True
                                exit = True
                            else : count=0
                        if size-i >=3:
                        
                            for k in range(min(size-i,4)):
                                if matrix[i+k,j]==n : 
                                    count+=1
                                if count ==4 : break
                            if count ==4:
                                # print('{} player Wins '.format(self.state))
                                self.wins=True
                                exit = True
                            else : count=0
                        if size-j >=3:
                            for k in range(min(size-j,4)):
                                if matrix[i,k+j]==n : 
                                    count+=1
                                if count ==4 : break
                            if count ==4:
                                # print('{} player Wins '.format(self.state))
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
class AIPlayer(Player):
    def __init__(self, state):
        super().__init__(state) 
        self.type='AI'      
    def mini_max(self, matrix, depth=0, maximizer=True):#by default the maximizer is True bc it's the frist player
        # ide=id(matrix)
        # print(depth,matrix)
        # print()
        x,y=np.where(matrix==0)
        if self.state=='X': n=1
        else : n=2
        p=permute(n) #n is maximizer player nd p is minimizer 
        score=evaluate(matrix) #return +10 if x wins -10 if 0 wins 0 if tie nd -1 if game still on
        # print(depth , matrix)
        if score!=-1: 
            if n==1:
                return score
            else : return -score
        else:
            if maximizer:
                score=-10000
                
                for i in range(len(x)):
                    
                        
                    matrix[x[i],y[i]]=n 
                    value=self.mini_max(matrix,depth+1,False)
                    score=max(score,value)
                    # if score==value:
                    #     k=i
                    #     l=j
                    matrix[x[i],y[i]]=0
                return score
            else :
                score=10000
                
                for i in range(len(x)):
                    
                        
                    matrix[x[i],y[i]]=p 
                    value=self.mini_max(matrix,depth+1,True)
                    score=min(score,value)
                    # if score==value :
                    #     k=i
                    #     l=j
                    matrix[x[i],y[i]]=0
                return score

    def alpha_beta(self, matrix, depth=0, maximizer=True,alpha=-10000,beta=10000):#by default the maximizer is True bc it's the frist player
        idmatrix=id(matrix)
        print(len(table))
        if idmatrix in table.keys() :
            return table[idmatrix]
        else:
            # print(depth,matrix)
            # print()
            x,y=np.where(matrix==0)
            if self.state=='X': n=1
            else : n=2
            p=permute(n) #n is maximizer player nd p is minimizer 
            score=evaluate(matrix) #return +10 if x wins -10 if 0 wins 0 if tie nd -1 if game still on
            # print(depth , matrix)
            if score!=-1: 
                if n==1:
                    table[idmatrix]=score
                    return score
                else : 
                    table[idmatrix]=-score
                    return -score
            else:
                if maximizer:
                    score=-10000
                    
                    for i in range(len(x)):
                        
                            
                        matrix[x[i],y[i]]=n 
                        value=self.alpha_beta(matrix,depth+1,False,alpha,beta)
                        score=max(score,value)-depth
                        matrix[x[i],y[i]]=0
                        if score>=beta:
                            table[idmatrix]=score
                            return score
                        alpha=max(alpha,score)
                        # if score==value:
                        #     k=i
                        #     l=j
                    table[idmatrix]=score 
                    return score
                else :
                    score=10000
                    
                    for i in range(len(x)):
                        
                            
                        matrix[x[i],y[i]]=p 
                        value=self.alpha_beta(matrix,depth+1,True,alpha,beta)
                        score=min(score,value)+depth
                        # if score==value :
                        #     k=i
                        #     l=j
                        matrix[x[i],y[i]]=0
                        if score<=alpha:
                            table[idmatrix]=score
                            return score
                        beta=min(beta,score)
                    table[idmatrix]=score
                    return score
        
    def choose_move(self,matrix):
        print(len(table))
        alpha=-10000
        beta=10000
        x,y=np.where(matrix==0)
        k=0
        l=0
        if self.state=='X': 
           n=1
        else : n=2
        best_score=-10000
        k,l=-1,-1
        for i in range(len(x)):
            matrix[x[i],y[i]]=n
            score=self.alpha_beta(matrix,0,False,alpha,beta)
            # print(score,x[i],y[i])
            if score>best_score:
                best_score=score
            
                k,l=x[i],y[i]
            matrix[x[i],y[i]]=0
            # if score>=beta:
            #     break
            # alpha=max(alpha,score)
            # print(best_score)
        return k,l,False
    # else:
        #     best_score=+10000
        #     for i in range(len(x)):
        #         matrix[x[i],y[i]]=2
        #         score=self.mini_max(matrix,False)
        #         print(score,x[i],y[i])
        #         if score<best_score:
        #             best_score=score

        #             k,l=x[i],y[i]
        #         matrix[x[i],y[i]]=0
        #     return k,l,False
            

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
            print('clicked')
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
            
    

def evaluate(matrix):
    x=Player('X')
    o=Player('O')
    x.check_win(matrix)
    o.check_win(matrix)
    if x.wins==True :return 10
    elif o.wins==True : return -10
    else : 
        if len(np.where(matrix==0)[0])==0 : return 0
        else: return -1  
            
        
if __name__ == '__main__':
    X_player=HumanPlayer('X')
    O_player=AIPlayer('O')
    window = Window(X_player, O_player)
    pyglet.app.run()


