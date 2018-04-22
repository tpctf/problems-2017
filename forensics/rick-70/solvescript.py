f1 = open("rick", "rb").read()
f2 = open("maxresdefault.jpg", "rb").read()
f3 = open("out.jpg", "wb")

import itertools

for j, k in zip(f1, itertools.cycle(f2)):
    f3.write(bytes([j^k]))

