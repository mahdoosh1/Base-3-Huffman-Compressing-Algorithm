import sys
import baseconvert
import math
import time
def b_to_b(num,basein,baseout):
    a = time.time()
    decimal_number = int(num, basein)
    res = ""

    while decimal_number > 0:
        remainder = decimal_number % baseout
        res = str(remainder) + res
        decimal_number //= baseout
    b = time.time()
    # print("Result:",res," ",baseconvert.base(num,basein,baseout,string=True),"  Time:",b-a,"   ",time.time()-b)
    return res
def b2_to_b3(inp):
    return b_to_b(str(inp),2,3)
def b3_to_b2(inp):
    return b_to_b(str(inp),3,2)
def count_digits(string):
    counts = {
        "0": 0,
        "1": 0,
        "2": 0
    }
    for digit in string:
        counts[digit] += 1
    return counts
def cmpmost(binary_string): 
    b3 = ("0" * (len(b2_to_b3("1"*len(binary_string))) - len(b2_to_b3(binary_string)))) + b2_to_b3(binary_string)
    dic = count_digits(b3)
    values = list(dic.values())
    values.sort()
    values.reverse()
    if values[0] == dic["0"]:
        most = "0"
    elif values[0] == dic["1"]:
        most = "1"
    elif values[0] == dic["2"]:
        most = "2"
    new_file = ""
    if most == "0":
        nxt = "1"
    else:
        nxt = "0"
    print("Proccess 2")
    for key, val in dic.items():
        if val == values[0]:
            most = key
    for i in b3:
        if i == most:
            new_file = new_file + "0"
        elif i == nxt:
            new_file = new_file + "10"
        else:
            new_file = new_file + "11"
    ln = len(b2_to_b3("1"*len(new_file)))
    ln2 = len(b2_to_b3(new_file))
    new_3 = ("0" * (ln - ln2)) + b2_to_b3(new_file)
    new_3 = most + new_3
    new_2 = b3_to_b2(new_3)
    return "0"+new_2
def cmpbit(inbit):
    b3 = b2_to_b3(inbit)
    if 0 in list(count_digits(b3).values()):
        no = str(list(count_digits(b3).values()).index(0))
    if no == "0":
        use = (1,2)
    else:
        use = (0,str(5-int(no)))
    out = ""
    print("Proccess 2")
    for i in b3:
        if i in use:
            out = out + str(use.index(i))
    return "10"+(b3_to_b2(no+b2_to_b3(out)))
def cmponly(inbit):
    b3 = b2_to_b3(inbit)
    cnt = list(count_digits(b3).values())
    for o in cnt:
        if o != 0:
            only = str(cnt.index(o))
            size = o
    print("Proccess 2")
    return "11"+(b3_to_b2(only+b2_to_b3(b_to_b(size + 1,10,2)[1:])))
def cmpbest(inbit):
    print("Proccess 1")
    cnt = count_digits(b2_to_b3(inbit)).values()
    zr = 0
    for i in cnt:
        zr += 1 if i == 0 else 0
    if zr == 0:
        return cmpmost(inbit)
    if zr == 1:
        return cmpbit(inbit)
    if zr == 2:
        return cmponly(inbit)
    if zr == 3:
        return "0"
aa=b_to_b("1001",2,10)
ab=b_to_b("022",3,10)
ba=b_to_b("1001",2,3)
bb=b_to_b("022",3,2)
if aa == "9":
    if ab == "8":
        if ba == "100":
            if bb == "1000":
                print("Test passed.")
            else:
                print("Test did not pass correctly! this could be due to unsupported version, exiting...")
                exit()
        else:
            print("Test did not pass correctly! this could be due to unsupported version, exiting...")
            exit()
    else:
        print("Test did not pass correctly! this could be due to unsupported version, exiting...")
        exit()
else:
    print("Test did not pass correctly! this could be due to unsupported version, exiting...")
    exit()
sys.set_int_max_str_digits(2000000)
file_path = input("file path to compress: ")
with open(file_path, 'rb') as file:
        binary_data = file.read()
        binary_string = ''.join(format(byte, '08b') for byte in binary_data)
result = cmpbest(binary_string)
print("Proccess 3")
ln = b_to_b(str(8-((len(result)+3)%8)),10,2)
ln = ("0"*(3-len(ln)))+ln
padded_result = result+"0"*(8-((len(result)+3)%8))+ln
def binary_to_file(binary_string, filename):
    # Convert the binary string to bytes
    byte_array = bytearray()
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        byte_value = int(byte, 2)
        byte_array.append(byte_value)
    print("Proccess 4")

    # Write the bytes to a file
    with open(filename, "wb") as f:
        f.write(byte_array)
binary_to_file(padded_result,file_path+".b3h")
print("Done")
input("press enter to exit ...")