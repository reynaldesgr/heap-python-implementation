import heap_max

""" return the max of the priority file"""
def get_max_heap(heap):
    return heap[0]

""" extract the max from the heap and return (heap, max)"""
def extract_max_from_heap(heap, length):
    if length < 1:
        exit()
    max = get_max_heap(heap)
    heap[0] = heap[length - 1]
    heap = heap[:len(heap) - 1]
    heap_max.cram_max(heap, 0, len(heap))
    return heap, max

""" increase the key at index i """
def increase_heap_key(heap, i, key):
    if key < heap[i]:
        exit()
    heap[i] = key
    while i >= 0 and heap[heap_max.parent(i)] < heap[i]:
        heap[heap_max.parent(i)], heap[i] = heap[i], heap[heap_max.parent(i)]
        i = heap_max.parent(i)
    return heap

""" insert a key into the heap """
def insert_into_heap(A, key):
    length = len(A) + 1
    A.append(-float('inf'))
    increase_heap_key(A, len(A) - 1, key)

heap            = [2, 5, 19, 20, 15, 45, 6]
priority_queue  = heap_max.create_heap_max(heap)
heap, max       = extract_max_from_heap(priority_queue, len(priority_queue))
up_heap         = increase_heap_key(heap, 3, 30)
insert_into_heap(up_heap, 20)
