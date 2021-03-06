"""
Nick is standing next to a staircase that leads to his apartment.
The staircase has n total steps; Nick knows he can climb anywhere between 1 and m steps in one jump.
He thinks about how many ways there are to climb this staircase.
He realizes it is a big number since there are a lot of possible combinations.
So, he has asked you to write an algorithm for him that tells him the number of possible ways
to climb a staircase given n (number of steps) and, m (number of steps covered in biggest jump).
"""


# Solution 1: Simple recursion
def staircase(n, m):
    # base case of when there is no stair
    if n == 0:
        return 1
    ways = 0
    # iterate over number of steps, we can take
    for i in range(1, m + 1):
        # if steps remaining is smaller than the jump step, skip
        if i <= n:
            # recursive call with n i units lesser where i is the number of steps taken here
            ways += staircase(n - i, m)
    return ways


print(staircase(4, 2))


# Solution 2: Recursion with memoization
def nthStair(n, m, memo):
    if n == 0:  # base case of when there is no stair
        return 1
    if n in memo:  # before recursive step check if result is memoized
        return memo[n]
    ways = 0
    for i in range(1, m + 1):  # iterate over number of steps, we can take
        # if steps remaining is smaller than the jump step, skip
        if i <= n:
            # recursive call with n i units lesser where i is the number of steps taken here
            ways += nthStair(n - i, m, memo)
            # memoize result before returning
    memo[n] = ways
    return ways


def staircase(n, m):
    memo = {}
    # helper function to add memo dictionary to function
    return nthStair(n, m, memo)
