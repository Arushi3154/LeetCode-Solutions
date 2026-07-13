class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # This pointer tracks the next position to write a non-val element
        k = 0
        
        # Iterate through the entire array
        for i in range(len(nums)):
            # If the current element is not the target value
            if nums[i] != val:
                # Move it to the front at index k
                nums[k] = nums[i]
                # Advance the k pointer
                k += 1
                
        # k represents the total number of elements not equal to val
        return k
