# You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near",
# unfortunately, is as close as you can get - the instructions on the Easter
# Bunny Recruiting Document the Elves intercepted start here, and nobody had
# time to work them out further.

# The Document indicates that you should start at the given coordinates (where
# you just landed) and face North. Then, follow the provided sequence: either
# turn left (L) or right (R) 90 degrees, then walk forward the given number of
# blocks, ending at a new intersection.

# There's no time to follow such ridiculous instructions on foot, though, so you
# take a moment and work out the destination. Given that you can only walk on
# the street grid of the city, how far is the shortest path to the destination?

# For example:

# Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
# R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
# R5, L5, R5, R3 leaves you 12 blocks away.
# How many blocks away is Easter Bunny HQ?

from collections import defaultdict
import sys

class Direction:
    def __init__(self):
        self.state = 0

    def left(self):
        self.state -= 1

    def right(self):
        self.state += 1

    def turn(self, direction):
        if direction == 'L':
            self.left()
        elif direction == 'R':
            self.right()
        else:
            raise ValueError("Unknown direction %s" % direction)

    @property
    def facing(self):
        state = self.state % 4
        return ['north', 'east', 'south', 'west'][state]

def parse_document(sequence):
    x, y = 0, 0

    direction = Direction()
    movements = defaultdict(int)
    
    for line in sequence.split(', '):
        turn, distance = line[0], line[1:]
        direction.turn(turn)
        movements[direction.facing] += int(distance)

    east_west = movements['east'] - movements['west']
    north_south = movements['north'] - movements['south']
    print('distance: {}'.format(north_south + east_west))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("provide sequence")
        raise SystemExit()
    parse_document(sys.argv[1])
