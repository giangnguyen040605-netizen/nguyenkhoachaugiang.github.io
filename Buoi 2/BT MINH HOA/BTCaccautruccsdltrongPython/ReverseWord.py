if __name__ == "__main__":
    with open("ReverseWord.inp", "r", encoding="utf-8") as f:
        n = int(f.readline().strip())
        lines = [f.readline().strip() for _ in range(n)]

    results = []
    for line in lines:
        words = line.split()
        words.reverse()
        results.append(" ".join(words))

    with open("ReverseWord.out", "w", encoding="utf-8") as f:
        for r in results:
            f.write(r + "\n")