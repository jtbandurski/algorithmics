import sys

import numpy as np


def paperboy_question_1(n, k, d, persons, start_house, num_papers):
	
	# count number of people in each house
	house_ppl = [0 for _ in range(k)]

	for person in persons:
		house_ppl[person-1] = house_ppl[person-1] + 1

	# calculate cummulative sums of houses in reverse
	# remeber that they are in reverse
	cum_sum = np.flip(np.cumsum(np.flip(house_ppl)))

	# main loop
	output = []
	for i in range(d):
		h = start_house[i]-1
		output.append(max(0, num_papers[i] - cum_sum[h]))
	return output

# binary search which finds index of the first greater or equal number
# if the target is larger than all elements of the list then we get k which is correct for our task
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

def paperboy_question_2(n, k, d, persons, start_house, num_papers):
	# count number of people in each house
	house_ppl = [0 for _ in range(k)]

	# calculate how many people leave in each house
	for person in persons:
		house_ppl[person-1] = house_ppl[person-1] + 1
    
	# prepare output
	output = []

	# calculate cum sums
	cum_sum = np.cumsum(house_ppl)

	# iterate over days
	for i in range(d):
		# if we start at first house we look for first number greater or equal to num_papers
		if start_house[i] == 1:
			target = num_papers[i]
			output.append(binary_search(array=cum_sum, target=target)+1)
		# else we look for the first number greater or equal to num_papers + cum_sum[start_house[i]-2]
		# this is equivalent to paperboy already having enough newspapers to arrive at start_house[i] and starting at 1st house
		else:
			target = num_papers[i] + cum_sum[start_house[i]-2]
			output.append(binary_search(array=cum_sum, target=target)+1)

	return output



# YOU CAN IGNORE THE CODE BELOW



# Set SUBMIT_TO_SZKOPUL=True when submitting
# your solution to the Szkopul webserver.
# Set SUBMIT_TO_SZKOPUL=False in order
# to test your code by reading the input from
# a test file ("input0.txt").
SUBMIT_TO_SZKOPUL = True

if SUBMIT_TO_SZKOPUL:
	reader = sys.stdin
else:
	reader = inputReader = open("input0b.txt","r")
 
# Reads the input
astr = reader.readline().split()
q = int(astr[0])
n = int(astr[1])
k = int(astr[2])
d = int(astr[3])
persons = [int(val) for val in reader.readline().split()]
start_house = [int(val) for val in reader.readline().split()]
num_papers = [int(val) for val in reader.readline().split()]

# Calls your function
if q == 1:
	output = paperboy_question_1(n, k, d, persons, start_house, num_papers)
else:
	output = paperboy_question_2(n, k, d, persons, start_house, num_papers)

# Writes the output
for i in range(d):
	print(output[i], end=' ')
print()