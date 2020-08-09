# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

# 아스키 코드로 박스 그리기

box = '''
╔════════════════════════════╗
║                            ║
╠════════════════════════════╣
║                            ║
╚════════════════════════════╝
'''

box = box.strip()
lines = box.split( "\n" )

print()

console_width = int( 119/3 )*3
cell_width = int(console_width / 3)

def empty_line( txt = "" ) :
    width = console_width
    line = txt.center( width, " " )

    return line
pass

def hor_line( txt = "" ) :
    width = console_width
    line = txt.center( width, "═" )

    return line
pass

def line(i, txt ="") :
    width = console_width - 2

    line = lines[ i ]

    line = line[ 0 ] + txt.center(width, line[1]) + line[ -1]

    return line
pass

def cell(txt ="") :
    width = int( console_width/4  - 1 )

    import re
    kor = re.sub('[^가-힣]', '', txt)

    t = len( kor )

    width -= t

    line = lines[ 1 ]

    line = line[ 0 ] + txt.center( width, line[1] ) + line[ -1]

    return line
pass

def top_line() :
    return line( 0, "" )
pass

def content_line(*txt) :
    txt_new = [""]*4

    if txt and len( txt ) > 0 and type( txt[0] ) == list :
        txt = txt[ 0 ]
    pass

    for i, t in enumerate(txt):
        txt_new[i] = t
        if i == 3 :
            break
        pass
    pass

    a = txt_new[0]
    b = txt_new[1]
    c = txt_new[2]
    d = txt_new[3]

    return cell( a )[ 0 : -1 ] + cell( b )[ 0 : -1 ] + cell(c)[0:-1] + cell(d)
pass

def middle_line() :
    return line( 2, "" )
pass

def bottom_line() :
    return line( 4, "")
pass

print()
print( hor_line() )
print()
print( empty_line( "구구단표") )
print( hor_line() )

for page in range( 2 ) :
    print( top_line() )
    col = [ 2 + page*4, 6 + page*4 ]
    print( content_line( [ f"{t}단" for t in range( col[0], col[1] ) ] ) )
    print( middle_line() )
    for r in range( 0, 9 ) :
        t = [ f"{c}x{r+1} = {c*(r+1):2d}" for c in range( col[0], col[1] ) ]
        print( content_line( t ) )
    pass
    print(bottom_line())
pass

print()

