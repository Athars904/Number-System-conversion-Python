number_system = input("Select number numsystem of number of (2,5,8,16,10) base: ")
if number_system == "16":
    num = input("Enter the number: ")
else:
    num = int(input("Enter the number: "))
conversion=input("Enter Number system you want it's base to be changed(2,5,8,16,10): ")
if number_system == "2":
    decimal_num = 0
    m = 1
    length = len(str(num))

    for k in range(length):
        reminder = num % 10
        decimal_num = decimal_num + (reminder * m)
        m = m * 2
        binary_num = int(num/10)
elif number_system == "8":
    decimal_num = 0
    m = 1
    length = len(str(num))

    for k in range(length):
        reminder = num % 10
        decimal_num = decimal_num + (reminder * m)
        m = m * 8
        binary_num = int(num / 10)
elif number_system == "16":
    m = 0
    decimal_num = 0
    numlen = len(num)
    numlen = numlen - 1
    i = 0
    while numlen >= 0:
        rem = num[numlen]
        if rem >= '0' and rem <= '9':
            rem = int(rem)
        elif rem >= 'A' and rem <= 'F':
            rem = ord(rem)
            rem = rem - 55
        elif rem >= 'a' and rem <= 'f':
            rem = ord(rem)
            rem = rem - 87
        else:
            m = 1
            break
        decimal_num = decimal_num + (rem * (16 ** i))
        numlen = numlen - 1
        i = i + 1
elif number_system == "10":
    decimal_num=num
elif number_system == "5":
    decimal_num = 0
    m = 1
    length = len(str(num))

    for k in range(length):
        reminder = num % 10
        decimal_num = decimal_num + (reminder * m)
        m = m * 5
        binary_num = int(num / 10)
else:
    print("INVALID NUMBER SYSTEM")

if conversion == "2":
    binary = 0
    m = 0
    temp = decimal_num


    while (temp > 0):
        binary = ((temp % 2) * (10 ** m)) + binary
        temp = int(temp / 2)
        m += 1
    print("CONVERTED NUMBER in Binary: ", binary)
elif conversion == "5":
   base_5 = 0
   m = 0
   temp = decimal_num
   while temp > 0:
        base_5 = ((temp % 5) * (10 ** m)) +base_5
        temp = int(temp / 5)
        m +=1
   print("CONVERTED NUMBER inbase_5: ", base_5)
elif conversion == "8":
    octal = 0
    m = 0
    temp = decimal_num
    while temp > 0:
        octal = ((temp % 8) * (10 ** m)) + octal
        temp = int(temp / 8)
        m += 1
    print("CONVERTED NUMBER in octal: ", octal)
elif conversion == "16":
    m_dict = {0: '0',
                1: '1',
                2: '2',
                3: '3',
                4: '4',
                5: '5',
                6: '6',
                7: '7',
                8: '8',
                9: '9',
                10: 'A',
                11: 'B',
                12: 'C',
                13: 'D',
                14: 'E',
                15: 'F'}
    m = ''

    while (decimal_num > 0):
        remainder = decimal_num % 16
        m = m_dict[remainder] + m
        decimal_num = decimal_num // 16
    print("number in Hexadecimal number system: " , m)
elif conversion == "10":
    print("Number in decimal number system: ", decimal_num)
else:
    print("INVALID NUMBER SYSTEM")