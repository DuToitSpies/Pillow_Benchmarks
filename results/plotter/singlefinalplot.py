import matplotlib.pyplot as plt
import sys, os
import numpy as np

benchmark = sys.argv[1]
num_bins = int(sys.argv[2])
min_val = float(sys.argv[3])
max_val = float(sys.argv[4])

filenames = ["cpython_capi","cpython_hpy","graalpython_capi", "graalpython_hpy"]
data = [[],[],[],[]]
bins = []
labels = filenames

datapath = "../" + benchmark + "/output/"
datafiles = []
for file in filenames:
    datafiles.append(open(datapath+file))

for i in range(4):
    for line in datafiles[i]:
        data[i].append(float(line))

for i in range(num_bins):
    bins.append(round(min_val+i/num_bins*(max_val-min_val),8))

plt.hist(data[0], bins, color='gray', label=labels[0], alpha=0.8)
plt.hist(data[1], bins, color='blue', label=labels[1], alpha=0.5)
plt.hist(data[2], bins, color='orange', label=labels[2], alpha=0.8)
plt.hist(data[3], bins, color='red', label=labels[3], alpha=0.5)
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Frequency")
plt.show()