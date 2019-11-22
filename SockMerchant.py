import math
import os
import random
import re
import sys

numOfSocks = int(raw_input())
socks = map(int, raw_input().split())


current = 0;
pairs = 0;
found = 0;

for sock in socks:
    current = sock
    found = 0

    for y in socks:
        if y == current:
            found += 1

        if found == 2:
            socks.pop(socks.index(y))
            socks.pop(socks.index(current))
            pairs += 1
            found = 0

print(pairs)
