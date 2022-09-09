from PIL import Image

import sys
import timeit

impl = sys.implementation.name
api = sys.argv[1]

jpg1 = Image.new("RGBA",(512,512))
jpg2 = Image.new("RGBA",(512,512))
outfile = open("output/" + impl + "_" + api, "w")

for i in range(100):
    start_time = timeit.default_timer()
    for i in range(40):
        im = Image.blend(jpg1, jpg2, 0.5)
    outfile.write(str(timeit.default_timer() - start_time)+"\n")

outfile.close()
