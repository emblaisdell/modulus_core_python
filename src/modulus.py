import sys
import os
import shutil


def calculation(inputTypes):
    def decorator(func):
        def newFunc(inputs):
            output = func(*inputs)
            if not isinstance(output, list):
                output = [output]
            return output
        newFunc.inputTypes = inputTypes
        return newFunc
    return decorator

def bytesToObject(data, dataType):    
    if dataType == "string":
        return data.decode("utf-8")
    if dataType == "integer":
        return int.from_bytes(data, byteorder='big')

def objectToBytes(obj):
    if isinstance(obj, str):
        return obj.encode("utf-8")
    if isinstance(obj, int):
        return obj.to_bytes(4, byteorder='big')


WORD_LENGTH = 4

byteorder = "little"

def decode(inputBytes):
    global byteorder
    byteorder = "big" if inputBytes[0:WORD_LENGTH//2]==b'\x00\x00' else "little"

    numArgs = int(int.from_bytes(inputBytes[0:WORD_LENGTH], byteorder=byteorder))
    lens = [int.from_bytes(inputBytes[WORD_LENGTH*i:WORD_LENGTH*(i+1)], byteorder=byteorder) for i in range(1,numArgs+1)]
    inputs = [None] * numArgs
    inputBytes = inputBytes[WORD_LENGTH*(numArgs+1):]
    for i in range(numArgs):
        split = lens[i]
        inputs[i] = inputBytes[0:split]
        inputBytes = inputBytes[split:]
    return inputs

def encode(outputs):
    global byteorder
    outputBytes = len(outputs).to_bytes(WORD_LENGTH, byteorder=byteorder)
    for output in outputs:
        outputBytes += len(output).to_bytes(WORD_LENGTH, byteorder=byteorder)
    for output in outputs:
        outputBytes += output
    return outputBytes
