# How to implement a simple addition function.
def Add(x : int, y : int) -> int:
    return x + y

if __name__ == "__main__":
    x = int(input("x: ")) # takes the first number
    y = int(input("y: ")) # takes the second number
    print(Add(x, y))