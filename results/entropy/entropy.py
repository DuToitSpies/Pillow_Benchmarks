from PIL import Image

import sys
import timeit

impl = sys.implementation.name
api = sys.argv[1]

im1 = Image.new('RGBA',(512,512))
outfile = open("output/" + impl + "_" + api, "w")

for i in range(100):
    start_time = timeit.default_timer()
    for i in range(200):
        ent_int = im1.entropy()
    outfile.write(str(timeit.default_timer() - start_time)+"\n")

outfile.close()
