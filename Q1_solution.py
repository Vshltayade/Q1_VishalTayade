i = int(input())
count_div = 2
if i < 0:
    print("Please provide a valid positive integer.")
else:
    for x in range(4,i):
        if i % x == 0:
            count_div += 1
    print(count_div)
