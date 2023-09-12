import random

example_list = [random.randint(0, 100) for _ in range(15)]

num_zeros = random.randint(1, 5)  # Adjust the number of zeros as needed
for _ in range(num_zeros):
    position = random.randint(0, 14)  # Assuming a list of 15 elements
    example_list[position] = 0

print("List before adjustment: ", example_list)

non_zeros = [num for num in example_list if num != 0]
zeros_count = len(example_list) - len(non_zeros)
example_list = non_zeros + [0] * zeros_count

print("List after adjustment: ", example_list)

'''
Lets analyze the following solution: 
def solution(nums):
for i in nums:
    if 0 in nums:
        nums.remove(0)
        nums.append(0)
return nums

this solution is wrong for two reasons: 
    1. List is being modified as we iterate through it so we can get unexpected behaviour
    2. Since remove operation is O(n) and it is nested in the for loop full time complexity would be
        O(n^2) and this task can be solved in lower time complexity as I provided.
'''