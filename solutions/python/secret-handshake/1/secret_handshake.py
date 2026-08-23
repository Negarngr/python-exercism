actions = {1: 'wink', 2: 'double blink', 4: 'close your eyes', 8: 'jump'}

def commands(binary_str):
    binary_str = int(binary_str, 2)
    result = []
    for bit in actions:
        if bit & binary_str:
            result.append(actions[bit])
    if binary_str & 16:
        result.reverse()
    return result