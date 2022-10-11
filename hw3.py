import numpy as np

def babyr_enc(block, key):
    round_keys = [
        [6, 11, 5, 13],
        [6, 5, 3, 8],
        [1, 14, 2, 6],
        [7, 13, 5, 11],
        [0, 3, 5, 8],
    ]
    result = [4, 7, 15, 8]
    print(result)

    result = babyr_enc_help(result, round_keys[1], 1)
    print(result)
    result = babyr_enc_help(result, round_keys[2], 1)
    print(result)
    result = babyr_enc_help(result, round_keys[3], 1)
    print(result)
    result = babyr_enc_help(result, round_keys[4], 0)
    print(result)


def babyr_enc_help(block, key, flag):
    temp = np.array(block).copy()
    print(temp) # 4 7 f 8
    temp = fs(temp) 
    print(temp) # 8 c d 5
    temp = fa(temp)
    print(temp)
    if flag is 0:
        temp = fr(blockToBin(temp), np.array(key))
        return "".join(str(i) for i in binToBlock(temp))
    temp = ft(temp)
    print(temp)
    temp = fr(temp, np.array(key))
    print(temp)
    return binToBlock(temp)

def babyr_dec(block, key):
    print("dec")

def fs(block):
    print("fs")
    table = {
        0: 10,
        1: 4,
        2: 3,
        3: 11,
        4: 8,
        5: 14,
        6: 2,
        7: 12,
        8: 5,
        9: 7,
        10: 6,
        11: 15,
        12: 0,
        13: 1,
        14: 9,
        15: 13,
    }
    def find(elem):
        return table[elem]
    return np.array(list(map(find, block)))
    # print(np.transpose(block.reshape(2, 2)))

def fsi(block):
    print("fs")
    table = {
        0: 12,
        1: 13,
        2: 6,
        3: 2,
        4: 1,
        5: 8,
        6: 10,
        7: 9,
        8: 4,
        9: 14,
        10: 0,
        11: 3,
        12: 7,
        13: 15,
        14: 5,
        15: 11,
    }
    def find(elem):
        return table[elem]
    return np.array(list(map(find, block)))

def fa(block):
    print("fa")
    result = block.copy()
    temp = result[3]
    result[3] = result[1]
    result[1] = temp
    return result

def ft(block):
    print("ft")
    t = np.array([
        1, 0, 1, 0, 0, 0, 1, 1,
        1, 1, 0, 1, 0, 0, 0, 1,
        1, 1, 1, 0, 1, 0, 0, 0,
        0, 1, 0, 1, 0, 1, 1, 1,
        0, 0, 1, 1, 1, 0, 1, 0,
        0, 0, 0, 1, 1, 1, 0, 1,
        1, 0, 0, 0, 1, 1, 1, 0,
        0, 1, 1, 1, 0, 1, 0, 1,
    ]).reshape(8, 8)
    return t.dot(blockToBin(block)) % 2

def fr(block, key):
    print("fr")
    result = []
    blockTemp = block.ravel()
    keyTemp = blockToBin(key.ravel()).ravel()
    for i, each in enumerate(blockTemp):
        result.append(each ^ keyTemp[i])
    return np.array(result).reshape(8, 2)

def reverse(w):
    result = []
    result.append(w[1])
    result.append(w[0])
    return np.array(result)

def getRoundKeys(key):
    temp = np.array(hexToBlock(key)).reshape(2, 2)
    result = []
    result.append(temp[0])
    result.append(temp[1])
    print(fs(reverse(result[1])), result[0])
    # print(np.array(result))

def hexToBlock(hex):
    result = []
    dic = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    for each in hex:
        if each in dic.keys():
            result.append(dic[each])
        else:
            result.append(int(each))
    return result

def blockToBin(block):
    result = []
    for each in block:
        temp = [int(d) for d in str(bin(each))[2:]]
        while len(temp) < 4:
            temp.insert(0, 0)
        result.append(temp)
    return np.transpose(np.array(result).ravel().reshape(2, 8))

def binToBlock(bin):
    result = []
    temp = "".join(str(i) for i in list(np.transpose(bin).ravel()))
    return hexToBlock(hex(int(temp, 2))[2:]);

block = np.array([2, 12, 10, 5])
key = np.array([6, 11, 5, 13])

# babyr_enc(block, key)
getRoundKeys("6b5d")
# babyr_dec(block, key)