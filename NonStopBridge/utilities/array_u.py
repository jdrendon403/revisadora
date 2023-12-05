def array_subset(array, index, lenth):
    out = []
    for i in range(index, index+lenth):
        tchar = int(array.pop(index))
        tchar = tchar.to_bytes(2, "big")
        for e in tchar:
            if e != 0:
                out.append(chr(e))
    return out
