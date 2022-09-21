'''
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
Expected	Run		
sum67([1, 2, 2]) → 5	5	OK	
sum67([1, 2, 2, 6, 99, 99, 7]) → 5	5	OK	
sum67([1, 1, 6, 7, 2]) → 4	4	OK	
sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]) → 2	2	OK	
sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]) → 2	2	OK	
sum67([2, 7, 6, 2, 6, 7, 2, 7]) → 18	18	OK	
sum67([2, 7, 6, 2, 6, 2, 7]) → 9	9	OK	
sum67([1, 6, 7, 7]) → 8	8	OK	
sum67([6, 7, 1, 6, 7, 7]) → 8	8	OK	
sum67([6, 8, 1, 6, 7]) → 0	0	OK	
sum67([]) → 0	0	OK	
sum67([6, 7, 11]) → 11	11	OK	
sum67([11, 6, 7, 11]) → 22	22	OK	
sum67([2, 2, 6, 7, 7]) → 11	11	OK	
other tests
OK
'''

def sum67(nums):
  flag = False
  summ = 0
  for e in nums:
    if e == 6:
      flag = True
    elif e == 7 and flag == True:
      flag = False
    elif flag == False:
      summ += e
  return summ
