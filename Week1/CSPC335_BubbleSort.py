#Bubble Sort
#Input: List of numbers: L
#Output: The list L is sorted in descening order
#(1) for i from 0 to length of L -1
#(2)    for j from 0 to length of L - i - 2
#(3)        if L[j] > L[j+1] then
#(4)            swap L[j] with L[i]
#(5)        End if
#(6)    End for
#(7) End for
#(8) return L

def bubble_sort(L):
    n = len(L)
    for i in range(n):
        for j in range(n-i-1):
            if L[j] > L[j + 1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L


#Input
L = [1,5,3,8,4,6,3,9]
print(bubble_sort((L)))






