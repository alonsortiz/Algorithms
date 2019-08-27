import math 

def main():
	print("Binary decimals for 1:   ", binary(1))
	print("Binary decimals for 2:   ", binary(2))
	print("Binary decimals for 3:   ", binary(3))
	print("Binary decimals for 4:   ", binary(4)) 
	print("Binary decimals for 8:   ", binary(8)) 
	print("Binary decimals for 16:  ", binary(16)) 
	print("Binary decimals for 32:  ", binary(32))  
	print("Binary decimals for 100: ", binary(100)) 


	print("Recursive: Binary decimals for 1:   ", recursiveBinary(1))
	print("Recursive: Binary decimals for 2:   ", recursiveBinary(2))
	print("Recursive: Binary decimals for 3:   ", recursiveBinary(3))
	print("Recursive: Binary decimals for 4:   ", recursiveBinary(4)) 
	print("Recursive: Binary decimals for 8:   ", recursiveBinary(8)) 
	print("Recursive: Binary decimals for 16:  ", recursiveBinary(16)) 
	print("Recursive: Binary decimals for 32:  ", recursiveBinary(32))  
	print("Recursive: Binary decimals for 100: ", recursiveBinary(100)) 
	


def binary(n):
	#decimals = int(math.log(n,2))
	#return decimals+1

	facts = 2
	decimals = 1

	while(facts <= n):
		facts *= 2
		decimals += 1

	return decimals

	

def recursiveBinary(n):
	decimals = 1
	
	if n < 2:
		return decimals
	else:
		return decimals + recursiveBinary(n/2)


main()       