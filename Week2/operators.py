"""Operators 
- They perform operations on variables and values

Types of operators: 

1. Arithmetic operators 
    +       Addition
    -       Subtraction
    *       Multiplication
    /       Division 
    %       Modulus  --gives remainder
    **      Exponential
    //      Floor division --divides two numbers and rounds the        result down to the nearest integer
    
2. Assignment operators : assigns values to a variable
   =     x=10       x=10
   +=    x+=4       x=x+3
   -=    x-=4       x=x-4      
   *=    x*=4       x=x*4   
   /=    x/=4       x=x/4
   %=    x%=4       x=x%4
   //=   x//=5      x=x//5
   **=   x**=5      x=x**5
   &=    x&=3       x=x&3
   |=    x|=3       x=x|3
   ^=    x^=3       x=x^3
   >>=   x>>=3      x=x>>3  (shifts )
   <<=   x<<4       
   
3. Comparison operators: 
  ==   Equal
  !=   Not equal
  >    Greater than
  <    Less than
  >=   Greater than or equal to
  <=   Less than or equal to

4. Logical operators
    and
    or 
    not
    
5. Identiy operators
    is
    not
    
6. Membership operators
    in         Returns True if a sequence with the specified value        is present in the object
    not in     Returns True if a sequence with the specified value        is not present in the object
   
   
7. Bitwise operators
   &   AND
   |   OR
   ^   XOR
   ~   NOT
   <<  Zero fill left shift
   >>  Signed right shift
   

"""
x1 = 10
y1 = 3
#arithmetic operators
print (x1/y1)
print (x1%y1)
print (x1//y1)

#comparison operators
print (x1 <12 and x1<15)
print (not(x1 <12 or x1<9))

#identity operators 
print (x is y)
print (x is not y)

""" Precendence 

()	                                      Parentheses	
**                              	      Exponentiation	
+x  -x  ~x	                              Unary plus, unary minus, and bitwise NOT	
*  /  //  %	                              Multiplication, division, floor division, and modulus	
+  -	                                  Addition and subtraction	
<<  >>	                                  Bitwise left and right shifts	
&                               	      Bitwise AND	
^	                                      Bitwise XOR	
|	                                      Bitwise OR	

==  !=  >  >=  <  
<=  is is not                             Comparisons, identity, and membership operators
in not in 	                                                                   	

not	                                      Logical NOT	
and	                                      AND	
or	                                      OR

"""
not	Logical NOT	
and	AND	
or	OR

