
# Algorithmic Efficiency & Recursion Toolkit (AERT)

class StackADT:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# ---------------- Factorial ----------------
def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n-1)


# ---------------- Fibonacci ----------------
fib_naive_calls = 0
fib_memo_calls = 0

def fib_naive(n):
    global fib_naive_calls
    fib_naive_calls += 1

    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)


def fib_memo(n, memo={}):
    global fib_memo_calls
    fib_memo_calls += 1

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)

    return memo[n]


# ---------------- Tower of Hanoi ----------------
def hanoi(n, source, auxiliary, destination, stack):
    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        stack.push(move)
        return

    hanoi(n-1, source, destination, auxiliary, stack)
    move = f"Move disk {n} from {source} to {destination}"
    stack.push(move)
    hanoi(n-1, auxiliary, source, destination, stack)


# ---------------- Binary Search ----------------
def binary_search(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid-1)
    else:
        return binary_search(arr, key, mid+1, high)


# ---------------- Main Test Runner ----------------
def main():
    print("----- FACTORIAL -----")
    for n in [0,1,5,10]:
        print(f"{n}! =", factorial(n))

    print("\n----- FIBONACCI -----")
    for n in [5,10,20,30]:
        global fib_naive_calls, fib_memo_calls

        fib_naive_calls = 0
        result_naive = fib_naive(n)

        fib_memo_calls = 0
        result_memo = fib_memo(n, {})

        print(f"\nn = {n}")
        print("Naive Result:", result_naive, "Calls:", fib_naive_calls)
        print("Memo Result :", result_memo, "Calls:", fib_memo_calls)

    print("\n----- TOWER OF HANOI (N=3) -----")
    stack = StackADT()
    hanoi(3, "A", "B", "C", stack)

    while not stack.is_empty():
        print(stack.pop())

    print("\n----- BINARY SEARCH -----")
    arr = [1,3,5,7,9,11,13]
    tests = [7,1,13,2]

    for key in tests:
        index = binary_search(arr, key, 0, len(arr)-1)
        print(f"Search {key} -> Index:", index)

    empty = []
    print("Search in empty list:", binary_search(empty, 5, 0, len(empty)-1))


if __name__ == "__main__":
    main()
