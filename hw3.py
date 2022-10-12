import numpy as np
import CYPHER
import CONVERT

TABLE = CYPHER.table_o
MATRIX = CYPHER.matrix_o

def babyr_enc(block, key):
    # Get round keys
    round_keys = get_round_keys(key)

    # Perform encryption
    round_0 = xor(CONVERT.hexToBlock(block), round_keys[0])
    round_1 = babyr_enc_help(round_0, round_keys[1], 1)
    round_2 = babyr_enc_help(round_1, round_keys[2], 1)
    round_3 = babyr_enc_help(round_2, round_keys[3], 1)
    round_4 = babyr_enc_help(round_3, round_keys[4], 0)

    # Convert result to hex str
    return CONVERT.binToHexStr(round_4)

def babyr_enc_help(block, key, flag):
    temp = np.array(block).copy()
    temp = apply_s(temp, TABLE) 
    temp = apply_a(temp)
    if flag is 0:
        temp = fr(blockToBin(temp), np.array(key))
        return temp
    temp = mult_t(temp, MATRIX)
    temp = fr(temp, np.array(key))
    return CONVERT.binToBlock(temp)

def babyr_dec(block, key):
    TABLE = CYPHER.table_i
    MATRIX = CYPHER.matrix_i

def apply_s(block, table):
    return np.array(list(map(lambda elem: table[elem], block)))

def apply_a(block):
    result = block.copy()
    temp = result[3]
    result[3] = result[1]
    result[1] = temp
    return result

def mult_t(block, matrix):
    return matrix.dot(blockToBin(block)) % 2

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

def get_round_keys(key):
    temp = np.array(CONVERT.hexToBlock(key)).reshape(2, 2)
    result = []
    result.append(temp[0])
    result.append(temp[1])
    result.append(xor(xor(apply_s(reverse(result[1]), TABLE), result[0]), np.array([1,0])))
    result.append(xor(result[1], result[2]))
    result.append(xor(xor(apply_s(reverse(result[3]), TABLE), result[2]), np.array([2,0])))
    result.append(xor(result[3], result[4]))
    result.append(xor(xor(apply_s(reverse(result[5]), TABLE), result[4]), np.array([4,0])))
    result.append(xor(result[5], result[6]))
    result.append(xor(xor(apply_s(reverse(result[7]), TABLE), result[6]), np.array([8,0])))
    result.append(xor(result[7], result[8]))
    resultFinal = []
    for i in range(0, len(result), 2):
        resultFinal.append(np.concatenate((result[i], result[i + 1]), axis=1))
    return np.array(resultFinal)

def blockToBin(block):
    result = []
    for each in block:
        temp = [int(d) for d in str(bin(each))[2:]]
        while len(temp) < 4:
            temp.insert(0, 0)
        result.append(temp)
    return np.transpose(np.array(result).ravel().reshape(2, 8))

print(babyr_enc("2ca5", "6b5d")) # 6855
assert babyr_enc("2ca5", "6b5d") == "6855", "Incorrect"
print(babyr_enc("5b69", "87b2")) # 5d4a
assert babyr_enc("5b69", "87b2") == "5d4a", "Incorrect"
print(babyr_enc("8f57", "5274")) # 4c8e
assert babyr_enc("8f57", "5274") == "4c8e", "Incorrect"