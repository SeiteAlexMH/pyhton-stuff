#sierpinski.py
#Alexandre Seite 
import turtle as t 
def sierpinski(sideLength, levels):    
  '''a short definition of the sierpinski function'''    
  if levels != 0:        
    for n in range(3):            
      sierpinski(sideLength/2,levels-1)            
      t.forward(sideLength)            
      t.left(120) 
      
t.tracer(False) 
sierpinski(300,7) 
t.update() 
t.exitonclick()
