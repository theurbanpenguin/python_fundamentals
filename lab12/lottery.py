#!/usr/bin/env python3
import random

n_list = []
u_selection = []

for n in range(1, 43):
    n_list.append(n)

for s in range(1, 7):
    selection = random.choice(n_list)
    u_selection.append(selection)
    n_list.remove(selection)

print(u_selection)
