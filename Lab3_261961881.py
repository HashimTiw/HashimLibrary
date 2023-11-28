#Q1
import random
import time

def perform_bubble_sort(array):
    length = len(array)

    for i in range(length):

        is_swapped = False

        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:

                array[j], array[j + 1] = array[j + 1], array[j]
                is_swapped = True

        if not is_swapped:
            break

input_list = [64, 34, 25, 12, 22, 11, 90]
print("Original List:", input_list)

perform_bubble_sort(input_list)

print("Sorted List:", input_list)


#Q2
def merge_sort(arr):
    if len(arr) > 1:

        mid_index = len(arr) // 2

        left_subarray = arr[:mid_index]
        right_subarray = arr[mid_index:]

        merge_sort(left_subarray)
        merge_sort(right_subarray)

        i = j = k = 0

        while i < len(left_subarray) and j < len(right_subarray):
            if left_subarray[i] < right_subarray[j]:
                arr[k] = left_subarray[i]
                i += 1
            else:
                arr[k] = right_subarray[j]
                j += 1
            k += 1

        while i < len(left_subarray):
            arr[k] = left_subarray[i]
            i += 1
            k += 1

        while j < len(right_subarray):
            arr[k] = right_subarray[j]
            j += 1
            k += 1


input_sequence = [38, 27, 43, 3, 9, 82, 10]
print("Original Sequence:", input_sequence)

merge_sort(input_sequence)

print("Sorted Sequence:", input_sequence)

#Q3

def calculate_sorting_duration(sort_function, array_size):
    array = [random.randint(1, 10000) for _ in range(array_size)]
    start_time = time.time()
    sort_function(array)
    end_time = time.time()
    return end_time - start_time

array_sizes = [100, 1000, 10000]

print(f"{'Array Size':<10} {'Bubble Sort Time':<20} {'Merge Sort Time':<20}")

for size in array_sizes:
    time_bubble_sort = calculate_sorting_duration(perform_bubble_sort, size)
    time_merge_sort = calculate_sorting_duration(merge_sort, size)
    print(f"{size:<10} {time_bubble_sort:<20.6f} {time_merge_sort:<20.6f}")
