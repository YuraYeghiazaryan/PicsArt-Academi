# ստուգում է val, էլեմենտ պարունակվում է լիստում, թե ոչ
def contain(data, val):
  if val in data:
    return 'Yes'
  return 'No'

lst1 = [6,4,0]
lst2 = [2, 2, 3 ]



contain(lst1, 0)
#contain(lst2, 9)

# /////////////////////////

# եթե արգումենտ չի փոխանցվել, այսինքն i-ին վերագրվել է None արժեքը, ջնջում է վերջին անդամը, 
# հակառակ դեպքում ջնջում է i-րդ ինդեքսում գտնվող անդամը, և անդամը վերադարձվում է որպես արդյունք

def pop(lst,i = None):
 if i == None:
   y = lst[len(lst)-1]
   del lst[len(lst)-1] 
   return y
 else:
   y = lst[i]
   del lst[i]
   return y

lst1 = [2, 5, 6, 3, 9]
pop(lst1)

# /////////////////////
# ջնջում է data-ում եղած բոլոն անդամները, որոնց արժեքը հավասար է value-ին (իրականացնելիս կարող եք օգտվել remօve մեթոդից)

def remove_all(data, value):
  for i in data:
    if i == value:
      data.remove(value)

lst1 = [2, 5, 7, 4, 9, 5]

remove_all(lst1,5)
print(lst1)

# //////////////////

# շրջում է data-ն հակառակ դասավորությամբ

def reverse(data):
  return data[::-1]

lst1 = [2, 5, 7, 4, 9, 5]
reverse(lst1)

# ///////////////////
# վերադարձնում է data-ի ամենափոքր անդամը

def min(data):
  if len(data) == 0:
    return 'List is empty'
  min = data[0]
  for i in data:
    if i < min:
      min = i 
  return min    

lst1 = [5, 4, 7, 9, 2, 6] 
min(lst1)

#////////////////////
# երադարձնում է data-ի ամենամեծ անդամը

def max(data):
  if len(data) == 0:
    return 'List is empty'
  max = data[0]
  for i in data:
    if i > max:
      max = i 
  return max    

lst1 = [5, 4, 7, 9, 2, 6] 
max(lst1)

