def check_sorted_array(lst:list[int])->bool:
    if len(lst)<=1:
        return True
    for i in range(len(lst)):
        if lst[i]>lst[i+1]:
            return False
    return True
import numpy as np
# Testing Data using Numpy random int array generator
for i in range(10):
    a = np.random.randint(-23,23,10)
    print(a)
    print(check_sorted_array(a))
