# 
#Alexandre Seite 
import turtle as t 

def rightleaf(length):    
  #recursively draw a leaf that curves to the right   
   if length >0.2:        
    t.forward(length/3)        
    t.left(55)        
    leaf(length*.33)        
    t.right(55)        
    t.forward(length*2/3)        
    t.right(60)        
    rightleaf(length*.28)        
    t.left(63)        
    rightleaf(length*.9)        
    t.right(3)        
    t.backward(length) 
    
def leaf(length):    
  #The main recursive leaf drawing function, curve to the left   
  if length > 0.2:        
    t.forward(length/3)        
    t.right(55)        
    rightleaf(length*.33)        
    t.left(55)        
    t.forward(length*2/3)        
    t.left(60)        
    leaf(length*.28)        
    t.right(63)        
    leaf(length*.9)        
    t.left(3)        
    t.backward(length)        
    
t.tracer(False) 
t.pu() 
t.backward(100) 
t.pd() 
leaf(50.0) 
t.update() 
t.exitonclick()
