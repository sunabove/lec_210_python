import logging
logging.basicConfig(
    format='%(levelname)-8s %(asctime)s %(filename)s %(lineno)d %(message)s',
    level=logging.DEBUG
    )

def sum_between_two_number( x, y ) :  
    import xlsxwriter
    workbook = xlsxwriter.Workbook('sum_data.xlsx')
    worksheet = workbook.add_worksheet()

    t = x
    x = min( t, y )
    y = max( t, y ) 
    sum = 0
    row = 0 
    worksheet.write(row, 0, "x" )
    worksheet.write(row, 1, "sum" )
    row += 1

    x_array = []
    y_array = []
    for x in range( x, y + 1 ):
        sum = sum + x 
        x_array.append( x )
        y_array.append( sum )
        worksheet.write(row, 0, x )
        worksheet.write(row, 1, sum )
        row += 1
        logging.debug( " current x = %s, sum = %s" % ( x, sum ) )
    pass

    import matplotlib.pyplot as plt
    import matplotlib as mpl
    import numpy as np
    plt.plot(x_array, y_array)
    plt.show()

    worksheet.write(row, 0, "sum" )
    worksheet.write(row, 1, sum ) 
    workbook.close()

    import matplotlib.pyplot as plt
    import matplotlib as mpl
    import numpy as np

    return sum
pass

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
sum = sum_between_two_number( x, y )

print ( sum )