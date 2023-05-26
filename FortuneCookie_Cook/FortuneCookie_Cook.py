'''
FortuneCookie
Samantha cook
4/25/2023
Python II
'''

import random

file = open('fortunes.txt', 'r')
fortunes = file.readlines()
print('Your fortune reads...')
print(random.choice(fortunes))
file.close()
