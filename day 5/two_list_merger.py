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