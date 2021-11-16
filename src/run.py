import sys
import modulus

# import files with calculations
from strings import *

def main():
    print("start lookup")

    func = globals()[sys.argv[1]]

    print("reading input...")
    inputBytes = sys.stdin.buffer.read()
    print("read input")
    inputs = [modulus.bytesToObject(*inp) for inp in zip(modulus.decode(inputBytes), func.inputTypes)]

    sys.stdout = open("./log", "w")
    outputs = func(inputs)
    sys.stdout = sys.__stdout__

    outputBytes = modulus.encode([modulus.objectToBytes(outp) for outp in outputs])
    sys.stdout.buffer.write(outputBytes)
    # XXX: is this necessary?
    sys.stdout.flush()

print("start running")

if __name__ == "__main__":
    main()
