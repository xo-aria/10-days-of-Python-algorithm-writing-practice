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

def s():
    return 1 == 1

print(s())

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