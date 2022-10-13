import numpy as np
import CONVERT, PERFORM, CYPHER

# decBlock -> decBlock
def reverse(matrix):
    result = []
    result.append(matrix[1])
    result.append(matrix[0])
    return result

# decBlock -> decBlock
def add(x1, x2):
    return np.array([each ^ x2[i] for i, each in enumerate(x1)])

# hexStr -> decBlock
def get_roundKeys(key):
    keys = list(np.array(CONVERT.hexStr_to_decBlock(key)).reshape(2, 2))
    
    # Perform key expansion
    for i in range(4):
        keys.extend(get_nextTwo_roundKeys(keys[i * 2], keys[i * 2 + 1], i))

    result = []
    for i in range(0, len(keys), 2):
        result.append(np.concatenate((keys[i], keys[i + 1]), axis=1))
    return np.array(result)

def get_nextTwo_roundKeys(matrix1, matrix2, round):
    result = []
    result.append(add(add(PERFORM.apply_s(reverse(matrix2), CYPHER.table_o), matrix1), np.array([pow(2, round),0])))
    result.append(add(matrix2, result[0]))
    return result;