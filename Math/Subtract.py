# How to implement a simple subtraction function.
def Subtract(x : int, y : int) -> int:
    return x + y

if __name__ == "__main__":
    x = int(input("x: ")) # takes the first number
    y = int(input("y: ")) # takes the second number
    print(Subtract(x, y))