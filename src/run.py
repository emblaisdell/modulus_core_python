import sys
import modulus

# import files with calculations
from strings import *

def main():
    func = globals()[sys.argv[1]]

    inputBytes = sys.stdin.buffer.read()
    inputs = [modulus.bytesToObject(*inp) for inp in zip(modulus.decode(inputBytes), func.inputTypes)]
    print("inputs")
    print(inputs)

    sys.stdout = open("./log", "w")
    outputs = func(inputs)
    sys.stdout = sys.__stdout__

    outputBytes = modulus.encode([modulus.objectToBytes(outp) for outp in outputs])
    print("outputs")
    print(outputs)
    #sys.stdout.buffer.write(outputBytes)
    # XXX: is this necessary?
    sys.stdout.flush()

if __name__ == "__main__":
    main()
