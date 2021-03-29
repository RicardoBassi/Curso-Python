def half(p,q):
    carry = p and q
    sum_ = int((p or q) and not(p and q))
    return (carry , sum_)

def full(r,s,t):
    carry_ = r and s
    sum__ = int((r or s) and not(r and s))
    carry__ = t and sum__
    sum___ = int((t or sum__) and not(t and sum__))
    carry___ = carry_ or carry__
    return(carry___ , sum___)

print( (0,0,0) , full(0,0,0) )
print( (0,0,1) , full(0,0,1) )
print( (0,1,0) , full(0,1,0) )
print( (1,0,0) , full(1,0,0) )
print( (0,1,1) , full(0,1,1) )
print( (1,1,0) , full(1,1,0) )
print( (1,0,1) , full(1,0,1) )
print( (1,1,1) , full(1,1,1) )