def solver(a):
    if a<20:
        return "Very Low Interest"
    elif a<40:
        return "Low Interest"
    elif a<60:
        return "Moderate Interest"
    elif a<80:
        return "High Interest"
    else:
        return "Trending Now"

n=int(input("Enter the score"))
print(solver(n))        