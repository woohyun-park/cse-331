import numpy as np

def binToHexStr(block):
    DIC = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

    result = ""
    for each in binToBlock(block):
        if each in DIC.keys():
            result = result + DIC[each]
        else:
            result = result + str(each)
    return result

def binToBlock(bin):
    result = []
    temp = "".join(str(i) for i in list(np.transpose(bin).ravel()))
    return hexToBlock(hex(int(temp, 2))[2:]);

def hexToBlock(hex):
    result = []
    dic = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    for each in hex:
        if each in dic.keys():
            result.append(dic[each])
        else:
            result.append(int(each))
    return result