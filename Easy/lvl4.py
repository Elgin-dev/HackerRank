def encode_row(scores):
    symbols = []
    for s in scores:
        if s <= 20:
            symbols.append(".")
        elif s <= 50:
            symbols.append("-")
        elif s <= 80:
            symbols.append("+")
        else:
            symbols.append("#")
    return "".join(symbols)
def main():
    categories = ["Tech", "Fashion", "Food"]
    for category in categories:
        scores = list(map(int, input().split()))
        encoded = encode_row(scores)
        print(f"{category}: {encoded}")
if __name__ == "__main__":
    main()