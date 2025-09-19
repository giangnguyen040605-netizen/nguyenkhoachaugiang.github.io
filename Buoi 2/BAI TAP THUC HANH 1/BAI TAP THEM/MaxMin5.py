import sys

def main():
    data = sys.stdin.read().strip().split()
    if len(data) < 5:
        print("Nhap 5 so nguyen")
        return
    
    numbers = list(map(int, data[:5]))
    min_val = min(numbers)
    max_val = max(numbers)
    
    print(f"{min_val} {max_val}")

if __name__ == "__main__":
    main()
