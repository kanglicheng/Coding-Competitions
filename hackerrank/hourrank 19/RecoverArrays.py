#!/bin/python3

import sys


n = int(input().strip())
file = list(map(int, input().strip().split(' ')))
#  Print the number of arrays defined in 'file' to STDOUT.

i = 0
count = 0
while i < n:
    i= i + file[i] + 1
    count += 1
print(count)
