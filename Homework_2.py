#1.8 վարժություն
def sqrt3 ( m ):
  n=1
  while not guess_enough( n , m ):
             n = improve( m , n )
  return ndef guess_enough( n , m ):
   return abs( m**3 - n ) <= 0,001def improve ( x , y ):
   return ( x / y**2 + 2*y) / 31.8 վարժություն
def sqrt3 ( m ):
  n=1
  while not guess_enough( n , m ):
             n = improve( m , n )
  return n
def guess_enough( n , m ):
   return abs( m**3 - n ) <= 0,001
def improve ( x , y ):
   return ( x / y**2 + 2*y) / 3
