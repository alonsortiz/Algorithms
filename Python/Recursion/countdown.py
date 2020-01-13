def main():
	countdown(5)

def countdown(i):
	print(i)
	if i==0:
		return
	else:
		countdown(i-1)

main()

#https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/tutorial/
#https://dev.to/s_awdesh/double-pivot-quick-sort--javas-default-sorting-algorithm-1m4
#https://dev.to/s_awdesh/timsort-fastest-sorting-algorithm-for-real-world-problems--2jhd
