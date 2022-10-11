import numpy as np

def babyr_enc(block, key):
    round_keys = getRoundKeys(key)
    result = xor(hexToBlock(block), round_keys[0])

    result = babyr_enc_help(result, round_keys[1], 1)
    result = babyr_enc_help(result, round_keys[2], 1)
    result = babyr_enc_help(result, round_keys[3], 1)
    result = babyr_enc_help(result, round_keys[4], 0)
    result = binToBlock(result)
    dic = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    resultFinal = ""
    for each in result:
        if each in dic.keys():
            resultFinal = resultFinal + dic[each]
        else:
            resultFinal = resultFinal + str(each)
    return resultFinal

def babyr_enc_help(block, key, flag):
    temp = np.array(block).copy()
    temp = fs(temp) 
    temp = fa(temp)
    if flag is 0:
        temp = fr(blockToBin(temp), np.array(key))
        return temp
    temp = ft(temp)
    temp = fr(temp, np.array(key))
    return binToBlock(temp)

def babyr_dec(block, key):
    print("dec")

def fs(block):
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

def fsi(block):
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
    result = block.copy()
    temp = result[3]
    result[3] = result[1]
    result[1] = temp
    return result

def ft(block):
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

def xor(x1, x2):
    def xorEach(a1, a2):
        return a1 ^ a2
    return np.array([each ^ x2[i] for i, each in enumerate(x1)])

def getRoundKeys(key):
    temp = np.array(hexToBlock(key)).reshape(2, 2)
    result = []
    result.append(temp[0])
    result.append(temp[1])
    result.append(xor(xor(fs(reverse(result[1])), result[0]), np.array([1,0])))
    result.append(xor(result[1], result[2]))
    result.append(xor(xor(fs(reverse(result[3])), result[2]), np.array([2,0])))
    result.append(xor(result[3], result[4]))
    result.append(xor(xor(fs(reverse(result[5])), result[4]), np.array([4,0])))
    result.append(xor(result[5], result[6]))
    result.append(xor(xor(fs(reverse(result[7])), result[6]), np.array([8,0])))
    result.append(xor(result[7], result[8]))
    resultFinal = []
    for i in range(0, len(result), 2):
        resultFinal.append(np.concatenate((result[i], result[i + 1]), axis=1))
    return np.array(resultFinal)

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

print(babyr_enc("2ca5", "6b5d")) # 6855
print(babyr_enc("5b69", "87b2")) # 5d4a
print(babyr_enc("8f57", "5274")) # 4c8e