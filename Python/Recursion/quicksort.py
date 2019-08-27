#Alonso - 12/Oct/2018
                                                                                                                                   
import random

def main():
	print("My Quicksort - Sorted Array: ", myQuicksort([]))
	print("My Quicksort - Sorted Array: ", myQuicksort([3]))
	print("My Quicksort - Sorted Array: ", myQuicksort([1, 3]))
	print("My Quicksort - Sorted Array: ", myQuicksort([3, 1]))
	print("My Quicksort - Sorted Array: ", myQuicksort([3, 1, 4, 2]))
	print("My Quicksort - Sorted Array: ", myQuicksort([3, 1, 4, 3, 2]))
	print("My Quicksort - Sorted Array: ", myQuicksort([7, 2, 4, 8, 3, 5, 9, 1]))

def myQuicksort(arr):
	if len(arr) < 2:
		return arr
	else:
		#Changed the pivot from the first element to a random element of the array to make the algorithm more efficient. On average, it will take O(n log n) time.
		pivot = arr[random.randint(0, len(arr)-1)]
		less = []
		more = []

		arr.remove(pivot)

		for i in arr:
			if(i <= pivot):
				less.append(i)
			else:
				more.append(i)

		return myQuicksort(less) + [pivot] + myQuicksort(more)

main()      