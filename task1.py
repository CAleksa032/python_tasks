starting_point = 1000
end_point = 3000
divisible_with = 9
not_multiple_of = 5

tmp_list = []

for index in range(starting_point, end_point):
    if (index % divisible_with == 0) and (index % not_multiple_of != 0):
        tmp_list.append(index)

for index, item in enumerate(tmp_list):
    print(item, end='')
    if index < len(tmp_list) - 1:
        print(', ', end='')

print()