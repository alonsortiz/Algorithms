#Alonso - 10/Oct/2018
#The Euclidean Algorithm is a technique for quickly finding the GCD of two integers.
#Recall that the Greatest Common Divisor (GCD) of two integers A and B is the largest integer that divides both A and B.
def main():
	myEuclidean(270, 192)

def myEuclidean(a, b):
	if a%b == 0:
		print('Euclidean Algorithm: ', a/b)
		return a/b
	else:
		myEuclidean(b, a%b)

main()