'''
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
Expected	Run		
has22([1, 2, 2]) → True	True	OK	
has22([1, 2, 1, 2]) → False	False	OK	
has22([2, 1, 2]) → False	False	OK	
has22([2, 2, 1, 2]) → True	True	OK	
has22([1, 3, 2]) → False	False	OK	
has22([1, 3, 2, 2]) → True	True	OK	
has22([2, 3, 2, 2]) → True	True	OK	
has22([4, 2, 4, 2, 2, 5]) → True	True	OK	
has22([1, 2]) → False	False	OK	
has22([2, 2]) → True	True	OK	
has22([2]) → False	False	OK	
has22([]) → False	False	OK	
has22([3, 3, 2, 2]) → True	True	OK	
has22([5, 2, 5, 2]) → False	False	OK	
other tests
OK
'''

def has22(nums):
  flag = False
  for e in nums:
    if e == 2 and flag == True:
      return True
    if e == 2:
      flag = True
    else:
      flag = False
    
  return False
