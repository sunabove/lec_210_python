import logging
logging.basicConfig(
    format='%(levelname)-8s %(asctime)s %(filename)s %(lineno)d %(message)s',
    level=logging.DEBUG
    )

def sum_between_two_number( x, y ) : 
    t = x
    x = min( t, y )
    y = max( t, y ) 
    sum = 0
    for x in range( x, y + 1 ):
        sum = sum + x 
        logging.debug( " current x = %s, sum = %s" % ( x, sum ) )
    pass

    return sum
pass

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
sum = sum_between_two_number( x, y )

print ( sum )