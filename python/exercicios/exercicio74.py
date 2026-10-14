from random import randint

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(n)
print('O maior número gerado é: ', max(n))
print('O menor número gerado é: ', min(n))