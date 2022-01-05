import sys
import time
import modulus

# import files with calculations
from strings import *

def main():

    inputBytes = sys.stdin.buffer.read()
    inputByteStrs = modulus.decode(inputBytes)

    funcName = modulus.bytesToObject(inputByteStrs[0],"string")
    func = globals()[funcName]
    inputs = [modulus.bytesToObject(*inp) for inp in zip(inputByteStrs[1:], func.inputTypes)]

    sys.stdout = open("./log", "w")
    outputs = func(inputs)
    sys.stdout = sys.__stdout__

    outputBytes = modulus.encode([modulus.objectToBytes(outp) for outp in outputs])
    sys.stdout.buffer.write(outputBytes)
    # XXX: is this necessary?
    sys.stdout.flush()

if __name__ == "__main__":
    main()
