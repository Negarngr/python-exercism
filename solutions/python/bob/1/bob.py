def response(hey_bob):
    message = hey_bob.strip()
    if message=="":
        return 'Fine. Be that way!'

    has_letters = any(char.isalpha for char in message)

    if message.isupper()and has_letters and message.endswith ("?"):
        return "Calm down, I know what I'm doing!"
    elif message.endswith ("?"):
        return 'Sure.'
    elif message.isupper() and has_letters:
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'
