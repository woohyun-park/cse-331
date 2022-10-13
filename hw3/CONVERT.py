import numpy as np

def decBlock_to_hexStr(block):
    DIC = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

    result = ""
    for each in block:
        if each in DIC.keys():
            result = result + DIC[each]
        else:
            result = result + str(each)
    return result

def hexStr_to_decBlock(hex):
    result = []
    dic = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    for each in hex:
        if each in dic.keys():
            result.append(dic[each])
        else:
            result.append(int(each))
    return result

def decBlock_to_BinBlock(block, row, col):
    result = []
    for each in block:
        temp = [int(d) for d in str(bin(each))[2:]]
        while len(temp) < 4:
            temp.insert(0, 0)
        result.append(temp)
    return np.transpose(np.array(result).ravel().reshape(row, col))

def binBlock_to_decBlock(bin):
    result = []
    temp = "".join(str(i) for i in list(np.transpose(bin).ravel()))
    temp = hex(int(temp, 2))[2:]
    while len(temp) < 4:
        temp = "0" + temp
    return hexStr_to_decBlock(temp);