# Վարժություն 1.9
>>> def inc(a):
	return a + 1
>>> def dec(a):
	return a - 1


>>> def add1(a, b):
	if a == 0:
		return b
	else:
		return inc(add1(dec(a), b))

>>> def add2(a, b):
	if a == 0:
		return b
	else:
		return add2(dec(a), inc(b))

"""
add1 ֆունկցիան հանդիսանում է ռեկուրսիվ ,իսկ add2-ը պոչավոր ռեկուրսիվ։

    Քանի որ add1-ում կատարվում է հետաձգված գործողություն, ի շնորհիվ այն բանի,
    որ նրա մեջ կանչվում է հենց add1 ֆունկցիան և inc ֆունկցիան սպասում է նրա բազային դեպքին հասնելուն, dec ֆունկցիայի շնորհիվ ։
    
         Իսկ add2-ում ռեկուռսիվ կանչման ժամանակ նույն add2 ֆունկցիային փոխանցվում են պատրաստի արժեքներ,
         որի շնորհիվ չի կատարվում հետաձգված գործողություն։
"""



# Վարժություն 1.10

>>> def ackermann(x, y):
	if y == 0:
		return 0
	elif x == 0:
		return 2 * y
	elif y == 1:
		return 2
	else:
		return ackermann(x - 1, ackermann(x, y - 1))

  
ackermann(1, 5) #--> 32

ackermann(2, 4) #--> 65536

ackermann(3, 3) #--> 65536


>>> def a1(n):
	return ackermann(0, n)
   # վերադարձնում է n-ի կրկնապատիկը։
>>> def a2(n):
	return ackermann(1, n)
   # վերադարձնում է 2-ի n աստիճան։
>>> def a3(n):
	return ackermann(2, n)
   # վերադարձնում է


  
  
  
  
  
  
  
  
