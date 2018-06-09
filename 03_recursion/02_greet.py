def greet2(name):
    print("how are you,", name, "?")

def bye():
    print("ok bye!")

def greet(name):
    print("hello,", name, "!")
    greet2(name)
    print("greeting ready to say bye...")
    bye()

greet("adit")