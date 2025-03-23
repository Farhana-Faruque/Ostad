def reverse_string():
    str_input = input()
    str_list = list(str_input)

    left, right = 0, len(str_list) - 1
    
    while left < right:
        str_list[left], str_list[right] = str_list[right], str_list[left]  
        left += 1
        right -= 1

    reversed_str = "".join(str_list)
    print(reversed_str)

reverse_string()
