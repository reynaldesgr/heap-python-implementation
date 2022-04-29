import math

import numpy as np

""" parent of element at index i"""
def parent(i):
    return math.floor(i/2)

""" left's children of element at index i"""
def left(i):
    return 2*i + 1 

""" right's children of element at index i"""
def right(i):
    return 2*i + 2

""" cram-min : order the elements by following the rules of a heap-min"""
def cram_min(A, i, length):
    l   = left(i)
    r   = right(i)
    min = None

    if l < length and A[l] < A[i]:
        min = l
    else:
        min = i
    
    if r < length and A[r] < A[min]:
        min = r

    if min != i:
        A[min], A[i] = A[i], A[min]
        cram_min(A, min, length)

""" create a heap-min"""
def create_heap_min(table):
    length = len(table)
    for i in range(math.floor(length/2) - 1, -1, -1):
        cram_min(table, i, length)
    return table

""" sort a table using the heap-min : max -> min"""
def heap_sort_min(table):
    heap = create_heap_min(table)
    length = len(heap)
    for i in range(len(heap) - 1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        length-=1
        cram_min(heap, 0, length)
    return heap



