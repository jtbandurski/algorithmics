def binary_search(array, target):
	low = 0
	high = len(array) - 1
	while low != high:
		mid = (low + high) // 2
		if(array[mid] < target):
			low = mid +1
		else:
			high = mid
	return low
		

array = [1,4,5,5,7]
x = 2

print(binary_search(array=array, target=x))
