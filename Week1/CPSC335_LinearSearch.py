#Linear Search
#Input: target element : T, List of items : L
#Output: index of T in L or -1 if T is not in L
#(1) for index from 0 to length of L - 1
#(2)    if L[i] is T
#(3)        return i
#(4)  End Loop
#(5) if T not found return -1

def linear_search(L,T):
    for i, element in enumerate(L):
        if element == T:
            return i
    return -1

L = [1,2,3,4,5,6,7,8,9]
T = 5

print(linear_search(L,T))