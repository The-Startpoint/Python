# Converts a decimal into a hexdecimal

def ConvertToHex(num : int, shorten : bool = True):
    hex_number = hex(num)
    if shorten is True:
        # Removes the "0x" prefix
        hex_number = hex_number[2:]  
        
    return int(hex_number, 16)

# How to run it
if __name__ == "__main__":
    test = int(input())
    print(ConvertToHex(test, False))