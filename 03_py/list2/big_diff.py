'''
Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8
Expected	Run		
big_diff([10, 3, 5, 6]) → 7	7	OK	
big_diff([7, 2, 10, 9]) → 8	8	OK	
big_diff([2, 10, 7, 2]) → 8	8	OK	
big_diff([2, 10]) → 8	8	OK	
big_diff([10, 2]) → 8	8	OK	
big_diff([10, 0]) → 10	10	OK	
big_diff([2, 3]) → 1	1	OK	
big_diff([2, 2]) → 0	0	OK	
big_diff([2]) → 0	0	OK	
big_diff([5, 1, 6, 1, 9, 9]) → 8	8	OK	
big_diff([7, 6, 8, 5]) → 3	3	OK	
big_diff([7, 7, 6, 8, 5, 5, 6]) → 3	3	OK	
other tests
OK
'''

def big_diff(nums):
  minn = 999999
  maxx = -999999
  for e in nums:
    minn = min(minn, e)
    maxx = max(maxx, e)
  return maxx - minn
