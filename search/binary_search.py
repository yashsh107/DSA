def binary_search(list, value) :
    low_index = 0
    high_index = len(list) - 1

    # mid_index = (low_index + high_index)//2 
    
    while low_index <= high_index :
        mid_index = (low_index + high_index)//2 
        if list[mid_index] == value :
            return mid_index
        elif list[mid_index] < value :
            low_index = mid_index + 1
        else :
            high_index = mid_index - 1
    return -1            


numbers = [1, 3, 5, 7, 9, 11, 15, 18, 20]
search_value = 7
result = binary_search(numbers, search_value)

if result == -1 :
    print("Element not found")
else :
    print(f"Element found at index {result}")    

