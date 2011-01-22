import sys
import math

DIVISION = 100.0
CYCLE = 5

# TODO
# 2. determine du from length of ellipse

def angles(du, a, b):
    phi = 0
    while phi <= 2 * math.pi:
        yield phi
        phi += du / math.sqrt((a * math.sin(phi))**2 + (b * math.cos(phi))**2)

def coordinate(du, a, b):
    for angle in angles(du, a, b):
        yield (a * math.cos(angle), b * math.sin(angle))

def circumference(a, b):
    """Return a length of a circumference of an ellipse.

    @param a, b length of two semi-axes

    reference: http://en.wikipedia.org/wiki/Ellipse#Circumference
    """
    expr = ((a - b)/(a + b))**2
    return math.pi * (a + b) * (1 + (3 * expr)/(10 + math.sqrt(4 - 3 * expr)))

def draw(argv=None):
    if not argv:
        argv = sys.argv
    filename = argv[1]
    a = float(argv[2])
    b = float(argv[3])
    du = 0.01

    with open(filename, 'w') as out_file:
        print >> out_file, '#x\ty'
        for i, coord in enumerate(coordinate(du, a, b)):
            i %= CYCLE * 2
            if i < CYCLE:
                print >> out_file, '{0}\t{1}'.format(*coord)
            else:
                print >> out_file, ''
                

if __name__ == '__main__':
    draw(sys.argv)
