from library.hello import get_greeting

# Some comment.
def say_hello():
    response = get_greeting()
    return f"The Python library says: '{response}'"


print(say_hello())
