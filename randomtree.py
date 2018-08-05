#randomtree.py 
#Alexandre Seite 

import turtle as t 
import random 
def drawTree(levels, len, angle,shrink):    
  ''' draw the tree starting basic value    
  then randomizes from them '''    
  if levels > 0:        
    if levels<=3:           
      t.color(0,1,0)        
    else:            
      t.color("brown")        
    shrink=random.uniform(0.7,0.9)        
    angle=random.randint(10,20)        
    t.forward(len)        
    t.left(angle)        
    drawTree(levels-1, shrink * len, angle, shrink)        
    t.right(2 * angle)        
    drawTree(levels-1, shrink * len, angle, shrink)        
    t.pu()        
    t.left(angle)        
    t.backward(len)        
    t.pd() 
    
# main program 
t.tracer(False) 
t.up() 
t.left(90) 
t.backward(250) 
t.down() 

drawTree(10, 60, 13,.09) 
t.update() 
t.exitonclick()
