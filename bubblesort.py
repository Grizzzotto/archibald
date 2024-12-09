s_list = [1,5,4,2,6,8,6,2,4,3]
def bubblesort(start_list):
    bubble = start_list
    while if_sorted(bubble) != 1:
        bubble = bubblesort(sort_list(start_list))
    return start_list

def sort_list(start_list):
    sorted_list = []
    for i in range(len(start_list)-1):
        a = start_list[i]
        b = start_list[i+1]
        if start_list[a] <= start_list[b]:
            sorted_list.append(a)
        else:
            sorted_list.append(b)
    return sorted_list

def if_sorted(start_list):
    for i in range(len(start_list)-1):
        a = start_list[i]
        b = start_list[i+1]
        if a<=b:
            pass
        else:
            return 0
    return 1

print(bubblesort([1,2,3,4,3,2]))
