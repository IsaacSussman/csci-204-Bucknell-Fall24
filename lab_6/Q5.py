def beautify_tree(levels, length, angle, thickness):
  if levels == 0:
    dot(3+random.random()*4, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
  else:
    width(thickness)
    forward(length)
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