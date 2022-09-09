import matplotlib.pyplot as plt
import sys, os
import numpy as np

funcs = os.listdir("..")
funcs.sort()
funcs.remove('plotter')

fig, axes = plt.subplots(6, 3)
#fig.suptitle("Histograms of benchmark performance of the Pillow methods written in HPy on CPython, PyPy, and GraalPython, and in the C-API  on CPython")
fig.subplots_adjust(hspace=0.5)

filenames = ["cpython_capi","cpython_hpy","graalpython_capi", "graalpython_hpy"]
data = []
bins = []
labels = ["C-API - CPython", "HPy - CPython", "C-API - GraalPython", "HPy - GraalPython"]

num_bins = 100
min_val = 0
max_val = [0.1,0.2,0.1,0.1,0.5,1.5,0.4,0.1,0.2,0.1,0.02,0.1,1,0.2,0.2,0.3,0.2,0.15]

numbers = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",]

datafiles = []
i = 0
for func in funcs:
    datafiles.append([])
    datapath = "../" + func + "/output/"
    for file in filenames:
        datafiles[i].append(open(datapath+file))
    i = i+1

j=0
for file in datafiles: 
    data.append([[],[],[],[]])
    bins.append([])
    for i in range(4):
        for line in file[i]:
            data[j][i].append(float(line))

    for i in range(num_bins):
        bins[j].append(round(min_val+i/num_bins*(max_val[j]-min_val),8))

    j = j+1

for i in range(len(datafiles)):
    x = i % 3
    y = i // 3

    axes[y][x].hist(data[i][0], bins[i], color='gray', label=labels[0], alpha=0.8)
    axes[y][x].hist(data[i][1], bins[i], color='blue', label=labels[1], alpha=0.5)
    axes[y][x].hist(data[i][2], bins[i], color='orange', label=labels[2], alpha=0.8)
    axes[y][x].hist(data[i][3], bins[i], color='red', label=labels[3], alpha=0.5)
    axes[y][x].set_title(numbers[i] + ") " + funcs[i] + " method")
    axes[y][x].set(xlabel="Time [s]", ylabel="Frequency")

plt.show()