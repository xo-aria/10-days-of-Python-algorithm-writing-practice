# Solution 1 ( not recommended )
"""
def climb_stairs(n):
    if n <= 2:
        return n
    else:
        return climb_stairs(n-1)+climb_stairs(n-2)
    
print(climb_stairs(40))
"""

# Solution 2 ( recommended )
def climbStairs(n: int) -> int:
    one, two = 1, 1
    for i in range(n-1):
        one, two = two, one + two
    return two

print(climbStairs(40)) # 165580141