def second_largest(lst: list[int]) -> int:
    first = second = float("-inf")
    
    for num in lst:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second

import numpy as np
# Testing with random generator
for _ in range(3):  
    a = np.random.randint(-23, 23, 10)
    print(f"Array: {a} -> Second Largest: {second_largest(a)}")
