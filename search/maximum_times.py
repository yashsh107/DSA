def maximum_times(list) :
    list.sort()

    max_count = 0
    count = 0

    for i in range(len(list)) :
        count = 1
        for j in range(len(list)) :
            if i!=j and list[i] == list[j] :
                count += 1

        if count > max_count :
            max_count = count
            max_repeated_number = list[i]        

    print(f"Maximum repeated number is {max_repeated_number}, repeated times {max_count}")     


num = [3,2,1,2,2,3,2,1,3]
maximum_times(num)

