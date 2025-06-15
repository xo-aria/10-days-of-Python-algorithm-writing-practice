import random

def hi(texts):
    texts_dict = {}
    for i, text in enumerate(texts):
        texts_dict[i] = text
    random_text = random.choice(list(texts_dict.keys()))
    return texts_dict[random_text]

print(hi(
    [
        "Hi",
        "Hello"
    ]
))

# i get an code from AI for learn
# -------

def s():
    return 1 == 1

print(s())

# this is a small code for test Boolean
# -------

def list_sum(li):
    final_sum = 0
    for l in li:
        final_sum = l + final_sum
    return final_sum

print(list_sum([1,2,3])) # 6
li = [
    'Ford',
    'BMW',
    'Dodge',
    '1',
]
li.sort()
print(li)

# So, Strings sorted by alphabet and number sorted by eighter and combinate this is, numbers - strings.
# -------

def sort_without_same_values_for_lists(l1, l2):
    merge_list = []
    for i in l1:
        merge_list.append(i)
    for j in l2:
        merge_list.append(j)
    final_list = list(set(merge_list))
    final_list.sort()
    return final_list

print(sort_without_same_values_for_lists([1, 2, 3], [4, 0, 6, 6, 2, 3]))

# this is just for test and debug day 5
# -------

def climb_stairs(n):
    if n <= 2:
        return n
    else:
        return climb_stairs(n-1)+climb_stairs(n-2)
    
climb_stairs(40)

# i find a code on stackoverflow and thinking on it. ( https://stackoverflow.com/a/72854792/22076615 )
# omg.. that is so hard! XD

def climbStairs(self, n: int) -> int:
    one,two=1,1
    for i in range(n-1):
        one,two=two,one+two
    return two

# and finally I find a fast code for doing this practice today. ( https://stackoverflow.com/a/73200894/22076615 )

# but i have problem in code
def climbStairs(n: int) -> int:
    one = 1
    two = 1
    for i in range(n-1):
        one = two
        two = one + two
    return two

print(climbStairs(40))

# because this print 549755813888 but i want 165580141 and i got this is for varibales! and updated code:
def climbStairs(n: int) -> int:
    one, two = 1, 1
    for i in range(n-1):
        one, two = two, one + two
    return two
# -------

