# This sort_without_same_values_for_lists is the same as day 5.
def sort_without_same_values_for_lists(l1, l2):
    merge_list = []
    for i in l1:
        merge_list.append(i)
    for j in l2:
        merge_list.append(j)
    final_list = list(set(merge_list))
    final_list.sort()
    return final_list

def get_maximum_subarray_from_a_list(li):
    merge_list = []
    for i in li:
        merge_list.append(i)
    final_list = list(set(merge_list))
    final_list.sort()
    maximum_value = final_list[-1]
    return maximum_value

print(get_maximum_subarray_from_a_list([1,2,3,4,64]))

# ---------------

def get_maximum_subarray_from_two_list(l1,l2):
    sorted_list = sort_without_same_values_for_lists([1, 2, 3], [4, 0, 6, 6, 2, 3])
    final_list = sorted_list[-1]
    return final_list

print(get_maximum_subarray_from_two_list([1, 2, 3], [4, 0, 6, 6, 2, 3]))