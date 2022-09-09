from PIL import Image
import sys, os
from timeit import default_timer as dt

impl = sys.implementation.name
api = sys.argv[1]

out = open("output/"+impl+"_"+api, "w")
im = Image.new("RGB",(400,400))

for i in range(100):
    start = dt()
    for j in range(400):
        for k in range(400):
            im.putpixel((j,k),(i,i,i))
    out.write(str(dt()-start)+"\n")

out.close()
