def make_palindrome(number_string, k):

    numbers = list(number_string)
    pointer_1 = 0
    pointer_2 = len(number_string) - 1
    counter = 0

    for i in range(len(number_string)):
        if numbers[pointer_1] != numbers[pointer_2]:
            counter += 1
            if numbers[pointer_2] > numbers[pointer_1]:
                # 12345
                numbers[pointer_1] = numbers[pointer_2]
                # 52345
            else:
                # 54321
                numbers[pointer_2] = numbers[pointer_1]
                # 54325
        if counter > k:
            return -1
            break
        pointer_1 += 1
        pointer_2 -= 1

    # maximizing (adding 9's)
    #number_to_maximize = k - counter


    # joining & printing the palindrome
    return ''.join(numbers)
