def find_missing_number(list) :
    list.sort()
    n = len(list)

    for i in range(n) :
        if list[i] != i+1 :
            return i+1


numbers = [2,1,4,6,3,5,7,9]

num = find_missing_number(numbers)

print(f"missing number is {num}")