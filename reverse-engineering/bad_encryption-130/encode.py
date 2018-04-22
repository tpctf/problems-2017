for i in range(1,101):
    tel1l1l1l1l1l1l1lt = "REDACTED"
    import builtins, random
    l1l1l1l1l1l1l1l = getattr(builtins, "__import__")
    l1l1l1l1l1l1l1l = l1l1l1l1l1l1l1l("PIL.Image")
    l1l1l1l1l1l1l1ll1l1l1l1l1l1l1l = l1l1l1l1l1l1l1l.Image
    l1l1l1l1l1l1l1ll1l1l1l1l1l1l1ll1l1l1l1l1l1l1l = l1l1l1l1l1l1l1ll1l1l1l1l1l1l1l.new("RGB", (len(tel1l1l1l1l1l1l1lt), 1), "white")
    l1l1l1l1l1l1l1ll1l1l1l1l1l1l1ll1l1l1l1l1l1l1ll1l1l1l1l1l1l1l = l1l1l1l1l1l1l1ll1l1l1l1l1l1l1ll1l1l1l1l1l1l1l.load()
    l1l1l1l1l1l1l1ll1l1l1l111l1l11 = 0
    for l1l1l1l1l1l1l1ll1l1l1l1l1l1l11 in tel1l1l1l1l1l1l1lt:
        l1l1l1l1l1l1l1ll1l1l1l1l1l1l11 = ord(l1l1l1l1l1l1l1ll1l1l1l1l1l1l11)
        l1l1l1l1l1l1l1ll1l1l1l1lll1l111 = random.randint(1,256)
        l1l1l1l1l1l1l1ll1l1l1l1lll1l112 = random.randint(1,256)
        l1l1l1l1l1l1l1ll1l1l1l1lll1l113 = random.randint(1,256)
        l1l1l1l1l1l1l11ll1l1l1l1lll1l111 = (l1l1l1l1l1l1l1ll1l1l1l1lll1l111/256)
        l1l1l1l1l1l1l11ll1l1l1l1lll1l112 = (l1l1l1l1l1l1l1ll1l1l1l1lll1l112/256)
        l1l1l1l1l1l1l11ll1l1l1l1lll1l113 = (l1l1l1l1l1l1l1ll1l1l1l1lll1l113/256)
        l1l121l1l1l1l11ll1l1l1l1lll1l111 = l1l1l1l1l1l1l1ll1l1l1l1l1l1l11*l1l1l1l1l1l1l11ll1l1l1l1lll1l111
        l1l121l1l1l1l11ll1l1l1l1lll1l112 = l1l121l1l1l1l11ll1l1l1l1lll1l111*l1l1l1l1l1l1l11ll1l1l1l1lll1l112
        l1l1l1l1l1l1l1ll1l1l1l1l1l1l1ll1l1l1l1l1l1l1ll1l1l1l1l1l1l1l[l1l1l1l1l1l1l1ll1l1l1l111l1l11,0] = (l1l1l1l1l1l1l1ll1l1l1l1lll1l111, l1l1l1l1l1l1l1ll1l1l1l1lll1l112, round(l1l121l1l1l1l11ll1l1l1l1lll1l112*10))
        l1l1l1l1l1l1l1ll1l1l1l111l1l11 += 1
    l1l1l1l1l1l1l1ll1l1l1l1l1l1l1ll1l1l1l1l1l1l1l.save("out"+str(i)+".png")
