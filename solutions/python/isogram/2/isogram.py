def is_isogram(phrase):
    phrase = phrase.lower()
    x = set()
    for ch in phrase:
        if not ch.isalpha():
            continue
        if ch in x :
            return False
        x.add(ch)
    return True
        
