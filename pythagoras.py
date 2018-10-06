import math

def find_pythagoras():
    for x in range( 1, 101 ): 
        for y in range( 1, 101 ):  
            real_z = math.sqrt( x*x + y*y ) 
            z = int( real_z )
            if z == real_z and z < 101 : 
                print( "x = %s, y= %s, z= %s" %(x, y, z) )
            pass
        pass
    pass
pass

find_pythagoras()