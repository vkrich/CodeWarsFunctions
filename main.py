def square_digits(num):
  print([int(i)**2 for i in str(num)])
  return "".join([str(int(i)**2) for i in str(num)])

def iq_test(numbers):    
    numbers_list, counts_odd = [int(i) for i in numbers.split()], 0
    
    for i in range(3):        
      if numbers_list[i] % 2 == 1:
        counts_odd += 1

    for i in range(len(numbers_list)):
      if (counts_odd <= 1 and numbers_list[i] % 2 == 1 
          or counts_odd > 1 and numbers_list[i] % 2 == 0):
        return i+1

def persistence(n):
  answer = 0
  while len(str(n)) > 1:
    answer += 1
    mult = 1
    for i in str(n):
      mult *= int(i)
    n = mult
  return answer

def count_sum(s):
  res = 0
  for i in s:
    res += ord(i)-96
  return res

def high_1(x):
  x = x.lower().split()
  scores = list(map(count_sum, x))
  for i in range(len(scores)):
    if scores[i] == max(scores):
      return x[i]  

def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

def delete_nth(order, max_e): 
  dict_nums, result = {}, [] 
  for i in order:    
    try:
      dict_nums[i] += 1
    except:
      dict_nums[i] = 1

    if dict_nums[i]<=max_e:
      result.append(i)

  return result

reg = """ ^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*\s).{6,}$ """

def primeFactors(n):
  prime_dict = dict()    
  while n > 1:    
    for i in range(2, int(n)+1):
      if n % i == 0:
        n /= i        
        try:
          prime_dict[i] += 1
        except:
          prime_dict[i] = 1
        break
  res = ''
  for i in prime_dict.keys():
    if prime_dict[i] == 1:
      res += f"({i})"
    else:
      res += f"({i}**{prime_dict[i]})"
  return res

print(primeFactors(7775460))