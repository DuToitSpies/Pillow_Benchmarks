import sys
import os

import matplotlib.pyplot as plt
import numpy as np

benchmark = sys.argv[1]
num_bins = int(sys.argv[2])
min_bin = float(sys.argv[3])
max_bin = float(sys.argv[4])
comparison = sys.argv[5]

datafiles = []
data = []
binvals = []
bins = []
comparisons = ["hpy", "capi", "cpython", "pypy", "graalpython"]
labels = []

datapath = "../"+benchmark+"/output/"
outfiles = os.listdir(datapath)

for output in outfiles:
    if comparison in output:
        labels.append(output)
        datafiles.append(output)
        data.append([])
        binvals.append(np.zeros(num_bins))


for i in range(len(datafiles)):
    f = open(datapath+datafiles[i])
    for line in f:
        line.strip()
        data[i].append(float(line))

for i in range(num_bins):
    bins.append(round(min_bin+i/num_bins*(max_bin-min_bin), 5))

plt.hist(data[0], bins, color='red', label=labels[0], alpha=0.5)
plt.hist(data[1], bins, color='blue', label=labels[1], alpha=0.5)
if comparison in ["hpy", "capi"]:
    plt.hist(data[2], bins, color='green', label=labels[2], alpha=0.5)
plt.xlabel("Time [s]")
plt.ylabel("Frequency")
plt.title("Histogram of benchmark performance of the Pillow " + benchmark + " method written in HPy and the C-API  on " + comparison)
plt.legend()
plt.show()
