for w in range(1, 101):
    from PIL import Image
    im = Image.open("out"+str(w)+".png")
    pixels = im.load()
    i = 0
    string = ""
    while True:
        if i >= im.size[0]: break
        p = pixels[i, 0]
        string += (chr(round(p[2]/10/(p[1]/256)/(p[0]/256))))
        i += 1
    if w == 1:
        freqs = [{} for i in range(len(string))]
    for loc in range(len(string)):
        try:
            freqs[loc][string[loc]] += 1
        except:
            freqs[loc][string[loc]] = 1
flag = ""
for loc in freqs:
    max = 0
    char = ""
    for k in loc:
        if loc[k] > max:
            max = loc[k]
            char = k
    flag += char
print(flag)
