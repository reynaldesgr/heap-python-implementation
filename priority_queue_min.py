import heap_min

""" return the max of the priority file"""
def get_min_heap(heap):
    return heap[0]

""" extract the max from the heap and return (heap, max)"""
def extract_min_from_heap(heap, length):
    if length < 1:
        exit()
    min = get_min_heap(heap)
    heap[0] = heap[length - 1]
    heap = heap[:len(heap) - 1]
    heap_min.cram_min(heap, 0, len(heap))
    return heap, max

""" decrease the key at index i """
def decrease_heap_key(heap, i, key):
    if key > heap[i]:
        exit()
    heap[i] = key
    while i >= 0 and heap[heap_min.parent(i)] > heap[i]:
        heap[heap_min.parent(i)], heap[i] = heap[i], heap[heap_min.parent(i)]
        i = heap_min.parent(i)
    return heap

""" increase the key at index i """
def increase_heap_key(heap, i, key):
    if key < heap[i]:
        exit()
    heap[i] = key
    heap_min.cram_min(heap, i, len(heap))
    return heap

def insert_into_heap(A, key):
    length = len(A) + 1
    A.append(-float('inf'))
    decrease_heap_key(A, len(A) - 1, key)

heap            = [2, 5, 19, 20, 15, 45, 6]
