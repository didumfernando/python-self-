#Q12
def denary_to_hex(number):
    conversion_table = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    hexa =''
    while number > 0:
        remainder = number % 16
        hexa = conversion_table[remainder] + hexa
        hexa = hexa // 16

    return hexa

#Q13
def randomnumber(start,end):
    number = random.randint(start,end)
    return number

#Q14
def createIPv4():
    number1 = randomnumber(0,255)
    number2 = randomnumber(0,255)
    number3 = randomnumber(0,255)
    number4 = randomnumber(0,255)
    ipv4 = str(number1) + "." + str(number2) + "." + str(number3) + "." + str(number4)
    return ipv4

#Q15
def storeIPv4(n):
    count = 0
    list_ipv4 = []
    while count <= n:
        ipv4_gen = createIPv4()
        list_ipv4 = list_ipv4 + ipv4_gen
    return list_ipv4

#Q16
def createIPv6():
    number1 = randomnumber(0,65535)
    hex1 = denary_to_hex(number1)

    number2 = randomnumber(0,65535)
    hex2 = denary_to_hex(number1)

    number3 = randomnumber(0,65535)
    hex3 = denary_to_hex(number1)

    number4 = randomnumber(0,65535)
    hex4 = denary_to_hex(number1)

    number5 = randomnumber(0,65535)
    hex5 = denary_to_hex(number1)

    number6 = randomnumber(0,65535)
    hex6 = denary_to_hex(number1)

    number7 = randomnumber(0,65535)
    hex7 = denary_to_hex(number1)

    number8 = randomnumber(0,65535)
    hex8 = denary_to_hex(number1)

    ipv6 = str(hex1) + ":" + str(hex2) + ":" + str(hex3) + ":" + str(hex4) + ":" + str(hex5) + ":" + str(hex6) + ":" + str(hex7) + ":" + str(hex8)
    
    return ipv6

#Q17
def createMAC():
    mac1 = denary_to_hex(randomnumber(0,255))
    mac2 = denary_to_hex(randomnumber(0,255))
    mac3 = denary_to_hex(randomnumber(0,255))
    mac4 = denary_to_hex(randomnumber(0,255))
    mac5 = denary_to_hex(randomnumber(0,255))
    mac6 = denary_to_hex(randomnumber(0,255))

    mac = str(mac1) + ":" + str(mac2) + ":" + str(mac3) + ":" + str(mac4) + ":" + str(mac5) + ":" + str(mac6)

#Q18
print("Option 1: Create an IPv4 address")
print("Option 2: Create an IPv6 address")
print("Option 3: Create a MAC address")
option = input("Please select options 1/2/3:")
if option not in "123":
    option = input("Re-enter option in 1/2/3:")
if option == "1":
    print(createIPv4())
if option == "2":
    print(createIPv6())
if option == "3":
    print(createMAC())

    



    
    
    

    
    
