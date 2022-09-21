'''
Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
Expected	Run		
sum13([1, 2, 2, 1]) → 6	6	OK	
sum13([1, 1]) → 2	2	OK	
sum13([1, 2, 2, 1, 13]) → 6	6	OK	
sum13([1, 2, 13, 2, 1, 13]) → 4	4	OK	
sum13([13, 1, 2, 13, 2, 1, 13]) → 3	3	OK	
sum13([]) → 0	0	OK	
sum13([13]) → 0	0	OK	
sum13([13, 13]) → 0	0	OK	
sum13([13, 0, 13]) → 0	0	OK	
sum13([13, 1, 13]) → 0	0	OK	
sum13([5, 7, 2]) → 14	14	OK	
sum13([5, 13, 2]) → 5	5	OK	
sum13([0]) → 0	0	OK	
sum13([13, 0]) → 0	0	OK	
other tests
OK
'''

def sum13(nums):
  flag = False
  summ = 0
  for e in nums:
    if e == 13:
      flag = True
    elif flag == True:
      flag = False
    else:
      summ += e
  return summ
