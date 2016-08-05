def make_palindrome(number_string, k):

    numbers = list(number_string)
    pointer_1 = 0
    pointer_2 = len(number_string) - 1
    counter = 0

    for i in range(len(number_string)):
        if numbers[pointer_1] != numbers[pointer_2]:
            counter += 1
            new_val = max(numbers[pointer_1], numbers[pointer_2])
            numbers[pointer_1], numbers[pointer_2] = new_val, new_val
        if counter > k:
            return -1
        pointer_1 += 1
        pointer_2 -= 1

    # maximizing (adding 9's)
    # number_to_maximize = k - counter
    # if number_to_maximize > 1:
    #     pointer_1 = 0
    #     pointer_2 = len(number_string) - 1
    #     if numbers[pointer_1] != '9':
    #         numbers[pointer_1] = '9'
    #         numbers[pointer_2] = '9'

    # joining & printing the palindrome
    return ''.join(numbers)
