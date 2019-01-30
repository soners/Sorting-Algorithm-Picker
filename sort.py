import numpy as np


# choosing first element as pivot ( not optimized )
def quick_sort(arr):
    less = []
    pivot_list = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivot_list.append(i)
        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivot_list + more

def partition(a, low, high):
    pivot = a[high]
    index = low
    for i in range(low, high):
        if a[i] <= pivot:
            temp = a[i]
            a[i] = a[index]
            a[index] = temp
            index = index + 1

    temp = a[high]
    a[high] = a[index]
    a[index] = temp

    return index


def insertion_sort_aux(arr, low, n):
    for i in range(low+1, n):
        value = arr[i]
        j = i
        while j > low and arr[j - 1] > value:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = value
        
def insertion_sort(arr):
    insertion_sort_aux(arr, 0, len(arr))

def count_sort(arr):

    max_element = max(arr)
    min_element = min(arr)

    length = max_element - min_element + 1

    fill = [0 for i in range(length)]

    for num in arr:
        insert = num - min_element
        fill[insert] += 1

    arr = []
    for i in range(length):
        for j in range(fill[i]):
            arr.append(i + min_element)

    return arr
        
RADIX = 10        
def radix_sort_nonneg(lst):
    last_iteration = False
    radix_power = 1
    while not last_iteration:
        buckets = [[] for _ in range(RADIX)]
        last_iteration = True
        for el in lst:
            digit = el % (radix_power*RADIX) // radix_power
            buckets[digit].append(el)
            if el >= radix_power*RADIX:
                last_iteration = False

        lst = [el for bucket in buckets for el in bucket]
        radix_power *= RADIX
    return lst


def radix_sort(lst):
    positive_ints = radix_sort_nonneg( x for x in lst if x >= 0)
    negative_ints = radix_sort_nonneg(-x for x in lst if x <  0)
    return [-x for x in reversed(negative_ints)] + positive_ints
        
        
def merge_sort_aux2(source, target, source_offset, target_offset, range_length):
    if range_length < 2:
        return

    half_range_length = range_length // 2

    merge_sort_aux2(target, source, target_offset, source_offset, half_range_length)
    merge_sort_aux2(target, source, target_offset + half_range_length, source_offset + half_range_length, range_length - half_range_length)

    left_run_index = source_offset
    right_run_index = source_offset + half_range_length

    left_run_bound = right_run_index
    right_run_bound = source_offset + range_length

    target_index = target_offset

    while left_run_index < left_run_bound and right_run_index < right_run_bound:
        if source[right_run_index] < source[left_run_index]:
            target[target_index] = source[right_run_index]
            right_run_index += 1
        else:
            target[target_index] = source[left_run_index]
            left_run_index += 1

        target_index += 1

    while left_run_index < left_run_bound:
        target[target_index] = source[left_run_index]
        target_index += 1
        left_run_index += 1

    while right_run_index < right_run_bound:
        target[target_index] = source[right_run_index]
        target_index += 1
        right_run_index += 1


def merge_sort_aux(array, from_index, to_index):
    range_length = to_index - from_index
    aux = []
    i = from_index

    while i < to_index:
        aux.append(array[i])
        i += 1

    merge_sort_aux2(aux, array, 0, from_index, range_length)
    
def merge_sort(arr):
    merge_sort_aux(arr, 0, len(arr))
                   
def heapify(arr, n, i): 
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
  
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        heapify(arr, n, largest) 
  
def heap_sort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 