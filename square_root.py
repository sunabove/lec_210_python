import math
class SquareRoot :
    def find_square_root(self, x ) :
        e = 0.0001 
        y = e 

        while abs( y*y - x ) > e :
            y += e
            print( "y = %s" % y ) 
        pass
        
        return y
    pass
pass

print( "find a square root")
s = SquareRoot()
y = s.find_square_root( 4 ) 
print( "square root = %s" % y )