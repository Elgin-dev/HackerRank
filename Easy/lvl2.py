def solver(a,b,t1,t2):
    diff = t1-t2
    if t1==t2:
        return "Equal"
    elif diff<30:
        return "Minor differnce"
    else:
        return "Major difference"
a=str(input("Enter the first term"))
t1=int(input("Enter the first score"))
b=str(input("Enter the second term"))
t2=int(input("Enter the second score"))
print(solver(a,b,t1,t2))            


