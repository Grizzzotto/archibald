s_list = [1,5,4,2,6,8,6,2,4,3]
def bubblesort(start_list):
    while True:
        x = sort_list(start_list)
        if s_list != x:
            x = sort_list(start_list)
        s_list = x
        else:
            return x

def sort_list(start_list):
    i = 0
    sorted_list = start_list
        while (i+1 != len(start_list)):
            a = i
            b = i+1
            if a <= b:
                sorted_list.append(a)

                i+=1
            else:
            i+=1
print(bubblesort(start_list))
