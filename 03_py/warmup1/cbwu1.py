def sleep_in(weekday, vacation):
  return (not weekday) or vacation

def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

def sum_double(a, b):
  if a == b:
    return 4 * a
  return a + b

def diff21(n):
  if n > 21:
    return 2*(n - 21)
  return 21 - n

def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)

def makes10(a, b):
  return a == 10 or b == 10 or (a + b) == 10

def near_hundred(n):
  return abs(100-n) <= 10 or abs(200-n) <= 10

def pos_neg(a, b, negative):
  if negative:
    return a < 0 and b < 0
  return (a > 0 and b < 0) or (a < 0 and b > 0)

def not_string(str):
  if len(str) > 2 and str[:3] == 'not':
    return str
  return 'not ' + str

def missing_char(str, n):
  return str[:n] + str[n+1:len(str)]

def front_back(str):
  if len(str) <= 1:
    return str
  first_char = str[0]
  last_char = str[len(str)-1]
  if len(str) == 2:
    return last_char + first_char
  return last_char + str[1:len(str)-1] + first_char

def front3(str):
  if len(str) < 3:
    firstChars = str
  firstChars = str[:3]
  return firstChars + firstChars + firstChars
