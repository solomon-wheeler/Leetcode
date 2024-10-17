class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        location_in_1 = -1
        while len(nums2) > 0 and location_in_1 <  len(nums1) - 1:
            location_in_1 += 1
            while len(nums2) != 0 and nums1[location_in_1] > nums2[0]:
                nums1.insert(location_in_1,nums2.pop(0))
                location_in_1 += 1



        if len(nums2) > 0:
            nums1.extend(nums2)

          

        print(nums1)

test_solution = Solution()

## Test cases
import random

def generate_sorted_list(size, start=0, end=100):
    return sorted(random.sample(range(start, end), size))

# Generate two sorted lists
m = 5
n = 3
nums1 = generate_sorted_list(m)  
nums2 = generate_sorted_list(n)

print("Before merge:")
print("nums1:", nums1)
print("nums2:", nums2)

# Create an instance of Solution and call the merge method
test_solution = Solution()
test_solution.merge(nums1, m, nums2, n)

print("After merge:")
print("nums1:", nums1)
