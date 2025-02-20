#find 3 elements in array whose sum is equal to given element

def three_element_sum(list, y) :
    list.sort()
    n = len(list)

    for i in range(n-2) :
        for j in range(i+1, n-1) :
            for k in range(j+1, n) :
                if list[i] + list[j] + list[k] == y :
                    return f"Three numbers are: {list[i]}, {list[j]}, {list[k]}"
    return "Not found"


numbers = [1, 6, 45, 3, 10, 18]

result = three_element_sum(numbers, 22)

print(result)
