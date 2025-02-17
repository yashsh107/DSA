def check_dublicate_number(list) :
    for i in range(len(list)) :
        for j in range(i+1, len(list)) :
            if list[i] == list[j] :
                return "Dublicate number exists"
            j += 1
        i += 1
    return "Dublicate number doesn't exists"



numbers = [13,2,10,20,10,22,32]

result = check_dublicate_number(numbers)

print(result)
        