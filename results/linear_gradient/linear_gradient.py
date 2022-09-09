from PIL import Image

import sys
import timeit

impl = sys.implementation.name
api = sys.argv[1]

outfile = open("output/" + impl + "_" + api, "w")

for i in range(200):
    start_time = timeit.default_timer()
    for i in range(500):
        im = Image.linear_gradient('L')
    outfile.write(str(timeit.default_timer() - start_time)+"\n")

outfile.close()
