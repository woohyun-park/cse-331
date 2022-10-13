import numpy as np
import CYPHER, CONVERT, PERFORM, HELPER

### Implementations

def babyr_enc(block, key):
    # Get round keys
    roundKeys = HELPER.get_roundKeys(key)

    # Perform encryption
    result = CONVERT.hexStr_to_decBlock(block)
    for i in range(5):
        result = babyr_enc_help(result, roundKeys[i], i)

    return CONVERT.decBlock_to_hexStr(result)

# decBlock -> decBlock
def babyr_enc_help(block, key, flag):
    if flag is 0:
        return PERFORM.add_roundKey(block, key)
    result = PERFORM.apply_s(block, CYPHER.table_o)
    result = PERFORM.apply_a(result)
    if flag is 4:
        return PERFORM.add_roundKey(result, key)
    result = PERFORM.mult_t(result, CYPHER.matrix_o)
    return PERFORM.add_roundKey(result, np.array(key))

def babyr_dec(block, key):
    # Get reversed round keys
    roundKeys = np.flipud(HELPER.get_roundKeys(key))

    # Perform decrpytion
    result = block
    for i in range(5):
        result = babyr_dec_help(CONVERT.hexStr_to_decBlock(result), roundKeys[i], i)
    
    return CONVERT.decBlock_to_hexStr(result);

# decBlock -> decBlock
def babyr_dec_help(block, key, flag):
    result = HELPER.add(CONVERT.hexStr_to_decBlock(block), key)
    if flag is 4:
        return result
    if flag is not 0:
        result = PERFORM.mult_t(result, CYPHER.matrix_i)
    result = PERFORM.apply_a(result)
    result = PERFORM.apply_s(result, CYPHER.table_i)
    return result

### Test Functions

# Toggle DETAIL for printing the details
DETAIL = False

ENC = 0
DEC = 1

def test_each(block, key, result, operation):
    if operation is ENC:
        if DETAIL:
            print('ENC, {0} + {1}:'.format(block, key))
        temp = babyr_enc(block, key)
        if temp == result:
            print("Correct!")
        else:
            print("Incorrect: {0} should be {1}".format(temp, result))
    elif operation is DEC:
        if DETAIL:
            print('DEC, {0} + {1}:'.format(block, key))
        temp = babyr_dec(block, key)
        if temp == result:
            print("Correct!")
        else:
            print("Incorrect: {0} should be {1}".format(temp, result))

def test_enc():
    print("TESTING ENCRYPTION")
    test_each("2ca5", "6b5d", "6855", ENC)
    test_each("5b69", "87b2", "5d4a", ENC)
    test_each("8f57", "5274", "4c8e", ENC)
    test_each("74e9", "9440", "bf1a", ENC)
    test_each("bf67", "cb37", "b9d8", ENC)
    print("")

def test_dec():
    print("TESTING DECRPYTION")
    test_each("6855", "6b5d", "2ca5", DEC)
    test_each("bf1a", "9440", "74e9", DEC)
    test_each("b9d8", "cb37", "bf67", DEC)
    test_each("5d4a", "87b2", "5b69", DEC)
    test_each("4c8e", "5274", "8f57", DEC)
    print("")

def main():
    test_enc()
    test_dec()

main()