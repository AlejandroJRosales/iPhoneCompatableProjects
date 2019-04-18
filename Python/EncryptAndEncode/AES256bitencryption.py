import random

key = "{:02x}".format(random.randint(0, 1 << 256))

print(key)
