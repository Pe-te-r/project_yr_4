from random import choice
 
def get_code(length = 4):
    return ''.join([choice('0123456789') for _ in range(length)])

def verify_code(saved_code, user_code):
    return saved_code == user_code