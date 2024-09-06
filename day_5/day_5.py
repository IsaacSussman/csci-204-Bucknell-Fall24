import matplotlib.pyplot as plt
import time
from test_functions import *

func = [self_sum, triangular_sum, parabolic_sum]
times = [[], [], [], []]
for i in range (1, 20):
        start = time.time_ns()
        for j in range(1000000):
            self_sum(i)
        end = time.time_ns()
        times[0].append((end - start)/1000000)
        start = time.time_ns()
        for j in range(100000):
            triangular_sum(i)
        end = time.time_ns()
        times[1].append((end - start)/100000)
        start = time.time_ns()
        for j in range(1000):
            parabolic_sum(i)
        end = time.time_ns()
        times[2].append((end - start)/1000)
        start = time.time_ns()
        for j in range(1):
            big_sum(i)
        end = time.time_ns()
        times[3].append((end - start)/1)

print(times)
for i in times:
    plt.plot(i)

#plt.yscale("log")
plt.show()
        





