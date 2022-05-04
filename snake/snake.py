import tkinter as tk
import keyboard
import time
import numpy as np

'''
Juego de Snake hecho con Tkinter y Numpy solamente. Proyecto intermedio
'''

#Variables globales
def init_vars():
    global snake,height,width,points,x
    snake = []
    points = -1
    height = 640
    width = 640

init_vars()
frame = tk.Tk()
frame.geometry('700x700')
frame.title('Snake. By: Sebastian Yusti')
canvas = tk.Canvas(height=height, width=width, bg='Black')
canvas.pack()

def head(count=20):
    a = canvas.create_rectangle(80+count,0,100+count,20, fill='Red')
    snake.append(a)
    canvas.pack()
    
def body(count,init,fin=0):
    for i in range(init,fin):
        count += 20
        gen = canvas.create_rectangle(120-count,0,140-count,20,fill='Blue')
        snake.append(gen)
        frame.update()
        canvas.pack()
        
def fieldprint():
    canvas.create_line(2,2,0,height, fill='Gray')

#Creacion del cuerpo

head()
body(20,0,3)

def FRUIT():
    FRUT = canvas.create_rectangle(0,0,20,20, fill='Yellow')
    canvas.pack()
    return FRUT

FRUT = FRUIT()
    
def FRUIT_CHANGE():
    fcoorX = np.random.randint(10,500)
    fcoorY = np.random.randint(10,500)
    x1f,y1f,x2f,y2f = fcoorX+20, fcoorY+20, fcoorX,fcoorY
    canvas.coords(FRUT,x1f,y1f,x2f,y2f)
    canvas.pack()
    
def RANDCOORD()->tuple():
    a = np.random.randint(10,500)    
    b = np.random.randint(10,500)
    return a,b
        
def CHANGE_BODY():
    OLD_COORDS = []
    NEW_COORDS = []
    for snk in snake:
        OLD_COORDS.append(canvas.coords(snk))
    for i in range(1,len(snake)):
        canvas.coords(snake[i], OLD_COORDS[i-1])
        new = canvas.coords(snake[i])
        NEW_COORDS.append(new)
        time.sleep(0.01)
    del OLD_COORDS
    return NEW_COORDS
        
def POSITION_HEAD(snake,xparm1=0,yparm1=0,xparm2=0,yparm2=0):   
    x1,y1,x2,y2 = canvas.coords(snake[0])
    x1 += xparm1 
    x2 += xparm2
    y1 += yparm1
    y2 += yparm2 
    canvas.coords(snake[0],x1,y1,x2,y2)
    NEW_POS = canvas.coords(snake[0])
    return NEW_POS
    frame.update()
    
CHANBODY = 0
def BODY_GROWN():
    body(20, 3+1,4+1)
    frame.update()
    
def CHANGE_ALL(snake, change, mills, position_0):
    for i in range(1,len(snake)):
        canvas.coords(snake[i], change[i-1])
        
def GAME_OVER():
    TEXT_POINTS = canvas.create_text(325, 400, text='Game Over', fill="White", font=('Helvetica 15 bold'))

def GENERAL_MOVE():
    X_AXIS = 1
    Y_AXIS = 0
    mills = 0.01
    points = 0
    xparm1,xparm2,yparm1,yparm2=20,20,0,0  
    TEXT_POINTS = canvas.create_text(60, 40, text=f'Puntos: {points}', fill="White", font=('Helvetica 15 bold'))
    POSITION_0 = canvas.coords(snake[0])
    x = True
    while x == True:
        BODY_POSITION = canvas.coords(snake[1])
        VAR_POSITION = canvas.coords(snake[0])
        if VAR_POSITION[0] != BODY_POSITION[0]:
            if keyboard.is_pressed('s'):
                X_AXIS = 0
                Y_AXIS = 1
                xparm1,xparm2,yparm1,yparm2=0,0,20,20
        if VAR_POSITION[0] != BODY_POSITION[0]:
            if keyboard.is_pressed('w'):
                X_AXIS = 0
                Y_AXIS = -1
                xparm1,xparm2,yparm1,yparm2=0,0,-20,-20  
        if VAR_POSITION[1] != BODY_POSITION[1]:
            if keyboard.is_pressed('d'):
                X_AXIS = 1
                Y_AXIS = 0
                xparm1,xparm2,yparm1,yparm2=20,20,0,0  
        if VAR_POSITION[1] != BODY_POSITION[1]:
            if keyboard.is_pressed('a'):
                X_AXIS = -1
                Y_AXIS = 0
                xparm1,xparm2,yparm1,yparm2=-20,-20,0,0     
    
        for snk in snake:
            canvas.move(snk,X_AXIS,Y_AXIS)
            frame.update()   
    
        CHANGE = CHANGE_BODY()
        xh1,xh2,yh1,yh2 = POSITION_HEAD(snake,xparm1=xparm1,xparm2=xparm2,yparm1=yparm1,yparm2=yparm2)
        canvas.coords(snake[0], xh1,xh2,yh1,yh2)
        CHANGE_ALL(snake, CHANGE, mills,POSITION_0)
        
        for i in range(1,len(snake)-1):
            if canvas.coords(snake[0]) == canvas.coords(snake[i]):
                GAME_OVER()
                x = False
          
        if VAR_POSITION[0] < 0: 
            y1,y2 = VAR_POSITION[1], VAR_POSITION[3]
            for i in range(len(snake)):
                canvas.coords(snake[i],width+20,y1,width,y2)
        elif VAR_POSITION[0] > width: 
            y1,y2 = VAR_POSITION[1], VAR_POSITION[3]
            for i in range(len(snake)):
                canvas.coords(snake[i],20,y1,0,y2)
        elif VAR_POSITION[1] < 0: 
            x1,x2 = VAR_POSITION[0], VAR_POSITION[2]
            for i in range(len(snake)):
                canvas.coords(snake[i],x1,height+20,x2,height)
        elif VAR_POSITION[1] > height: 
            x1,x2 = VAR_POSITION[0], VAR_POSITION[2]
            for i in range(len(snake)):
                canvas.coords(snake[i],x1,20,x2,0)
                
        if np.allclose(canvas.coords(snake[0]), canvas.coords(FRUT), atol=20):
            FRUIT_CHANGE()
            BODY_GROWN()
            mills -= mills/1.5
            points +=1
            canvas.delete(TEXT_POINTS)
            TEXT_POINTS = canvas.create_text(60, 40, text=f'Puntos: {points}', fill="White", font=('Helvetica 15 bold'))
            canvas.pack()
            frame.update()
        time.sleep(0.00001)            
            


GENERAL_MOVE()
canvas.pack()
frame.mainloop()

