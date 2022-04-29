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

""" cram-max : order the elements by following the rules of a heap-max"""
def cram_max(A, i, length):
    l   = left(i)
    r   = right(i)
    max = None

    if l < length and A[l] > A[i]:
        max = l
    else:
        max = i
    
    if r < length and A[r] > A[max]:
        max = r

    if max != i:
        A[max], A[i] = A[i], A[max]
        cram_max(A, max, length)

""" create a heap-max"""
def create_heap_max(table):
    length = len(table)
    for i in range(math.floor(length/2) - 1, -1, -1):
        cram_max(table, i, length)
    return table

""" sort a table using the heap-max : min -> max"""
def heap_sort_max(table):
    heap = create_heap_max(table)
    length = len(heap)
    for i in range(len(heap) - 1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        length-=1
        cram_max(heap, 0, length)
    return heap

