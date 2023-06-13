# How to get the Area of a circle
def GetCircleArea(radius : int) -> float:
    PI = 3.14
    return PI * pow(radius, 2)

if __name__ == "__main__":
    r = int(input("radius: ")) # takes the radius
    print(GetCircleArea(r))