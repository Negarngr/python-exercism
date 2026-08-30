def flatten(iterable):
    x = []
    for i in iterable :
        if isinstance(i , list):
           u =flatten(i)
           x.extend(u)
        elif i == None :
            continue
        else:
            x.append(i)
    return x