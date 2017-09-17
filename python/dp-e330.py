import operator
import itertools

def box_for(x, y, r):
    return [x-r, x+r, y-r, y+r]

def boxes_for_all(circles):
    print([box_for(*circle) for circle in circles])
    return [box_for(*circle) for circle in circles]

def bounding_box(circles):
    boxes = boxes_for_all(circles)
    xs = [a[0] for a in boxes] + [a[1] for a in boxes]
    ys = [a[2] for a in boxes] + [a[3] for a in boxes]
    return ((min(xs), min(ys)), (min(xs), max(ys)), (max(xs), max(ys)), (max(xs), min(ys)))
    return [min(low_lefts), min(upper_lefts), max(upper_rights), min(low_rights)]


circles = [
    (1,1,2),
    (2,2,0.5),
    (-1,-3,2),
    (5,2,1)
]

print(bounding_box(circles))
