"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.


def foo(x):
    if x <= 1:
        return x
    else:
        ra = foo(x - 1)
        rb = foo(x - 2)
        return ra + rb


def longest_run(mylist, key):
    ### TODO
    count = 0
    maxcount = 0

    for i in range(len(mylist)):
        if mylist[i] == key:
            count += 1
        else:
            count = 0
        if count > maxcount:
            maxcount = count
    return maxcount


class Result:
    """ done """

    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size  # run on left side of input
        self.right_size = right_size  # run on right side of input
        self.longest_size = longest_size  # longest run in input
        self.is_entire_range = is_entire_range  # True if the entire input matches the key

    def __repr__(self):
        return (
            'longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
            (self.longest_size, self.left_size, self.right_size,
             self.is_entire_range))


def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)


def longest_run_recursive(mylist, key):
    return longest_run_recursive_code(mylist, key)[2]
def longest_run_recursive_code(mylist, key):
    if len(mylist) == 0:
        return (0, 0, 0)

    if len(mylist) == 1:
        if mylist[0] == key:
            return (1, 1, 1)
        else:
            return (0, 0, 0)
    mid = len(mylist) // 2
    Left_Max = longest_run_recursive_code(mylist[:mid], key)
    Right_Max = longest_run_recursive_code(mylist[mid:], key)

    if Left_Max[0] != mid:
        left_run = Left_Max[0]
    else:
        left_run = Left_Max[0] + Right_Max[0]
    if Right_Max[1] != len(mylist) - mid:
        right_run = Right_Max[1]
    else:
        right_run = Right_Max[1] + Left_Max[1]
    Mid_Max = Left_Max[1] + Right_Max[0]
    if((Left_Max[2] >= Right_Max[2]) and (Left_Max[2] >= Mid_Max)):
        max = Left_Max[2]
    elif ((Right_Max[2] >= Left_Max[2]) and (Right_Max[2] >= Mid_Max)):
        max = Right_Max[2]
    else:
        max = Mid_Max

    return (left_run, right_run, max)


