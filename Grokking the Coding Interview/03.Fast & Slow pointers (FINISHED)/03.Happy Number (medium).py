"""
Any number will be called a happy number if, after repeatedly replacing it with a number equal
to the sum of the square of all of its digits, leads us to number ‘1’.
All other (not-happy) numbers will never reach ‘1’.
Instead, they will be stuck in a cycle of numbers which does not include ‘1’.
"""


# determines where stuck of cycle
def find_happy_number(num):
    slow, fast = num, num
    while True:
        slow = find_square_sum(slow)
        # move two steps
        fast = find_square_sum(find_square_sum(fast))
        # found the cycle
        if slow == fast:
            break
    # see if the cycle is stuck on the number '1'
    return slow == 1


# calculates the sum of the squares of the digits of a number
def find_square_sum(num):
    _sum = 0
    while num > 0:
        digit = num % 10
        _sum += digit * digit
        num //= 10
    return _sum


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()
