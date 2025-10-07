import re

if __name__ == "__main__":
    # Đọc input
    with open("WordHistogram.inp", "r", encoding="utf-8") as f:
        n = int(f.readline().strip())
        sentences = [f.readline().strip().lower() for _ in range(n)]

    # Gom tất cả từ lại, bỏ dấu chấm phẩy ?!,-...
    words = []
    for sentence in sentences:
        tokens = re.split(r"[ ,.!?\-]+", sentence)
        words.extend([w for w in tokens if w != ""])

    # Đếm tần số xuất hiện
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1

    # In ra theo thứ tự xuất hiện ban đầu (stable dict)
    with open("WordHistogram.out", "w", encoding="utf-8") as f:
        for w in freq:
            f.write(f"{w}: {freq[w]}\n")
