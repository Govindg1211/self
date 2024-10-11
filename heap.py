import heapq

min_heap = []

def add_to_heap(heap, element):
    heapq.heappush(heap, element)
    print(f"Added {element}: {heap}")

def pop_from_heap(heap):
    if heap:
        smallest = heapq.heappop(heap)
        print(f"Removed {smallest}: {heap}")
    else:
        print("Heap is empty!")

def peek_heap(heap):
    if heap:
        print(f"Smallest element is: {heap[0]}")
    else:
        print("Heap is empty!")

add_to_heap(min_heap, 5)
add_to_heap(min_heap, 1)
add_to_heap(min_heap, 3)
add_to_heap(min_heap, 7)

peek_heap(min_heap)

pop_from_heap(min_heap)
pop_from_heap(min_heap)

print(f"Final heap: {min_heap}")