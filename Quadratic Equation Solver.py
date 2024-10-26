import math
def quadratic_equation_Solver():
    try:
        a=float(input("enter the first number here: "))
        b=float(input("enter the second number here: "))
        c=float(input('enter the third number here: '))
    
        d=float(0)
        d=b*b-4*a*c
   
    
        if d>=0:
            d=math.sqrt(d)
            root_a=(-b+d)/2*a     
            root_b=(-b-d)/2*a
            print("the first root is:",root_a)
            print('the second root is:',root_b)
            

        elif d<0:
            print("please enter real numbers")
            
        
    except:
        print('please enter valid real numbers')
    return root_a,root_b
  

while True:
    quadratic_equation_Solver()
