import sys
import math

def main():
    data = sys.stdin.read().strip().split()
    if len(data) != 3:
        print("Nhap 3 so thuc a b c")
        return

    a, b, c = map(float, data)

    if a == 0:
        if b == 0:
            if c == 0:
                print("Unlimited solutions")
            else:
                print("No solution")
        else:
            x = -c / b
            print(f"x1={x:.2f}")
    else:
        delta = b*b - 4*a*c
        if delta < 0:
            print("No solution")
        elif delta == 0:
            x = -b / (2*a)
            print(f"x1={x:.2f}")
        else:
            x1 = (-b - math.sqrt(delta)) / (2*a)
            x2 = (-b + math.sqrt(delta)) / (2*a)
            print(f"x1={x1:.2f}, x2={x2:.2f}")

if __name__ == "__main__":
    main()

