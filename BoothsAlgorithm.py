def main():

    binMulti = input("Enter Multiplier in binary: ") 
    binCand = input("Enter Multiplicand in binary: ") 
    dec1 = binaryToDecimal(binMulti)
    dec2 = binaryToDecimal(binCand)

    product = "0000" + binMulti

    print("Product:", product)

    check = [int(product[7]), 0]
    #For loop runs 4 times in this instance because the most bits it can have is 4
    for i in range(4):
        print(check[0], check[1])
        product = checkPair(product,binCand,check)
        check[1] = check[0]
        check[0] = int(product[7])
    print("{} ({}) * {} ({}) = {}".format(binMulti, dec1, binCand, dec2, product))

#Checks the LSB and the check for the ALGO rules
def checkPair(num, multica,check):
    if (check[0] == 0 and check[1] == 0):
            num = right_shift(num)
    elif (check[0] == 1 and check[1] == 1):
            num = right_shift(num)
    elif (check[0] == 0 and check[1] == 1):
            num = right_shift(add(num, multica))
    elif (check[0] == 1 and check[1] == 0):
            num = right_shift(add(num, twos_compliment(multica)))
    return num

#Adds the left side of the product and the Multiplicand together and updates the product register
def add(prod, cand):
    fourdig, mult = prod[:len(prod)//2],  prod[len(prod)//2:] #splits the product register into two halves
    result = bin(int(fourdig, 2) + (int(cand, 2)))[2:].zfill(4)
    result = result + mult
    if (len(result) == 9):
        result = result[1:]
    print("Add:    ", result)
    return (result)


# Shifts all binary digits to right
def right_shift(num):
    numList = [int(d) for d in str(num)]
    if (numList[0] == 0):
        num = bin(int(num, 2) >> 1)
        num = num[2:].zfill(8)
        print("Shift:  ", num)
        return(num)
    else:
        num = bin(int(num, 2) >> 1)
        num = "1" + num[2:].zfill(7)
        print("Shift:  ", num)
        return (num)


# Convert the multiplicand to Twos Compliment For Subtraction
def twos_compliment(num):
    binary = [int(d) for d in str(num)]
    for i in range(len(num)):
        if (binary[i] == 1):
            binary[i] = 0
        elif (binary[i] == 0):
            binary[i] = 1
    binary = int(''.join(str(i) for i in binary))
    binary = binaryToDecimal(binary)
    binary += 1
    binary = bin(binary)
    if len(binary) == 3:
        binary = 0 + binary
    return (binary[2:].zfill(4))

# Convert Binary To Decimal
def binaryToDecimal(binary):
    binary = str(binary)
    decimal = int(binary, 2)
    return(decimal)


if __name__ == '__main__':
    main()
