def max_value(list1):
    max = list1[0]

    for x in list1[1:]:
        if x > max:
            max = x

    return max


list1 = [1, 2, 3, 4, 20, 6, 88, 8, 9, 10]
print(max_value(list1))
