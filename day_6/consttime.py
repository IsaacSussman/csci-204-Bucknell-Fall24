import matplotlib.pyplot as plt

def test_algorithm():
  '''
  tests to see how the time an algorithm takes
  changes depending on the size of the input
  tries input sizes 1 to 10
  for an an algorithm named timed_algorithm
  '''
  num_tests = 10
  tests = list(range(num_tests))
  times = []
  for n in tests:
    t = timed_algorithm(n)
    times = times + [t]
  print(tests, times)
  scatter_plot(tests, times)

def scatter_plot(x,y):
  '''
  creates a scatter plot from x and y
  where x and y are lists
  x is the size of the input, n
  y is the time taken by the algorithm
  '''
  plt.xlabel('n') # x-axis label
  plt.ylabel('time') #y-axis label
  plt.title('Time complexity') # title
  plt.plot(x, y)
  plt.show()

def timed_algorithm(n):
  '''
  An An algorithm! What's its time complexity?
  '''
  time = 1
  return time

test_algorithm()