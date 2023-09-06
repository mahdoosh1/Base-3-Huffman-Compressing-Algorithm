def b_to_b(num,basein,baseout):
    # a = time.time()
    if num == '':
        return '0'
    decimal_number = int(num, basein)
    res = ""

    while decimal_number > 0:
        remainder = decimal_number % baseout
        res = str(remainder) + res
        decimal_number //= baseout
    # b = time.time()
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
def demost(inbit):
    b3 = b2_to_b3(inbit)
    most = b3[0]
    nxt = str(max(1-int(most),0))
    otr = "2" if most in ["0","1"] else "1"
    b2 = b3_to_b2(b3[1:])
    out3 = ""
    for idx in range(len(b2)):
        if b2[idx]=="0":
            out3 = out3+most
        elif b2[idx+1]=="0":
            out3 = out3+nxt
        elif b2[idx+1]=="1":
            out3 = out3+otr
    return b3_to_b2(out3)
def debit(inbit):
    b3 = b2_to_b3(inbit)
    nt = b3[0]
    a = str(max(1-int(nt),0))
    b = "2" if nt in ["0","1"] else "1"
    data = b3[1:]
    out3 = ""
    for bit in data:
        if bit == "0":
            out3 = out3 + a
        elif bit == "1":
            out3 = out3 + b
    return b3_to_b2(out3)
def deonly(inbit):
    b3 = b2_to_b3(inbit)
    only = b3[0]
    size = b3_to_b2(b3[1:])
    out3 = only * (int("1"+size,2)-1)
    return b3_to_b2(out3)
def decompress(inbit):
    if inbit[0]=="0":
        demost(inbit[1:])
    elif inbit[1]=="0":
        debit(inbit[2:])
    else:
        deonly(inbit[2:])
outs = []
for i in range(2**8-1):
    try:
        outs.append(decompress(b_to_b(i,10,2))
    except:
        outs.append("?")
for i in outs:
    print(i)
