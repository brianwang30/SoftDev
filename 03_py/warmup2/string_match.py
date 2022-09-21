'''
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
Expected	Run		
string_match('xxcaazz', 'xxbaaz') → 3	3	OK	
string_match('abc', 'abc') → 2	2	OK	
string_match('abc', 'axc') → 0	0	OK	
string_match('hello', 'he') → 1	1	OK	
string_match('he', 'hello') → 1	1	OK	
string_match('h', 'hello') → 0	0	OK	
string_match('', 'hello') → 0	0	OK	
string_match('aabbccdd', 'abbbxxd') → 1	1	OK	
string_match('aaxxaaxx', 'iaxxai') → 3	3	OK	
string_match('iaxxai', 'aaxxaaxx') → 3	3	OK
'''
def string_match(a, b):
  retCount = 0
  counter = 0
  while counter < len(a) - 1 and counter < len(b) - 1:
    if a[counter] == b[counter] and a[counter + 1] == b[counter + 1]:
      retCount += 1
    counter += 1
  return retCount
