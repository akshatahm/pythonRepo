
'''
print(lesser_of_two_evens(2,4))			# 2
print(lesser_of_two_evens(2,5))			# 5
'''

def lesser_of_two_evens(n1, n2):
    if both_even(n1,n2) :
        return n1 if n1<n2 else n2
    else:
        return n1 if n1>n2 else n2

def both_even(n1, n2):
    if n1%2==0 and n2%2==0:
        return True
    else:
        return False

#OR

def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)

#############################################
'''
print(animal_crackers('Levelheaded Llama'))      # True
print(animal_crackers('Crazy Kangaroo'))			  # False
'''

def animal_crackers(animal):
    split_val = animal.split(' ')
    first_char = split_val[0][0]
    return_val = True
    #print(f'first char:{first_char}')
    for word in split_val:
        if first_char != word[0]:
            return_val = False
    return return_val

OR

def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]

#############################################
'''
print(makes_twenty(20,10)) 	 # True
print(makes_twenty(12,8))		 # True
print(makes_twenty(2,3))  		 # False
'''
def makes_twenty(n1,n2):
    if n1 ==20 or n2==20 or n1+n2==20:
        return True
    else:
        return False

#OR

def makes_twenty(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20
	
#############################################
'''
print(old_macdonald('macdonald'))  	# 'MacDonald'

'''
def old_macdonald(name):
    split_list =[]
    split1 = name[:3]
    split_list.append(split1)
    split2 = name[3:]
    split_list.append(split2)

    print(split_list)
    result =''
    for s in split_list:
        news = s[0].capitalize()+s[1:]
        result = result +news
    return result

#OR

def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'

#############################################
'''
print(master_yoda('I am home'))    # 'home am I'
print(master_yoda('We are ready'))  # 'ready are We'
'''

def master_yoda(snt):
    ls = snt.split()
    ls.reverse()
    return ' '.join(ls)

# OR

def master_yoda(text):
    return ' '.join(text.split()[::-1])
	
#############################################
'''
print(has_33([1, 3, 3]))    # True
print(has_33([1, 3, 1, 3]))    # False
print(has_33([3, 1, 3]))   # False
'''
def has_33(ls):
  prev = -1
  for i in ls:
    if i==prev==3:
        return True
    prev = i
  return False
        
#############################################
'''
print(paper_doll('Hello')) # 'HHHeeellllllooo'
print(paper_doll('Mississippi')) # 'MMMiiissssssiiippppppiii'
'''
def paper_doll(inp):
  res = ''
  for n in inp:
      res = res + 3*n
  return res
      
#############################################
'''
print(blackjack(5,6,7))  # 18
print(blackjack(9,9,9))  # 'BUS'
print(blackjack(9,9,11)) # 19
'''

def blackjack(i1, i2, i3):
  sum = i1 + i2 + i3
  #print(sum)
  if sum <= 21:
      return sum
  else:
      if i1 == 11 or i2==11 or i3==11:
          sum = sum -10
      if sum > 21:
          return 'BUS'
      else:
          return sum

#############################################
'''
print(summer_69([1, 3, 5])) # 9
print(summer_69([4, 5, 6, 7, 8, 9])) # 9
print(summer_69([2, 1, 6, 9, 11])) # 14
'''
def summer_69(ls):
  sum =0
  ls1 =[]
  for i in ls:
      if i<6 or i>9:
          ls1.append(i)
  print(ls1)
  for ii in ls1:
      sum = sum + ii
  return sum

#############################################

