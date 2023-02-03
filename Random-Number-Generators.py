#Random Number Generators
import random

#1.Number Generator that picks a random number through 1-1000
num = random.randint(1, 1000)
print(num)

#2. Random Number Generator that picks a random number through 5 and 10
num = random.randrange(5, 10, 2)
print(num)

#3. Random Number Generator that picks a random floating point number within 200 and 500
num = random.uniform(200, 500)
print(num)