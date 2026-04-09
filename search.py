def binary_search(lst, item):
    low = 0
    high = len(lst)-1
    while(low<=high):

        mid = (low+high)//2

        if (lst[mid]==item):
            return mid
        elif (lst[mid]<item):
            low = mid+1
        else:
            high = mid-1
    return None

lst = [12,32,34,56,78,98,900]
target_idx = binary_search(lst,32)
print(target_idx)


