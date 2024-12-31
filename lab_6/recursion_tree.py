from turtle import *
import random

def good_forward(length):
  for i in range(int(length)//5):
      forward(3.25)
      pencolor("black")
      forward(1.75)
      pencolor(251,251,63)
  forward(length%5)
def make_a_polygon(sides, levels, length) :
    """!
    Draws a number of sides of a polygon.
        sides is the total number of sides of the polygon
        levels is the number of sides to draw
        length is how long each side is
    """
    if levels == 0 :
       return
    else :
        good_forward(length)
        right(360 / sides)
        make_a_polygon(sides, levels - 1, length)

def create_tree(levels):
  """!
  TODO: Create a simple Y shaped tree.
  """
  if levels == 0:
    return
  else:
    good_forward(30)
    left(30)
    create_tree(levels-1)
    right(60)
    create_tree(levels-1)
    left(30)
    back(30)



def create_tree2(levels, length):
  """!
  TODO: Create a Y shaped tree where draw lengths are reduced by a factor of 0.8.
  """
  if levels == 0:
    return
  else:
    good_forward(length)
    left(30)
    create_tree2(levels-1,length*0.8)
    right(60)
    create_tree2(levels-1,length*0.8)
    left(30)
    back(length)

def create_tree3(levels, length, angle):
  """!
  TODO: Create a Y shaped tree where the draw lengths reduce by a factor of 0.8 and angle widths increase by a factor of 2.
  """
  if levels == 0:
    return
  else:
    good_forward(length)
    left(angle)
    create_tree3(levels-1,length*0.8, angle)
    right(angle*2)
    create_tree3(levels-1,length*0.8, angle)
    left(angle)
    back(length)

def beautify_tree(levels, length, angle, thickness):
  if levels == 0:
    dot(9+random.random()*4, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
  else:
    width(thickness)
    good_forward(length)
    left(angle)
    if random.random()<0.91:
      beautify_tree(levels-1,length*((random.random()+1)/2), angle*(((random.random()*2)+4)/5), thickness*((random.random()+1)/2))
    right(angle)
    if random.random()<0.91:
      beautify_tree(levels-1,length*((random.random()+1)/2), angle*(((random.random()*2)+4)/5), thickness*((random.random()+4)/5))
    right(angle)
    if random.random()<0.91:
      beautify_tree(levels-1,length*((random.random()+1)/2), angle*(((random.random()*2)+4)/5), thickness*((random.random()+4)/5))
    left(angle)
    penup()
    back(length)
    pendown()

def grow_forest() :
    for x in range(-300, 300, 30):
        xcoord = x + random.randint(-15, 15)
        ycoord = random.randint(-50, 50)
        penup()
        setx(xcoord)
        sety(ycoord)
        pendown()
        
        """
        Change the following 3 lines to make random 
          - levels, 
          - lengths, and 
          - angles
        """ 
        levels = int(4 + 2*random.random())
        length = random.randint(10,50)
        angle = random.randint(10, 50)
        t = 2 +random.random()*2
        beautify_tree(levels, length, angle, t) 


"""
The code below is effectively the Main function you will be calling functions in.
You should feel free to play with the parameters below to get different images!
"""
if __name__ == "__main__" :
    colormode(255)
    pencolor(251,251,63)

    # Turns the turtle North to begin with
    left(90)      

    # Sets the draw speed of the turtle
    speed(0)      

    # True if you would like to watch as the turtle draws, false if you just want to see the result
    tracer(False)  

    # TODO: Test that this runs. Comment this out before you continue with the rest of the lab.
    # ---
    #make_a_polygon(5, 5, 100)
    # ---

    # TODO: The function calls you will make will go here
    # beautify_tree(6, 50, 20, 3)
    grow_forest()

    
    
    """
    The following code is corresponds to the forest part of the lab, which counts for bonus marks.
    Uncomment it and play around with the parameters. 
    """
    # grow_forest()
    

    # Wait until user clicks to exit screen
    exitonclick()