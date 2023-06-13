#!/usr/bin/env python3

s = 'utah texas maine iowa'
states = s.split()
states.sort()
print(states[0])
print(states[-1])
states.append('new york')
print(states[-1])
for i, s in enumerate(states):
    print(f'Index: {i} State: {s}')
for i, s in enumerate(states):
    states[i] = s.title()
s = ':'.join(states)
print(s)