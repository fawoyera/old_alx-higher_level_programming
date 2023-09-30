#!/usr/bin/python3
"""Module to return a list of lists of pascal triangle for number n"""


def pascal_triangle(n):
    """Function to create list of lists of pascal triangle for n"""
    if n <= 0:
        return []
    pascal = [[int(1)]]
    for i in range(n - 1):
        pascal.append([int(combination(i + 1, r)) for r in range(i + 2)])
    return pascal


def combination(n, r):
    """Function to compute the combination nCr"""
    return (fact(n) / (fact(n - r) * fact(r)))


def fact(n):
    """Function to compute the factorial of a number n"""
    result = 1
    if n == 0:
        return result
    for i in range(n):
        result *= i + 1
    return result
