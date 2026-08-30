def transform(legacy_data):
    x = {}
    for i,j in legacy_data.items() :
        for u in j :
            u = u.lower()
            x[u] = i
    return x

