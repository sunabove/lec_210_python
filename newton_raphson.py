# coding=utf-8

# 입실론 : 아죽 작은 값 
e = 0.00001 

# 함수 정의
def f(x) :
   return x*x - 3*x -100
pass

def derivative(x) :
   der = (f(x + e) - f(x)) / e 
   return der 
pass

def main() : 
    x = 6.0
    y = 1
    index = 0

    while abs(y) >= e :
        y = f(x)  
        print( "[%03d] f(%.20f) = %.20f" % ( index, x, y) )
        x = x - (y / derivative(x))
        index += 1
    pass
pass

if __name__ == '__main__' :   
    main()
pass
