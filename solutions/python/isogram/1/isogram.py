def is_isogram(phrase):
    phrase = phrase.lower()
    x = set()
    for i in phrase:
        if i == ' ' or i == '-':
            continue
        if i in x :
            return False
        else:
            x.add(i)
    return True
        
