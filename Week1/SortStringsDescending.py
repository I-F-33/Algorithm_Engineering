
def sortList(L):
    n = len(L)
    for i in range(n):
        for j in range(n - i - 1):
            # if the length of the string at index j is greater than the string at index j+1 then swap
            if len(L[j]) < len(L[j+1]):
                L[j], L[j+1] = L[j+1], L[j]
            # if the strings at index j and j+1 are the same length then sort alphabetically
            elif len(L[j]) == len(L[j+1]):
                if L[j] < L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j]
    return L


#Input
list1 = ["zoo", "apple", "amazing", "banana", "computer", "boxes"]
list2 = ["hello", "hi", "goodbye", "farewell", "friend", "no"]

print('sorted list 1:', sortList(list1))
print('sorted list 2:', sortList(list2))
