'''
Given two int values, return their sum. Unless the two values are the same, then return double their sum.
sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
Expected	Run		
sum_double(1, 2) → 3	3	OK	
sum_double(3, 2) → 5	5	OK	
sum_double(2, 2) → 8	8	OK	
sum_double(-1, 0) → -1	-1	OK	
sum_double(3, 3) → 12	12	OK	
sum_double(0, 0) → 0	0	OK	
sum_double(0, 1) → 1	1	OK	
sum_double(3, 4) → 7	7	OK	
'''
def sum_double(a, b):
  if a == b:
    return 4 * a
  return a + b
