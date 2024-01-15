def array_subset(array, index, lenth):
    out = []
    for i in range(index, index+lenth):
        tchar = int(array.pop(index))
        tchar = tchar.to_bytes(2, "big")
        for e in tchar:
            if e != 0:
                out.append(chr(e))
    return out

def chararraytofloat(chararray: []):
    auxarray = []
    for c in chararray:
        if c.isdigit() or c == ".":
            auxarray.append(c)
    auxstr = "".join(auxarray)
    try:
        out = float(auxstr)
    except:
        out = 0.0

    return out
