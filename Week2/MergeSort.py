#PsuedoCode for Merge sort
#Divide -> Conquer -> Combine
def mergeSort(array):
# --checking if the array has more than one element, if it does, it needs sorting,
# --if not then its already sorted
    if len(array) > 1:
#       --Find the midpoint of array
        mid = len(array) // 2
#       --Create left sublist and assigning first half
        L = array[:mid]
#       --Create right sublist anf assign second half
        R = array[mid:]
#       --Recursively applies Mergesort to the left sublist
        mergeSort(L)
#       --Recursively applies Mergesort to the right sublist
        mergeSort(R)

#       --Three pointers
#       -- i , current index for the left index
#       -- j , for the current index of right sublist
#       -- k , for the current index of main array
    i = j = k = 0
#       --Continue the loop as long as there are elements ihe subarrays
    while i < len(L) and j < len(R):
#       --Check if the current element in the left sublist is less than the current element in the right sublist
        if L[i] < R[j]:
#           --place the smaller element in the main array at the starting index
            array[k] = L[i]
#           --increment the left index pointer to the next index
            i += 1
        else:
#           --Place the current element from from right sublist
            array[k] = R[j]
#           --moves pointer in the right sublist
            j += 1
#       --Increment the main array pointer to the next slot
        k += 1

#   -- will handle the scenario when one sublist is exhausted before the other
#   -- will copy the remaining elements from L or R into the main array
    while i < len(L):
        array[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        array[k] = R[j]
        k += 1
        j += 1



#
#
#
