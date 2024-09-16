def prumer(list1):
    if len(list1) != 0:
        all = 0
        for cislo in list1:
            all += cislo
        prumer = all/(len(list1))
        return(prumer)
    else:
        return('error')

print(prumer([4,2,4,2,115]))
print(prumer([1,1,1,1,1,1]))
print(prumer([99]))
print(prumer([0,1,2,3,-1,-2,-3, 9]))
print(prumer([]))



