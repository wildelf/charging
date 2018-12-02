#date: 2018/12/3


import random,string

def get_random_token():

    return ''.join(random.choices(string.ascii_uppercase + string.digits+string.ascii_lowercase, k=30))


