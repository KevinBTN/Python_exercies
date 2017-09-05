import random

a = [random.randint(0,50) for i in range(10)]
b = [random.randint(0,50)for u in range(13)]



for i in a:
    if i in b:
        print(i)
