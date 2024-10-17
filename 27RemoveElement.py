class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        total_elements = len(nums)
        total_correct_elements = 0
        total_incorrect_elements =0
        count = 0
        while count < (total_elements - total_incorrect_elements) :

            if nums[count] == val:
                nums.pop(count)
                total_incorrect_elements += 1

            else:
                total_correct_elements += 1
                count += 1
        return total_correct_elements
    
    def removeElementOptimised(self, nums: list[int], val: int) -> int:
        next_correct_element = 0  
        for count in range(len(nums)):
            if nums[count] != val: # We will never be overwrting values because we will be at the current value, or skipping a value if incorrect
                nums[next_correct_element] = nums[count] #Put our value in the location for the next correct element
                next_correct_element +=1 
        return next_correct_element

# Test cases
s = Solution()
print(s.removeElement([0,1,2,2,3,0,4,2], 3)) 