def largest_element_in_array(lst:list[int])->int:

    if len(lst)==0:
        return None
    # What is the disadvantage of using 0 as max why cant you use max = 0 initially think about it.
    max = lst[0]
    for i in range(len(lst)):
        if  lst[i]>max:
            max = lst[i]
        #or
        #largest = max(max,lst[i])

    return max

import numpy as np
for i in range(10):
    a = np.random.randint(-2345678,2345678,10)
    print(a)
    print(largest_element_in_array(a))