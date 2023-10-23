import random

def generate_code(length=9):
    scope = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    return "".join([random.choice(scope) for i in range(length)])

def cart_generate_code():
    return generate_code(15)