def DecimalToBinary(num):
    try: num=int(num)
    except: return """

    +=================================+
    | [ERROR] input must be a number! |
    +=================================+
    """
    strs = ""
    while num:
        # if (num & 1) = 1
        if (num & 1):
            strs += "1"
        # if (num & 1) = 0
        else:
            strs += "0"
        # right shift by 1
        num >>= 1
    return strs[::-1]

def operands(operation, num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    if operation == "A":
        result = num1|num2
        return result
    elif operation == "B":
        result = num1|num2
        if result == 1:
            result = 0
        elif result == 0:
            result = 1
        return result
    elif operation == "C":
        result = num1&num2
        return result
    elif operation == "D":
        result = num1&num2
        if result == 1:
            result = 0
        elif result == 0:
            result = 1
        return result
    elif operation == "E":
        result = num1^num2
        return result
    elif operation == "F":
        result = num1^num2
        if result == 0:
            result = 1
        elif result == 1:
            result = 0
        return result
    elif operation == "G":
        result = not num1
        return result


# Driver Code
do = input("""
    +=================================+
    | [INFO] Select one:              |
    | [A] Convert binary to decimal   |
    | [B] Binary operations           |
    +=================================+
""")
while True:
    if do.upper() == "A" or do.upper() == "B":
        break
    do = input("""
    +=================================+
    | [INFO] Select one:              |
    | [INFO] Select one:              |
    | [A] Convert binary to decimal   |
    | [B] Binary operations           |
    +=================================+
""")
if do.upper() == "A":
    num = input("""
    +=================================+
    | [INFO] Input number:            |
    +=================================+
""")
    binary = DecimalToBinary(num)
    print(f"{num} converted to binary is: {binary}")
    exit()
elif do.upper() == "B":
    operation = input("""
    +=================================+
    | [INFO] Select one:              |
    | [A] OR                          |
    | [B] NOR                         |
    | [C] AND                         |
    | [D] NAND                        |
    | [E] XOR                         |
    | [F] XNOR                        |
    | [G] NOT                         |
    +=================================+
""")
    while True:
        if operation.upper() != "A" or operation.upper() != "B" or operation.upper != "C:" or operation.upper != "D:" or operation.upper != "E:" or operation.upper != "F:" or operation.upper != "G:":
            break
        operation = input("""
    +=================================+
    | [INFO] Select one:              |
    | [A] OR                          |
    | [B] NOR                         |
    | [C] AND                         |
    | [D] NAND                        |
    | [E] XOR                         |
    | [F] XNOR                        |
    | [G] NOT                         |
    +=================================+
""")
    if operation.upper() == "A":
        num1 = input("""
    +=================================+
    | [INFO] Input number 1:          |
    +=================================+
""")
        num2 = input("""
    +=================================+
    | [INFO] Input number 2:          |
    +=================================+
""")
        result = operands(operation.upper(), num1, num2)
        print(f"{num1} OR {num2} output in BINARY is: {result}")
    elif operation.upper() == "B":
        num1 = input("""
    +=================================+
    | [INFO] Input number 1:          |
    +=================================+
""")
        num2 = input("""
    +=================================+
    | [INFO] Input number 2:          |
    +=================================+
""")
        result = operands(operation.upper(), num1, num2)
        print(f"{num1} NOR {num2} output in BINARY is: {result}")
    elif operation.upper() == "C":
        num1 = input("""
    +=================================+
    | [INFO] Input number 1:          |
    +=================================+
""")
        num2 = input("""
    +=================================+
    | [INFO] Input number 2:          |
    +=================================+
""")
        result = operands(operation.upper(), num1, num2)
        print(f"{num1} AND {num2} output in BINARY is: {result}")
    elif operation.upper() == "D":
        num1 = input("""
    +=================================+
    | [INFO] Input number 1:          |
    +=================================+
""")
        num2 = input("""
    +=================================+
    | [INFO] Input number 2:          |
    +=================================+
""")
        result = operands(operation.upper(), num1, num2)
        print(f"{num1} NAND {num2} output in BINARY is: {result}")
    elif operation.upper() == "E":
        num1 = input("""
    +=================================+
    | [INFO] Input number 1:          |
    +=================================+
""")
        num2 = input("""
    +=================================+
    | [INFO] Input number 2:          |
    +=================================+
""")
        result = operands(operation.upper(), num1, num2)
        print(f"{num1} XOR {num2} output in BINARY is: {result}")
    elif operation.upper() == "F":
        num1 = input("""
    +=================================+
    | [INFO] Input number 1:          |
    +=================================+
""")
        num2 = input("""
    +=================================+
    | [INFO] Input number 2:          |
    +=================================+
""")
        result = operands(operation.upper(), num1, num2)
        print(f"{num1} XNOR {num2} output in BINARY is: {result}")
    elif operation.upper() == "G":
        num1 = input("""
    +=================================+
    | [INFO] Input number 1:          |
    +=================================+
""")
        result = operands(operation.upper(), num1, "")
        print(f"{num1} NOT {num2} output in BINARY is: {result}")
    exit()