def string_times(str, n):
  if n == 0:
    return ""
  string = ""
  while n > 0:
    string = string + str
    n = n - 1
  return string

def front_times(str, n):
  front = str[:3]
  string = ""
  while n > 0:
    string = string + front
    n = n - 1
  return string

def string_bits(str):
  string = ""
  index = 0
  while index < len(str):
    string += str[index]
    index += 2
  return string

def string_splosion(str):
  string = ""
  index = 1
  while index <= len(str):
    string += str[:index]
    index += 1
  return string

def last2(str):
  last = str[len(str)-2:len(str)]
  retCount = 0
  counter = 0
  
  while counter < len(str)-2:
    if str[counter] == last[0]:
      if str[counter + 1] == last[1]:
        retCount += 1
    counter = counter + 1
    
  return retCount

def array_count9(nums):
  counter = 0
  for e in nums:
    if e == 9:
      counter += 1
  return counter

def array_front9(nums):
  counter = 0
  for e in nums:
    if counter < 4 and e == 9:
      return True
    counter += 1
  return False

def array123(nums):
  counter = 0
  while counter < len(nums):
    if nums[counter] == 1 and len(nums) > counter + 2 and nums[counter + 1] == 2 and nums[counter + 2] == 3:
      return True
    counter += 1
  return False

def string_match(a, b):
  retCount = 0
  counter = 0
  while counter < len(a) - 1 and counter < len(b) - 1:
    if a[counter] == b[counter] and a[counter + 1] == b[counter + 1]:
      retCount += 1
    counter += 1
  return retCount
