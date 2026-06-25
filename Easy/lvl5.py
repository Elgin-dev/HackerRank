def find_rising_star(scores):
    n = len(scores)
    best_start = None
    best_peak = -1
    i = 0
    while i < n - 2:
        j = i
        while j + 1 < n and scores[j + 1] > scores[j]:
            j += 1
        run_length = j - i + 1
        if run_length >= 3:
            peak = scores[j]
            if peak > best_peak:
                best_peak = peak
                best_start = i
        i = j + 1 if j > i else i + 1
    if best_start is None:
        print("No rising star")
    else:
        print(f"Day {best_start + 1}")
if __name__ == "__main__":
    scores = list(map(int, input().split()))
    find_rising_star(scores)