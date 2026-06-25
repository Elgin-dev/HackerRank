def longest_streak(months_data):
    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    yearly_avg = sum(months_data) / len(months_data)

    best_start = best_end = -1
    best_len = 0
    best_avg = 0

    i = 0
    while i < 12:
        if months_data[i] > yearly_avg:
            start = i
            streak_sum = 0
            count = 0

            while i < 12 and months_data[i] > yearly_avg:
                streak_sum += months_data[i]
                count += 1
                i += 1

            end = i - 1
            streak_avg = streak_sum / count

            if count > best_len or (count == best_len and streak_avg > best_avg):
                best_len = count
                best_avg = streak_avg
                best_start = start
                best_end = end
        else:
            i += 1

    print(f"Yearly avg: {yearly_avg:.2f}")
    print(
        f"Longest streak: {months[best_start]} to {months[best_end]}"
    )
    print(f"({best_len} months, avg {best_avg:.2f})")


# Input
data = list(map(int, input().split()))

longest_streak(data)