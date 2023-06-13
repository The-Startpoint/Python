# Converts a decimal into binary
def ConvertToBinary(num : int):
    binary = bin(num)[2:]
    return int(binary)

# How to run it
if __name__ == "__main__":
    test = int(input())
    print(ConvertToBinary(test))