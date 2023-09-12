starting_point = 1000
end_point = 3000
divisible_with = 9
not_multiple_of = 5
for i in range(starting_point, end_point):
    if (i % divisible_with == 0) and (i % not_multiple_of != 0):
        print(i, end=', ')
