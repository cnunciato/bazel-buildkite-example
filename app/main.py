from library.hello import say_hello

def hi_there():
    response = say_hello()
    return f"Hey! there's a message from the Python library: '{response}'"

print(hi_there())
