# generate a random password base on the requirements
# letters
# numbers
# symbols

import random
import string
any_letter = random.choice(string.ascii_letters)

# 
# 
# chr(random.randrange(97, 97 + 26))


import random
import string
random.seed(10)
letters = string.ascii_lowercase
rand_letters = random.choices(letters,k=5) # where k is the number of required rand_letters


# map(lambda a : chr(a),  np.random.randint(low=65, high=90, size=4))


def randchar(a, b):
    return chr(random.randint(ord(a), ord(b)))