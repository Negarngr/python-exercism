alphabet = {'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' ,'t' , 'u' , 'v' , 'w' , 'x' ,'y' ,'z' }
def is_pangram(sentence):
    sentence = sentence.lower()
    x = set()
    for i in sentence :
        if i not in alphabet:
            continue
        x.add(i)
    return x == alphabet

