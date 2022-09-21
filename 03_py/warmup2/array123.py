'''
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
Expected	Run		
array123([1, 1, 2, 3, 1]) → True	True	OK	
array123([1, 1, 2, 4, 1]) → False	False	OK	
array123([1, 1, 2, 1, 2, 3]) → True	True	OK	
array123([1, 1, 2, 1, 2, 1]) → False	False	OK	
array123([1, 2, 3, 1, 2, 3]) → True	True	OK	
array123([1, 2, 3]) → True	True	OK	
array123([1, 1, 1]) → False	False	OK	
array123([1, 2]) → False	False	OK	
array123([1]) → False	False	OK	
array123([]) → False	False	OK
'''
def array123(nums):
  counter = 0
  while counter < len(nums):
    if nums[counter] == 1 and len(nums) > counter + 2 and nums[counter + 1] == 2 and nums[counter + 2] == 3:
      return True
    counter += 1
  return False
