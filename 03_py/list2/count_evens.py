'''
Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
Expected	Run		
count_evens([2, 1, 2, 3, 4]) → 3	3	OK	
count_evens([2, 2, 0]) → 3	3	OK	
count_evens([1, 3, 5]) → 0	0	OK	
count_evens([]) → 0	0	OK	
count_evens([11, 9, 0, 1]) → 1	1	OK	
count_evens([2, 11, 9, 0]) → 2	2	OK	
count_evens([2]) → 1	1	OK	
count_evens([2, 5, 12]) → 2	2	OK	
other tests
OK
'''

def count_evens(nums):
  counter = 0
  for e in nums:
    if e % 2 == 0:
      counter += 1
  return counter
