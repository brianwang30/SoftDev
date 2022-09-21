'''
Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
Expected	Run		
array_front9([1, 2, 9, 3, 4]) → True	True	OK	
array_front9([1, 2, 3, 4, 9]) → False	False	OK	
array_front9([1, 2, 3, 4, 5]) → False	False	OK	
array_front9([9, 2, 3]) → True	True	OK	
array_front9([1, 9, 9]) → True	True	OK	
array_front9([1, 2, 3]) → False	False	OK	
array_front9([1, 9]) → True	True	OK	
array_front9([5, 5]) → False	False	OK	
array_front9([2]) → False	False	OK	
array_front9([9]) → True	True	OK	
array_front9([]) → False	False	OK	
array_front9([3, 9, 2, 3, 3]) → True	True	OK	
'''
def array_front9(nums):
  counter = 0
  for e in nums:
    if counter < 4 and e == 9:
      return True
    counter += 1
  return False
