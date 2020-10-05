# multiply by 2 = shift left 1, by 4, shift left 2
# divide by 2 = shift right 1, by 4 shift right 2
def main():
    binary = input("Enter an 8-bit binary number: ")
    print("Multiply by 2: ",lshift(binary))
    print("Multiply by 4: ",lshift(lshift(binary)))
    print("Divide by 2: ",rshift(binary))
    print("Divide by 4: ",rshift(rshift(binary)))


def lshift(bina):
    update = ""
    for i in range(7):
        update += bina[i]
    update += "0"
    return update

def rshift(bina):
    update = ""
    if (bina[0] == "1"):
        update = "1" + update
    else:
        update = "0" + update
    for i in range(7):
        update += bina[i]
    return(update)


if __name__ == '__main__':
    main()
