#Alonso - 12/Oct/2018
#D&C
#Sum all elements of an array in an iterative and recursive way
def main():
	print('***ITERATIVE***')
	print('[1, 2, 3, 4]: ', iterateSum([1, 2, 3, 4]))

	print('\n***RECURSIVE***')
	print('[]:           ', recursiveSum([]))
	print('[1]:          ', recursiveSum([1]))
	print('[3, 4]:       ', recursiveSum([3, 4]))
	print('[1, 2, 3, 4]: ', recursiveSum([1, 2, 3, 4]))

def iterateSum(arr):
	total = 0
	for x in arr:
		total += x
	return total

def recursiveSum(arr):
	if not arr:
		return 0
	elif len(arr) == 1:
		return arr[0]
	else:
		return arr[0] + recursiveSum(arr[1:])

'''
public static List<ProcessInstanceStep> reversedList(List<ProcessInstanceStep> unordered, List<ProcessInstanceStep> ordered) {
        Integer lastPos = unordered.size()-1;
        if(unordered.size() == 0) {
            return ordered;
        } else {
            ordered.add(unordered[lastPos]);
            unordered.remove(lastPos);
            return reversedList(unordered, ordered);
        }
    }
'''


main()