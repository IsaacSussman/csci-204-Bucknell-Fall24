def create_tree(levels):
  """!
  TODO: Create a simple Y shaped tree.
  """
  if levels == 0:
    return
  else:
    forward(30)
    left(30)
    create_tree(levels-1)
    right(60)
    create_tree(levels-1)
    left(30)
    back(30)