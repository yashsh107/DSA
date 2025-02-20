def find_repeating_elements(list) :
    list.sort()
    
    l = []
   
    for i in range(len(list)) :
        if i < len(list) - 1 :
            if list[i] == list[i+1] :
                if list[i] not in l :
                    l.append(list[i])

    return l

numbers = [3,5,7,4,2,4,2,1,9, 9,2]            

res = find_repeating_elements(numbers)

print(res)