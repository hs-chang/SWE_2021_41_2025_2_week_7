from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    
    
    length = len(nums)
    i=0
    stop = False
    while (i<length):
        j=i+1
        while (j<length):
            if (nums[i]+nums[j]==target): 
                stop = True
                break
            j += 1
        if stop:
            break
        i += 1
    
    answer = [i,j]
    
    return answer

