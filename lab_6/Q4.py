def create_tree3(levels, length, angle):
  """!
  TODO: Create a Y shaped tree where the draw lengths reduce by a factor of 0.8 and angle widths increase by a factor of 2.
  """
  if levels == 0:
    return
  else:
    forward(length)
    left(angle)
    create_tree3(levels-1,length*0.8, angle)
    right(angle*2)
    create_tree3(levels-1,length*0.8, angle)
    left(angle)
    back(length)