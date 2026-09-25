#A recursive function is a function that calls itself to solve a problem by breaking it into smaller versions of the same problem.
# It stops when it reaches a base case.import time


def factorial(n):
    if n == 0:      # Base case
        return 1

    return n * factorial(n - 1)   # Recursive call

print(factorial(5))  #120 is the o/p bcz it is factorial of 5! like 5*4*3*2*1


import time
def countdown(n):
    # Base case
    if n == 0:
        print("🎉 Happy New Year!")
        return

    print(n)

    # Wait for 1 second
    time.sleep(1)

    # Recursive call
    countdown(n - 1) #formula

# Function call
countdown(5)


'''
countdown(5) prints 5 and calls countdown(4).
countdown(4) prints 4 and calls countdown(3).
countdown(3) prints 3 and calls countdown(2).
countdown(2) prints 2 and calls countdown(1).
countdown(1) prints 1 and calls countdown(0).
countdown(0) prints 🎉 Happy New Year! and stops because of the base case.
'''