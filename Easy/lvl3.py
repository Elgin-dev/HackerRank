def solver(term):
    total = sum(term)
    avg = total / len(term)
    count = 0
    for score in term:
        if score > 50:
            count += 1
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]

    max_index = term.index(max(term))
    print("Total:", total)
    print("Average:", round(avg, 2))
    print("Days over 50:", count)
    print(f"Best day: {days[max_index]} ({term[max_index]})")


scores = []

for i in range(7):
    scores.append(int(input()))

solver(scores)