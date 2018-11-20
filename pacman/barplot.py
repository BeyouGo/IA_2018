import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
nb_maps = 3
nb_algo = 4
run_times = np.random.rand(3, 4)
run_times
plt.figure(figsize=(16, 10))
plt.title("Running times of different search algorithms")
plt.xlabel("Maps")
plt.ylabel("Running time (s)")

bar_width = .5
bar_positions = np.arange(nb_maps)*bar_width*(nb_algo+1)

for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, run_times[:, i], width=bar_width)

plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, ["Map %d" % i for i in range(nb_maps)])
plt.legend(["Algo %d" % i for i in range(nb_algo)])
#plt.savefig("myfigure.png")