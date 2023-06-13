"""
How to get an average value of a list.
1. Add up all values together (31)
2. Divide the total with the amount of values (31 / 9)
3. you've gotten the average grade (3.4)
"""
def GetAverage(numbers : list) -> float:
    avg = sum(numbers) / len(numbers)
    return float(avg)

# For example what's the average grade in the class:
if __name__ == "__main__":
    numlist = [2, 5, 5, 6, 4, 3, 4, 1, 1]
    print(len(numlist), ", ", sum(numlist))
    print(GetAverage(numlist))