#Description: Program that sorts phone book entries provided by the user

import pandas as pd

def stripFormatting(number):
    """Remove formatting characters from a phone number."""
    return ''.join(filter(str.isdigit, number))

def padWithZeros(number,length):
    """Pad the number with leading zeroes to match the specified format."""
    return number.zfill(length)

def findMaxLength(numbers):
    """Find the maximum length of numbers in the list."""
    return max(len(number) for number in numbers)

def countingSortByDigit(numbers, digitPosition, radix=10):
    """Sort the numbers based on the digit at the specified position using Counting Sort."""
    output = [0] * len(numbers)
    count = [0] * radix
    #We can count the occurences of each digit at digitPosition

    for number in numbers:
        index = int(number[digitPosition]) if digitPosition < len(number) else 0
        count[index] += 1

    #Counted values Accumulation
    for i in range(1, radix):
        count[i] += count[i-1]

    for number in reversed(numbers):
        index = int(number[digitPosition]) if digitPosition < len(number) else 0

        output[count[index]-1] = number
        count[index] -= 1

    return output

def radixSort(numbers):
    """Sort the numbers using radix sort."""
    maxLength = findMaxLength(numbers)
    for digitPosition in range(maxLength - 1, -1, -1):
        numbers = countingSortByDigit(numbers, digitPosition)
    return numbers

def preprocessPhoneNumbers(phoneNumbers):
    """Preprocess the list of phone numbers by Standardizing their format"""
    standardizedNumbers = [stripFormatting(number) for number in phoneNumbers]
    maxLength = findMaxLength(standardizedNumbers)

    return [padWithZeros(number, maxLength) for number in standardizedNumbers]


def main():
    n = int(input("Enter the phone numbers, you want to record: "))

    rawPhoneNumbers = [input(f"Enter phone number {i+1}: ") for i in range(n)]

    #Step 1: Preprocess on the raw numbers provided by the user
    standarizedNumbers = preprocessPhoneNumbers(rawPhoneNumbers)

    #Step 2: Sorting of teh raw numbers
    sortedNumbers = radixSort(standarizedNumbers)

    #Display Sorted Numbers
    print("\nSorted Numbers")
    for number in sortedNumbers:
        print(number)


if __name__ == "__main__":
    main()













