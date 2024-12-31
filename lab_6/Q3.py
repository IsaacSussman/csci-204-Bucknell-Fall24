def create_tree2(levels, length):
  """!
  TODO: Create a Y shaped tree where draw lengths are reduced by a factor of 0.8.
  """
  if levels == 0:
    return
  else:
    forward(length)
    left(30)
    create_tree2(levels-1,length*0.8)
    right(60)
    create_tree2(levels-1,length*0.8)
    left(30)
    back(length)