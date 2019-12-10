sorting definition:
sorting is an algorithm that arranges the elements of a list in a certain order (either ascending or descending, as per the requirement). The output is simply a permutation of the input data.

Types of sorting:
•	Bubble Sort
•	Selection Sort
•	Insertion Sort
•	Merge Sort
•	Heap Sort
•	Quick Sort
•	Sorting in Python
Bubble Sort:
This simple sorting algorithm iterates over a list, comparing elements in pairs and swapping them until the larger elements "bubble up" to the end of the list, and the smaller elements stay at the "bottom".
Example program:
def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_dlist_of_nums)
print(random_list_of_nums)
Selection Sort:
This algorithm segments the list into two parts: sorted and unsorted. We continuously remove the smallest element of the unsorted segment of the list and append it to the sorted segment.
Example program:
def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
random_list_of_nums = [12, 8, 3, 20, 11]
selection_sort(random_list_of_nums)
print(random_list_of_nums)
Merge Sort:
This divide and conquer algorithm splits a list in half, and keeps splitting the list by 2 until it only has singular elements.
Example program:
b=[int(x) for x in input().split()]
	c=len(b)
	e=(len(b))//2
	d=b[0:e]
	n=b[e:c]
	x=d+n
	print(sorted(x))
 
Quick Sort:
This divide and conquer algorithm is the most often used sorting algorithm covered in this article. When configured correctly, it's extremely efficient and does not require the extra space Merge Sort uses. We partition the list around a pivot element, sorting values around the pivot.
Example program:
def partition(nums, low, high):# chosen or created.
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    
    def _quick_sort(items, low, high):
        if low < high:
             split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

random_list_of_nums = [22, 5, 1, 18, 99]
quick_sort(random_list_of_nums)
print(random_list_of_nums)






