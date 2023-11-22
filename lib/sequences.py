#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
    else:
        sequence = [0, 1]
        if length == 1:
            print([0])
        elif length == 2:
            print(sequence)
        else:
            while len(sequence) < length:
                next_num = sequence[-1] + sequence[-2]
                sequence.append(next_num)
            print(sequence)
