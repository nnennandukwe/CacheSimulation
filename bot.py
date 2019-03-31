import sys
from collections import deque

def initialize():
    print("Welcome to THE CACHE SIMULATION")
    print("Pick a card... any card...")
    print("Just kidding...")

def build_test():
    messages = deque()
    with open('test', 'r') as f:
        for msg in f:
            msg = ''.join(list(msg)[:-1])
            messages.append(msg)

    return messages
