def longest_consec(strarr, k):
    if len(strarr) == 0 or k<=0 or k > len(strarr):
        return ""
    maxi, ans = 0, ""
    for i in range(len(strarr)-k+1):        
        if len("".join(strarr[i:i+k])) > maxi:            
            maxi = len("".join(strarr[i:i+k]))            
            ans = strarr[i:i+k]        
    return "".join(ans)

def add_zero(n):
    if n < 10:
        return f'0{n}'
    else:
        return n

def make_readable(seconds):    
    return f'{add_zero(seconds//3600)}:{add_zero(seconds%3600//60)}:{add_zero(seconds%60)}'


def check_blocks(block, s):    
  dxy = [-1, 0, 1]
  for i in range(1, 9, 3):        
    temp = []
    for x in dxy:
      for y in dxy:                
          temp.append(block[1 + y][i + x])
    if sum(temp) != s:
      return False
  return True
    
def done_or_not(board):    
    s = sum([ 1, 2, 3, 4, 5, 6, 7, 8, 9 ])
    
    if False in [check_blocks(board[0+i:3+i], s) for i in [0, 3, 6]]:
        return 'Try again!'        
    
    for i in board: #row check
        if len(set(i)) != 9 or sum(i)!=s:
            return 'Try again!'
        
    for i in range(9): #column check
        temp = []
        for j in range(9):
            temp.append(board[j][i])        
        if len(set(temp)) != 9 or sum(temp)!=s:            
            return 'Try again!'
    return 'Finished!'
         
        
print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                  ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                 , [7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                           ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                           ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                           ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]))
'''                           
print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]))
'''

def sum_pairs(ints, s):
  olds = set()    
  for i in range(len(ints)):
    if ints[i] in olds:
      return [s - ints[i], ints[i]]
    olds.add(s-ints[i])
  return None

def solution(args):    
    i, s, temp = 0, '', []
    begin = True
    
    while i<len(args):
      
      temp.append(args[i])       
        
      if i == len(args)-1 or args[i]-args[i+1] != -1:                
            if begin or s[-1] == ',':
                s = s[:-1]
                begin = False 
            
            if len(temp) == 1:
                s += ',' + str(temp[0]) + ','                
                    
            if len(temp) == 2:
                s += ',' + str(temp[0]) + ',' + str(temp[1])+','               
                    
            if len(temp)>2:                 
                s += ',' + str(temp[0]) + '-' + str(temp[-1]) + ','                
               
        temp = []  
                
        i += 1
        
    return s[1:-1]

print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '\n-6,-3-1,3-5,7-11,14,15,17-20')
print(solution([-7,-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '\n-7,-6,-3-1,3-5,7-11,14,15,17-20')
#print(solution([-3,-2,-1,2,10,15,16,18,19,20]), '\n-3--1,2,10,15,16,18-20')
#print(solution([-88,-87,-84,-82,-80,-77,-74,-73,-71,-70,-67,-64,-61,-59,-58,-55]),'\n-88,-87,-84,-82,-80,-77,-74,-73,-71,-70,-67,-64,-61,-59,-58,-55')


