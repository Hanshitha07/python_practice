if __name__ == '__main__':
    arr = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])

    # Step 1: Find the minimum score
    min_score = arr[0][1]
    for pair in arr:
        if pair[1] < min_score:
            min_score = pair[1]

    # Step 2: Remove all students with the lowest score
    arr2 = []
    for pair in arr:
        if pair[1] != min_score:
            arr2.append(pair)

    # Step 3: Find the second lowest score
    second_min = arr2[0][1]
    for pair in arr2:
        if pair[1] < second_min:
            second_min = pair[1]

    # Step 4: Collect all names with second lowest score
    result_names = []
    for pair in arr2:
        if pair[1] == second_min:
            result_names.append(pair[0])

    # Step 5: Sort names alphabetically (manual bubble sort)
    n = len(result_names)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result_names[j] > result_names[j + 1]:
                # swap
                temp = result_names[j]
                result_names[j] = result_names[j + 1]
                result_names[j + 1] = temp

    # Step 6: Print names
    for name in result_names:
        print(name)

    
    

        
