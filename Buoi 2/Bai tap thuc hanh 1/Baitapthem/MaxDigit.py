import sys

def main():
    n = sys.stdin.read().strip()
    max_digit = max(n)
    print(max_digit)

if __name__ == "__main__":
    main()
