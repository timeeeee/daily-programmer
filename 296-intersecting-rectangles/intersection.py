"""
Given some number of pairs that represent opposing corners of rectangles-
1,1 4,4
2,2 5,5
3,3 6,6
etc.
Find the area of the intersection of all of the rectangles.
"""

def intersection_1d(a, b, c, d):
    """
    Find the intersection of segments (a, b) and (c, d) on a number line.
    Return a tuple of the end points of the intersection, or (0, 0) if there is
    no intersection.
    """
    # Make sure segments are represented left to right
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c

    # Make sure first segment is on the left
    if a > c:
        a, b, c, d = c, d, a, b

    # There are 3 possible orderings for points a, b, c, d
    if b < c:  # a, b, c, d- the segments do not intersect
        return (0, 0)
    else:
        if b < d:  # a, c, b, d- segments overlap
            return (b, c)
        else:  # a, c, d, b- segment 2 is inside segment 1
            return (c, d)


def intersection_2d(rect1, rect2):
    """
    Find the intersection of two rectangles. Each rectangle is represented by
    a tuple of points, and each point is represented by a tuple of numbers.
    """
    ((rect1_x1, rect1_y1), (rect1_x2, rect1_y2)) = rect1
    ((rect2_x1, rect2_y1), (rect2_x2, rect2_y2)) = rect2

    # Find the intersection when projected onto both x and y axes
    x_min, x_max = intersection_1d(rect1_x1, rect1_x2, rect2_x1, rect2_x2)
    y_min, y_max = intersection_1d(rect1_y1, rect1_y2, rect2_y1, rect2_y2)
    return ((x_min, y_min), (x_max, y_max))


def area(rectangle):
    ((x1, y1), (x2, y2)) = rectangle
    return abs((x2 - x1) * (y2 - y1))


def area_of_intersection(rectangles):
    return area(reduce(intersection_2d, rectangles))


assert area(intersection_2d(((0, 0), (2, 2)), ((1, 1), (3, 3)))) == 1
rect1 = ((-3.5, 4), (1, 1))
rect2 = ((1, 3.5), (-2.5, -1))
assert area(intersection_2d(rect1, rect2)) == 8.75
rect1 = ((-4, 4), (-.5, 2))
rect2 = ((.5, 1), (3.5, 3))
assert area(intersection_2d(rect1, rect2)) == 0

# Try with 4 rectangle bonus input
rect1 = ((-3, 0), (1.8, 4))
rect2 = ((1, 1), (-2.5, 3.6))
rect3 = ((-4.1, 5.75), (0.5, 2))
rect4 = ((-1.0, 4.6), (-2.9, -0.8))
print area_of_intersection([rect1, rect2, rect3, rect4])
