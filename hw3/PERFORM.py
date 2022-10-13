import numpy as np
import CONVERT

# decBlock -> decBlock
def apply_s(block, table):
    return np.array(list(map(lambda elem: table[elem], block)))

# decBlock -> decBlock
def apply_a(block):
    # Swap
    temp = block[3]
    block[3] = block[1]
    block[1] = temp

    return block

# decBlock -> decBlock
def mult_t(block, matrix):
    block = CONVERT.decBlock_to_BinBlock(block, 2, 8)

    # Dot product the block with matrix
    block = matrix.dot(block) % 2

    return CONVERT.binBlock_to_decBlock(block)

# decBlock -> decBlock
def add_roundKey(block, key):
    block = CONVERT.decBlock_to_BinBlock(block, 2, 8).ravel()
    key = CONVERT.decBlock_to_BinBlock(key.ravel(), 2, 8).ravel()

    # Add each elements in matrix
    result = []
    for i, each in enumerate(block):
        result.append(each ^ key[i])

    return CONVERT.binBlock_to_decBlock(np.array(result).reshape(8, 2))