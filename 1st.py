def calc_sum(n):
    if(n==0 ):
        return 0
    else:
        return calc_sum(n-1) + n
    
print(calc_sum (9))