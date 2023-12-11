unsorted_list = [14,27,8,-42,11,35,-9,56,25]
# this one displays unsorted list
print(unsorted_list)

def selection_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        min_index = i
        for j in range(i+1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j
        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]
    return unsorted_list

unsorted_list = [14,27,8,-42,11,35,-9,56,23]
sorted_list = selection_sort(unsorted_list)
print(sorted_list)
