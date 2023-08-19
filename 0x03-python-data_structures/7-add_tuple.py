#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 1:
        tuple_a = (0, 0)
    if len(tuple_b) < 1:
        tuple_b = (0, 0)
    if len(tuple_a) < 2:
        tuple_a = (tuple_a[0], 0)
    if len(tuple_b) < 2:
        tuple_b = (tuple_b[0], 0)
    if tuple_a[0] is None:
        tuple_a[0] = 0
    if tuple_a[1] is None:
        tuple_a[1] = 0
    if tuple_b[0] is None:
        tuple_b[0] = 0
    if tuple_b[1] is None:
        tuple_b[1] = 0
    a, b = (tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1])
    return (a, b)
