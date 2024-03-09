# Fibonacci Sequence Calculation
def fibonacci_memo(n, memo):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)

    return memo[n]


def fibonacci_tab(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


def main():
    n = int(input("Enter value of n for Fibonacci Sequence Calculations: "))

    # using memoization

    memo = {}

    for i in range(n + 1):
        print(f"F({i}) = {fibonacci_memo(i, memo)}")

    # using tabulations

    print("\n Fibonacci Sequence using Tabulations:")
    for i in range(n + 1):
        print(f"F({i}) = {fibonacci_tab(i)}")


if __name__ == "__main__":
    main()
