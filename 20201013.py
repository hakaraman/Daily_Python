"""
Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.
"""

def div(x, y):  
    sign = -1 if ((x < 0) ^ (y < 0)) else 1    
    x, y = abs(x) , abs(y)    
    q = 0
    while (x >= y):  
        x -= y 
        q += 1      
    return sign * q

def d(x, y, r=0, c=1): 
    return r if x < y else d(x-y, y, r+c, c)    


def div3(dividend, divisor): 
      
    sign = (-1 if((dividend < 0) ^ (divisor < 0)) else 1)     
    # remove sign of operands 
    dividend = abs(dividend) 
    divisor = abs(divisor) 
      
    # Initialize 
    # the quotient 
    quotient = 0
    temp = 0
      
    # test down from the highest  
    # bit and accumulate the  
    # tentative value for valid bit 
    for i in range(31, -1, -1): 
        if (temp + (divisor << i) <= dividend): 
            temp += divisor << i
            quotient |= 1 << i
      
    return sign * quotient


def div1(x, y):
    sign = -1 if ((x < 0) ^ (y < 0)) else 1  
    x, y = abs(x) , abs(y)  
    quotient = 0
    power = 32           # Assume 32-bit integer
    yPower = y << power  # Initial y^d value is y^32
    remainder = x        # Initial remainder is x
    while remainder >= y:
        while yPower > remainder:
            yPower >>= 1
            power -= 1
        quotient += 1 << power
        remainder -= yPower
    return sign * quotient

# Driver code 
a = 10
b = 3
print(div(a, b)) 
print(d(a,b))
print(div1(a,b))
a = 43
b = -8
print(div(a, b)) 
print(div1(a,b))