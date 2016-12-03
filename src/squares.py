import itertools
import re

def valid_triangle(side1, side2, side3):
    """True if sum of any two greater than the third side"""
    
    orders = itertools.permutations([side1, side2, side3])

    for order in orders:
        if not (order[0] + order[1]) > order[2]:
            return False

    return True

def total_valid_triangles(triangles):
    total = 0
    for triangle in triangles:
        if valid_triangle(*triangle):
            total += 1

    return total

def _process_line(l):
    return [int(i.strip()) for i in l.strip().split('  ') if i.strip()]

if __name__ == '__main__':
    with open('squares_input.tsv', 'r') as f:
        input_triangles = [_process_line(l) for l in f]

    print(total_valid_triangles(input_triangles))
